from flask import Flask, render_template, request

app = Flask(__name__)

# Funksjon som håndterer både kryptering og dekryptering
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        mode = request.form['mode']
        text = request.form['text']
        shift = int(request.form['shift'])

        if mode == 'encrypt':
            result = caesar_encrypt(text, shift)
        elif mode == 'decrypt':
            result = caesar_encrypt(text, -shift)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
