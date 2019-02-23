

# 파이썬 Day1



## 자료형

1. 숫자
2. 문자
3. 참/거짓
4. 리스트
5. 딕셔너리



### 1. 숫자

```python 
number1 = 1 # number라는 변수에 정수를 넣을 수 있다.
number2 = -3 # 음수도 가능.
number3 = 3j+4 # 복소수도 넣을 수 있다.
```

### 2. 문자

> 파이썬에서 큰따옴표와 작은따옴표는 동일하다.

```python
string1 = "파이썬" # 파이썬에서는 큰따옴표 안에 문자열을 넣는다.
```

### 3. 참/거짓

```python
my_bool = True # 시작은 대문자로 적어야한다.
```

### 4. 리스트

리스트는 다음과 같이 생겼다.

```python 
menu = ["피자", "치킨", "파스타", "돈까스", "불닭볶음면", "치즈찜닭"]
```

- 리스트 안에는 어떤 자료형도 포함시킬 수 있다.
- menu[0] 과 같이 인덱스를 이용할 수 있다.
- menu[0:3] 과 같이 슬라이싱을 이용할 수 있다.

### 5. 딕셔너리

딕셔너리의 예시는 다음과 같다.

```python 
restaurants = {"피자":"02-1234-5678",
        "치킨":"02-1234-5678",
        "파스타":"02-1234-5678",
        "돈까스":"02-1234-5678",
        "치즈찜닭":"02-1234-5678"}
```

- 딕셔너리는 {key:value}의 쌍으로 구성된다.

- 대표적인 데이터 타입 중 json이 딕셔너리의 형태로 구성된다.

- restaurants.keys()를 통해 key값만 반환받을 수 있다.

- restaurants.values()를 통해 value값만 반환받을 수 있다.

  > 이렇게 반환받은 결과물은 list 타입이 아니다!!

```python
list(restaurants.keys())
```

- 다음과 같이 반환되는 결과물을 리스트로 변환해주는 과정을 거쳐야 한다.



## 함수

1. for문 사용하기
2. if문 사용하기



### 1. for문 사용하기

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



### 2. if문 사용하기

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

