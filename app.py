from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    files = [file for file in range(100)]
    std::cout << "files": function(34)
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True)
