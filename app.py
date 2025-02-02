from flask import Flask, render_template, request, send_file
from modules.pdf_generator import generar_pdf 
from modules.calculos_solar import CalculoNumeroPaneles  # Importar la clase

app = Flask(__name__)

# ---------------------RUTAS------------------------------

# Ruta principal (Landing Page)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para "Cotizador de proyectos solares"
@app.route('/calculadora_solar')
def calculadora_solar():
    return render_template('calculadora_solar.html')

# Ruta para generar PDF del "Cotizador de proyectos solares"
@app.route('/generar_pdf', methods=['POST'])
def generar_pdf_route():
    if request.method == 'POST':
        # Recibir datos del formulario
        cliente = request.form['cliente']
        proyecto = request.form['proyecto']
        correo = request.form['correo']
        correo_asesor = request.form['correo_asesor']
        celular = request.form['celular']
        ubicacion = request.form['ubicacion']
        potencia = float(request.form['potencia'])
        costo = float(request.form['costo'])
        area = float(request.form['area'])
        
         # ✅ Calcular la energía generada y el número de paneles
        calculo = CalculoNumeroPaneles(ubicacion, potencia)
        energia_generada = calculo.energia_generada_por_panel()  

        # Extraer los valores importantes
        consumo_anual = energia_generada["Consumo Anual (kWh)"]
        paneles_400 = energia_generada["Número de paneles de 400W"]
        paneles_585 = energia_generada["Número de paneles de 585W"]
        paneles_605 = energia_generada["Número de paneles de 605W"]

        # Generar PDF utilizando el módulo y pasar los valores como argumentos
        pdf_path = generar_pdf(cliente, proyecto, celular, correo_asesor, correo, 
                       ubicacion, potencia, costo, area, 
                       consumo_anual, paneles_400, paneles_585, paneles_605)

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