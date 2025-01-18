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
    

