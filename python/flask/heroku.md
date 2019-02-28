# heroku를 이용해 chatbot 배포하기

```bash
$ heroku login
$ heroku create ### url에 등장할 키워드 ... unique로 설정해야함
```

- app.py로 돌아와 마지막 줄을 다음과 같이 수정한다.

```python
app.run(debug=True, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))
```

- bash를 통해 파일을 하나 생성한다.

```bash
$ touch Profile # 꼭 첫글자를 대문자로 생성한다.
```

- Profile 파일로 들어와 다음을 추가한다.

> web: python app.py

- 다시 bash로 돌아와 다음을 작성한다.

```bash
$ pip freeze > requirements.txt # 사용한 모듈들을 알려주는 파일이다.
```

- 이후 변동사항을 'git push heroku master'로 푸쉬해준다.
- 만약 push가 한번에 안된다면 heroku 앱설정에 나와있는 git 주소로 'remote add heroku url'로 원격 저장소를 지정해주고 push하면 된다.
- 성공적으로 push되었다면 heroku에 url 하나가 배정되고 여기서 flask에서 작업한 것처럼 요청을 수행할 수 있게 된다.
- 앞에서 만든 telegram app.py를 사용하고자 한다면 telegram의 요청을 다시 heroku로 hook 해주는 작업을 거쳐야 한다.

> https://uakbuak.herokuapp.com/
>
> 나의 헤로쿠 주소

- web hooking 하기 : https://api.telegram.org/bot<token값>/setWebhook?url=<서버주소>/<token값>

- 이후 heroku 사이트에서 환경변수 설정을 마치면 정상적으로 telegram 요청이 c9이 아닌 telegram으로 간다.
- heroku 서버는 상시 작동하며, 30분간 요청이 없을 시에 꺼진다.

