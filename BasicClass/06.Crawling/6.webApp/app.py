from flask import Flask, request, render_template
from crawling2 import Crawling

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["GET"])
def get():
    return render_template("main.html")


# @app.route("/crawling", methods=["GET"])
# def crawling():
#     # word = requests.get('word')
#     return Crawling.interparkcrawling("부산")

@app.route("/crawling2", methods=["POST"])
def crawling():
    word = request.form.get('word')
    print(word)
    return Crawling.interparkcrawling(word)


# @app.route("/result", methods=["GET"])
# def result():
    # Crawling.interparkcrawling(word)

#     return 

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")