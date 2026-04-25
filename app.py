import os
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Настройки Telegram (Замени на свои данные)
TELEGRAM_TOKEN = "8268190336:AAHTaPqyiy7nXgzIncNeJgYrnNXCjs5lY2k"
TELEGRAM_CHAT_ID = "5541846108"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")

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
        
        # Отправка в Telegram
        tg_message = f"🚀 Новый заказ KaraamDev!\n\n👤 Имя: {name}\n📧 Email: {email}\n📝 Сообщение: {message}"
        send_telegram(tg_message)
        
        # Сохранение в файл (на всякий случай)
        with open('orders.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name} | Email: {email} | Сообщение: {message}\n")
            f.write("-" * 30 + "\n")
            
        return render_template('order.html', success=True)
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
