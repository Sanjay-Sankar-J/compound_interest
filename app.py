from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate/n)**(n*time)
    return round(amount, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    final_amount = None
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate']) / 100
        time = float(request.form['time'])
        n = int(request.form['n'])
        
        final_amount = calculate_compound_interest(principal, rate, time, n)

    return render_template('index.html', final_amount=final_amount)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
