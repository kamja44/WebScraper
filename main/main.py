from flask import Flask

app = Flask("JobScrapper")

@app.route("/") # decorator <- /페이지에 접속했을 때 home함수 실행
def home():
    return "hi there!"

app.run("127.0.0.1")