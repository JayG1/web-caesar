from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-sarif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="/encrypt" method="post">
            <label>Rotate by:
            <input type="text" name="rot" value="0">
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit">
        </form>

    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    rot_string = int(request.form['rot'])
    text_string = request.form['text']
    display = rotate_string(text_string, rot_string)
    return '<h1>' + form.format(display) + '</h1>'

app.run()