from flask import Flask, render_template, request, send_file
from modules.pdf_generator import generar_pdf 
from modules.pdf_generator_ferragro import generar_pdf_ferragro 
from modules.calculos_solar import calcular_proyecto
import json
import os
from datetime import datetime

app = Flask(__name__)

# ✅ LOGICA DEL NUMERO DE COTIZACIÓN
def cargar_cotizacion():
    """Carga el número de cotización desde un archivo JSON."""
    if os.path.exists("cotizacion.json"):
        with open("cotizacion.json", "r") as file:
            return json.load(file).get("cotizacion", 0)
    return 0

def guardar_cotizacion(numero):
    """Guarda el número de cotización en un archivo JSON."""
    with open("cotizacion.json", "w") as file:
        json.dump({"cotizacion": numero}, file)

cotizacion_contador = cargar_cotizacion()

# --------------------- RUTAS ------------------------------

# 🔹 Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 Cotizador de Proyectos Solares (Landing Solar)
@app.route('/calculadora_solar')
def calculadora_solar():
    return render_template('calculadora_solar.html')

@app.route('/calculadora_ia')
def calculadora_solar_ia():
    return render_template('calculadora_ia.html')

# 🔹 Cotizador de Equipos Solares
@app.route('/calculadora_equipos')
def calculadora_equipos():
    return render_template('calculadora_equipos.html')

# 🔹 Cotizador de Equipos Ferragro (Landing específica)
@app.route('/calculadora_equipos_ferragro')
def calculadora_equipos_ferragro():
    return render_template('calculadora_equipos_ferragro.html')

# 🔹 Generar PDF para la Calculadora Solar
@app.route('/generar_pdf', methods=['POST'])
def generar_pdf_route():
    global cotizacion_contador
    cotizacion_contador += 1  
    guardar_cotizacion(cotizacion_contador)  

    try:
        cliente = request.form['cliente']
        proyecto = request.form['proyecto']
        celular = request.form['celular']
        correo_asesor = request.form['correo_asesor']
        correo = request.form['correo']
        ubicacion = request.form['ubicacion']
        potencia = float(request.form['potencia'])
        costo = float(request.form['costo'])
        area = float(request.form['area'])

        fecha_cotizacion = datetime.now().strftime("%d/%m/%Y")

        # ✅ Calcular los datos del proyecto
        datos_proyecto = calcular_proyecto(ubicacion, potencia, costo)

        # ✅ Generar el PDF con el módulo estándar
        pdf_path = generar_pdf(
            cotizacion_contador, fecha_cotizacion, cliente, proyecto, celular, 
            correo, correo_asesor, ubicacion, potencia, costo, area, datos_proyecto
        )

        return send_file(pdf_path, as_attachment=True)
    except KeyError as e:
        return f"Error: Falta el campo {str(e)} en el formulario", 400
    except ValueError:
        return "Error: Verifica que los campos numéricos sean correctos.", 400

# 🔹 Generar PDF para la Calculadora de Equipos Ferragro
@app.route('/generar_pdf_ferragro', methods=['POST'])
def generar_pdf_ferragro_route():
    global cotizacion_contador
    cotizacion_contador += 1  
    guardar_cotizacion(cotizacion_contador)  

    try:
        cliente = request.form['cliente']
        proyecto = request.form['proyecto']
        celular = request.form['celular']
        correo_asesor = request.form['correo_asesor']
        correo = request.form['correo']
        ubicacion = request.form['ubicacion']
        potencia = float(request.form['potencia'])
        costo = float(request.form['costo'])
        area = float(request.form['area'])

        fecha_cotizacion = datetime.now().strftime("%d/%m/%Y")

        # ✅ Calcular datos del proyecto
        datos_proyecto = calcular_proyecto(ubicacion, potencia, costo)

        # ✅ Generar el PDF específico para Ferragro
        pdf_path = generar_pdf_ferragro(
            cotizacion_contador, fecha_cotizacion, cliente, proyecto, celular, 
            correo, correo_asesor, ubicacion, potencia, costo, area, datos_proyecto
        )

        return send_file(pdf_path, as_attachment=True)
    except KeyError as e:
        return f"Error: Falta el campo {str(e)} en el formulario", 400
    except ValueError:
        return "Error: Verifica que los campos numéricos sean correctos.", 400

# 🔹 Otras páginas estáticas
@app.route('/diligenciamiento_contratos')
def diligenciamiento_contratos():
    return render_template('diligenciamiento_contratos.html')

@app.route('/instalaciones_terceros')
def instalaciones_terceros():
    return render_template('instalaciones_terceros.html')

@app.route('/sagrilaft')
def sagrilaft():
    return render_template('sagrilaft.html')

# --------------------- EJECUCIÓN DEL SERVIDOR ------------------------------
if __name__ == '__main__':
    app.run(debug=True)
