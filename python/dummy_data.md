

[TOC]

# 더미 데이터 만들기

------



```bash
$ pip install faker
$ touch make_student.py
$ touch change.py
```



### 1. make_student.py

```python
import os
from faker import Faker

fake = Faker("ko_KR")
for i in range(100):
    name = fake.name()
    cmd = f"touch {str(i)}_{name}.txt"
    os.system(cmd)
```

> 해당 폴더에 임의의 이름.txt 파일이 100개 생성된다.



### 2. change.py

```bash
$ pwd
#를 이용하여 현재 경로를 복사한다.
```

```python
import os

# 해당 폴더로 이동
os.chdir("/home/ubuntu/workspace/monday/student_list")

# 폴더 안에 모든 파일을 돌면서 이름을 바꾼다
for filename in os.listdir("."): # 현재 위치의 모든 파일 리스트를 리턴
    os.rename(filename, "student"+filename) # 최초로 설정하기
    os.rename(filename, filename.replace("student", "MC")) # 설정값 다시 바꾸기
```

