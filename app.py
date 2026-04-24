from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Сохранение в файл
        with open('orders.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name} | Email: {email} | Сообщение: {message}\n")
            f.write("-" * 30 + "\n")
            
        print(f"Новый заказ сохранен в orders.txt: {name}")
        return render_template('order.html', success=True)
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
