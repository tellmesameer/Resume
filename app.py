# @app.route('/download')
# def download():
#     pdf = open('path/to/pdf', 'rb').read()
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=file.pdf'
#     return response

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)