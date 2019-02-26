# SMTP을 이용해 메일 보내기



```python
import csv
import smtplib
from email.message import EmailMessage # 파이썬이 원래 가지고 있는 email이라는 모듈
from email.mime.application import MIMEApplication
from jinja2 import Template
import getpass
password = getpass.getpass("password : ")

smtp = smtplib.SMTP_SSL("smtp.naver.com",465)
        # 네이버 메일 서버로 접속, 네이버 메일 환경설정에서 SMTP 서버와 포트번호를 사용
smtp.login("userid", password)
filename = "image.jpg"
# rb : read binary
with open(filename, "rb") as img_file :
    img = img_file.read() # 파일을 읽어서 img 변수에 넣기
    
    # csv 파일 읽기 위한 with
    with open("mailbakery-kappa-regular.html", "r", encoding="utf-8") as html :
        email_template = html.read()
        t = Template(email_template)
        render_html = t.render() # python 코드를 html안에서 사용할 수 있도록 한다.
        with open("student_list.csv","r") as f:
            # ex) 박찬희, pchmarine@naver.com, 출석,
            csv_reader = csv.reader(f) 
            for student in csv_reader :
                msg = EmailMessage() # 메일 하나의 객체
                msg["Subject"] = f"{student[0]}님 서류결과"
                msg["From"] = "userid@naver.com"
                msg["To"] = student[1]
                msg.add_alternative(render_html, subtype= "html")
                # subtype 으로 어떤 형식인지 알려줘야한다.
                part = MIMEApplication(img, name=filename)
                msg.attach(part) # 이미지첨부
                smtp.send_message(msg)
```

