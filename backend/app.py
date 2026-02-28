from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    # This sends the index.html file from the frontend folder
    return send_file('../frontend/index.html')

if __name__ == '__main__':
    app.run(debug=True)
