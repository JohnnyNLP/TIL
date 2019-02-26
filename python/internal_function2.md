

[TOC]

# 파이썬 함수 -2

------



## 1. for

```python
greeting="Hi!!!"

for i in range(10):
for i in "abcdefghij":
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(greeting)
```

- in 뒤에는 range, string, list, tuple 형태의 자료형(끝이 정해져 있는)이라면 뭐든 들어갈 수 있다.
- for문에 범위를 정해준 뒤에는 꼭 :를 적고 줄바꿈한다.
- 줄바꿈을 한 뒤에 실제로 적용할 함수 부분에는 `들여쓰기`를 해주어야 한다. (4space 권장)



## 2. if

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&numOfRows=10&pageSize=10&pageNo=3&startPage=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
gangnam = soup('item')[7]
location = gangnam.stationName.text
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)

if (dust > 150) :
  status = "매우 나쁨"
elif (dust <= 150 and dust > 80) :
  status = "나쁨"
elif (dust <= 80 and dust > 30) :
  status = "보통"
else :
  status = "좋음"
  
print("{0} 기준 {1}의 미세먼지 농도는 {2}이고, 상태는 {3}입니다.".format(time,location,dust, status))
```

- if 문에는 참/거짓을 판별할 문자식을 준다.
- elif 는 부여하고 싶은 조건이 더 있을 경우에 사용한다.
- else 는 나머지 경우에 수행할 명령을 적는다.
- 사실 위의 작성 방식은 자바에 근접하고, 파이썬에서는 다음과 같이 훨씬 간결하게 표현할 수 있다.



```python
if dust > 150 :
  status = "매우 나쁨"
elif 80 < dust <= 150 :
  status = "나쁨"
elif 30 < dust <= 80 :
  status = "보통"
else :
  status = "좋음"
```

- 괄호를 생략할 수 있다.
- 조건을 줄 때 연산자를 오른쪽 뿐만 아니라 왼쪽에도 쓸 수 있다.



## 3. open/close

##### 		a. write() 함수

```python
f = open("/c/Users/student/Desktop/newtext.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

- open("파일의 경로", "파일의 열기 모드") 형식으로 파일을 불러올 수 있다.
- 파일 열기 모드는 다음과 같다
  - r : 읽기
  - w : 쓰기
  - a : 추가하기
- 만약 파일이 존재하지 않는다면 해당 파일을 자동으로 생성한다.
- 이미 존재하는 파일이라면 'w' 명령어 수행시 기존의 내용이 모두 날아가버린다.



##### 		b. readline() 함수

```python
f = open("/c/Users/student/Desktop/newtext.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
```

> 1번째 줄입니다.
>
> 2번째 줄입니다.
>
> ...
>
> 10번째 줄입니다.

- readline()은 더 이상 읽을 라인이 없을 경우 None을 출력한다.

  

  ##### 	c. readlines() 함수

```python
f = open("/c/Users/student/Desktop/newtext.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```

- readline()은 한 줄씩 읽어오는 반면, readlines()는 여러 줄을 리스트 형태로 출력한다.



##### 		d. read() 함수

```	python
f = open("/c/Users/student/Desktop/newtext.txt", 'r')
data = f.read()
print(data)
f.close()
```

- read() 함수는 파일 내용 전체를 객체로 리턴한다.



##### 	e. 추가하기

```python
f = open("/c/Users/student/Desktop/newtext.txt", 'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

> 1번째 줄입니다.
>
> 2번째 줄입니다.
>
> ...
>
> 20번째 줄입니다.

- 기존의 데이터를 날려버리는 w와는 달리 a는 기존의 내용에 추가로 내용을 작성하고 싶을 때 사용한다.



## 4. with/as

```python
"with" expression ["as" target] ":" suite
# 출처: https://ingorae.tistory.com/505 [잉고래의 잇다이어리]
```

- with문의 기본 구조이다.



```python
with open("test.txt", "w") as f:
    f.write("Life is too short, you need python")
```

> "Life is too short, you need python"	

- with는 open/close 기능을 동시에 수행하는 함수이다.
- with문은 내부의 명령어를 모두 수행하면 자동으로 파일을 close한다.
- 이를 통해 코드가 한결 간결해진다.

