from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return html_code

with open('home.html', 'r') as f:
    html_code = f.read()

if __name__ == '__main__':
    app.debug = True
    app.run()