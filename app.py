from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    resultado = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            resultado = a + b
        except ValueError:
            resultado = "Error ingresa números validos"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
    

# Back-end en Python con Flask (para la lógica de la suma).

# Front-end simple en HTML para interactuar con el usuario.

# Despliegue en internet utilizando Render o PythonAnywhere.


# Explicación: La ruta '/' muestra el formulario HTML. Cuando el usuario envía los datos, Flask recibe los valores a y b, realiza la suma y envía el resultado a la página.
