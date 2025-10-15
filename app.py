from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 and num2:
            try:
                result = float(num1) + float(num2)
            except ValueError:
                result = 'Invalid input. Please enter numbers only.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)