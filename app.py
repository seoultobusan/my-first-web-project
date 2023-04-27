import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET',])
def index():
    return """
<html>
    <head>
        <title>
        this is my first web project
        </title>
    </head>
    <body>
        <div>
            <h1>Hello World!</h1>
            <p>
                이것은 이우용의 첫번째 파이썬 정적 웹 프로젝트 입니다.
            </p>
            <a href="https://oboki.net">동일이 형 블로그로 이동하기</a>
        </div>
    <body>
</html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')