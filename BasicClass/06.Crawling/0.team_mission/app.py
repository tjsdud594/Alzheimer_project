from flask import Flask, request, render_template
from crawling import Crawling

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["GET"])
def get():
    return render_template("index.html")

@app.route("/crawling2", methods=["POST"])
def crawling_300():
    # word = request.form.get('word')
    # print(word)
    

    return Crawling.youtube_300rank_sub()

@app.route("/crawling3", methods=["POST"])
def crawling_300_video():
    # word = request.form.get('word')
    # print(word)

    return Crawling.youtube_300rank_video()


if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
