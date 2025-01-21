from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Configuración de directorios
PDF_FOLDER = 'generated_pdfs'
os.makedirs(PDF_FOLDER, exist_ok=True)

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
def generar_pdf():
    if request.method == 'POST':
        # Recibir datos del formulario
        cliente = request.form['cliente']
        proyecto = request.form['proyecto']
        ubicacion = request.form['ubicacion']
        potencia = request.form['potencia']
        costo = request.form['costo']

        # Crear PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)

        # Logo
        pdf.image('./static/css/imagenes/logo solartech.png', x=10, y=8, w=30)

        # Título
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(200, 10, txt="Cotización de Proyecto Solar", ln=True, align='C')

        # Información del cliente
        pdf.set_font('Arial', size=12)
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=True)
        pdf.cell(200, 10, txt=f"Proyecto: {proyecto}", ln=True)
        pdf.cell(200, 10, txt=f"Ubicación: {ubicacion}", ln=True)
        pdf.cell(200, 10, txt=f"Potencia Instalada: {potencia} kWp", ln=True)
        pdf.cell(200, 10, txt=f"Costo del Proyecto: ${costo}", ln=True)

        # Guardar PDF
        pdf_path = os.path.join(PDF_FOLDER, 'cotizacion.pdf')
        pdf.output(pdf_path)

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

if __name__ == '__main__':
    app.run(debug=True)


    

