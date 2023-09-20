from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    image_path = '/static/images/cat.jpg'
    name = 'cameron'
    description = 'verry cute!'
    btn_msg = 'more read'
    return render_template('index.html', image_path=image_path, name=name, description=description, btn_msg=btn_msg)

if __name__ == '__main__':
    app.run(port=5050)
