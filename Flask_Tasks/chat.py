from flask import Flask, Response
import matplotlib.pyplot as plt
import io, random, webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "Simple Flask Data Dashboard<br><br>"
        "Use:<br>"
        "/plot — to view a random data chart"
    )

@app.route('/plot')
def plot():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [random.randint(10, 100) for _ in x]
    plt.plot(x, y, marker='o')
    plt.title("Random Data Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5004/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, port=5004)