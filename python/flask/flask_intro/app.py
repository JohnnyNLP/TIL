# 플라스크 사용 선언
import random
from flask import Flask, render_template
from faker import Faker
import requests

app = Flask(__name__)

# / 를 기본 url로 경로설정 해주는 부분 (servlet mapping과 유사)
# 즉, app.route를 이용해 경로를 설정하고 해당 부분에 코드를 추가하면 된다.
@app.route("/")
def hello():
    return "안녕하세요!"
    
@app.route("/multi_c")
def greeting():
    return "멀캠 C반"
    
@app.route("/html_tag")
def html_tag(): # 선언하는 함수명은 route값과 일치하게 주는 것이 관례
    return """
    <h1>html 태그도 전송이 가능합니다.</h1>
    <p>p 태그도 전송이 가능합니다.</p>
    """

@app.route("/html_file")    
def html_file():
    return render_template("html.html")

@app.route("/hi/<string:name>") #<데이터타입:변수명>
def hi(name):
    return render_template("hi.html", name=name)
    
@app.route("/cube/<int:num>") #<데이터타입:변수명>
def cube(num):
    # cubic = num * num * num
    cubic = num ** 3
    return render_template("cube.html", num=num, cubic=cubic)
    # html에게 전달해줄 변수명=함수 내에서 정의된 변수명
    # request.setParameter("name", "value")와 비슷하다고 이해하면 될 듯.

@app.route("/dinner")
def dinner():
    menu_list = ["김밥까페", "시골집", "강남목장"]
    pick = random.choice(menu_list)
    return render_template("dinner.html", pick=pick)
    
@app.route("/lotto")
def lotto():
    numbers = range(1, 46)
    pick = random.sample(numbers, 6)
    return render_template("lotto.html", pick=pick)
    
@app.route("/random_img")
def random_img():
    return render_template("random_img.html")

@app.route("/ego/<string:name>")
def ego(name):
    url = "http://api.giphy.com/v1/gifs/search?api_key=xWsN9spauUQ86kH9uaEyz9khJrKKz7PT&q="
    fake = Faker("ko_KR")
    job = fake.job()
    res = requests.get(url+job).json() # json 형태의 데이터를 딕셔너리로 바꾸어주는 역할
    img_url = res["data"][0]["images"]["original"]["url"]
    return render_template("ego.html", img_url=img_url, name=name, job=job)

# 서버실행 옵션
if __name__ == '__main__': # 모듈로 실행되었는지, 파일로 직접 실행되었는지 확인
    app.run(debug=True, host='0.0.0.0', port=8080) 