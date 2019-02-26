

[TOC]

# 파이썬 Day1

------



## 자료형



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

