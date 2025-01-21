from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal (Landing Page)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para "Cotizador de proyectos solares"
@app.route('/calculadora_solar')
def calculadora_solar():
    return render_template('calculadora_solar.html')

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

    

