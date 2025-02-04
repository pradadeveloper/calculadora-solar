from flask import Flask, render_template, request, send_file
from modules.pdf_generator import generar_pdf 
from modules.calculos_solar import calcular_proyecto
import json
import os
from datetime import datetime

app = Flask(__name__)


# LOGICA DEL NUMERO DE COTIZACIÓN
# Cargar el número de cotización desde un archivo JSON
def cargar_cotizacion():
    if os.path.exists("cotizacion.json"):
        with open("cotizacion.json", "r") as file:
            return json.load(file).get("cotizacion", 0)
    return 0

# Guardar el número de cotización en un archivo JSON
def guardar_cotizacion(numero):
    with open("cotizacion.json", "w") as file:
        json.dump({"cotizacion": numero}, file)

# Inicializar el contador de cotizaciones
cotizacion_contador = cargar_cotizacion()

# ---------------------RUTAS------------------------------

# Ruta principal (Landing Page)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para "Cotizador de proyectos solares"
@app.route('/calculadora_solar')
def calculadora_solar():
    return render_template('calculadora_solar.html')

@app.route('/generar_pdf', methods=['POST'])
def generar_pdf_route():
    global cotizacion_contador
    cotizacion_contador += 1  # Incrementamos la cotización
    guardar_cotizacion(cotizacion_contador)  # Guardamos en el archivo

    # Recibir datos del formulario
    cliente = request.form['cliente']
    proyecto = request.form['proyecto']
    celular = request.form['celular']
    correo_asesor = request.form['correo_asesor']
    correo = request.form['correo']
    ubicacion = request.form['ubicacion']
    potencia = float(request.form['potencia'])
    costo = float(request.form['costo'])
    area = float(request.form['area'])
    
    # Obtener la fecha actual en formato día/mes/año
    fecha_cotizacion = datetime.now().strftime("%d/%m/%Y")

    # **✅ CALCULAR TODOS LOS DATOS DEL PROYECTO**
    datos_proyecto = calcular_proyecto(ubicacion, potencia, costo)

    # **✅ GENERAR EL PDF**
    pdf_path = generar_pdf(cotizacion_contador,fecha_cotizacion, cliente, proyecto, celular,correo, correo_asesor, ubicacion, potencia, costo, area, datos_proyecto)

    return send_file(pdf_path, as_attachment=True)

# Ruta para "Cotizador de equipos solares"
@app.route('/calculadora_equipos')
def calculadora_equipos():
    return render_template('calculadora_equipos.html')

# Ruta para "Diligenciamiento de contratos"
@app.route('/diligenciamiento_contratos')
def diligenciamiento_contratos():
    return render_template('diligenciamiento_contratos.html')

# Ruta para "Servicios de instalaciones terceros"
@app.route('/instalaciones_terceros')
def instalaciones_terceros():
    return render_template('instalaciones_terceros.html')

# Ruta para "Diligenciamiento de SAGRILAFT"
@app.route('/sagrilaft')
def sagrilaft():
    return render_template('sagrilaft.html')

# Única instancia de ejecución del servidor
if __name__ == '__main__':
    app.run(debug=True)