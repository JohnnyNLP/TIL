[TOC]

# 파이썬 함수

------



## 1. print

- print 함수는 숫자, 문자열, 리스트를 모두 출력할 수 있다.
- print 함수 내의 ""로 둘러싸인 문자열은 + 연산과 동일하다.

```python
print("life" "is" "too short")
print("life"+"is"+"too short")
```

> lifeistoo short
>
> lifeistoo short

- 문자열 띄어쓰기는 콤마로 한다.

```python
print("life", "is", "too short")
```

> life is too short

- 한 줄에 결과값을 출력하려면 인수에 end=' '을 부여한다

```python
A = ["life","is","too","short"]
for word in A:
    print(word, end=' ')
```

> life is too short



## 2. abs

- 정수나 실수의 절대값을 반환한다.
- 인자가 복소수이면 그 크기를 반환한다.

```python
a = 3 + 2j
abs(a)
```

> 3.605551275463989



## 3. len

- 객체의 길이를 반환한다.
- 인자로는 문자열, 튜플, 리스트, range, 딕셔너리 등이 들어갈 수 있다.



## 4. range

```python
numbers = range (1, 46)
print(numbers)
```

- range (a, b) 는 a 이상 b 미만의 범위를 설정해준다.
- range 객체를 리턴한다.
- 결과물이 그대로 (1, 46)으로 리턴됨



## 5. sorted

- iterable 객체를 정렬해주는 함수이다.
- key와 reverse 인자를 추가할 수 있다.
- 기본 셋팅은 오름차순, reveres=True를 부여하면 내림차순으로 정렬된다.
- key=str.lower 이라는 인자값을 부여하면 소문자가 우선하여 정렬된다.



## 6. str

- object를 str 객체로 바꾸어준다.



## 7. def

- 함수를 정의하고 싶을 땐 def 함수를 사용한다.

> def 함수명 (입력 인수) :
>
> ​	수행할 문장 1
>
> ​	수행할 문장 2
>
> ​	...
>
> ​	(return 결과값)

- 함수가 return할 수 있는 결과값은 항상 하나이다.
- 만약 경우에 따라 다른 값을 반납하고 싶다면 if문을 통해서 분기를 만들어주면 된다.
- return에 2개 이상의 값을 돌려줄 경우, return값은 튜플 형태로 만들어진다. 즉, 이 경우에도 return되는 값은 하나인 셈이다.
- 함수가 진행되다가 return과 마주하면 이후의 코드는 수행하지 않는다.



### 입력값이 없는 함수 

```python
def say()
	return('Hi')

a = say()
print(a)
```

> Hi

- 입력값(arg)이 없고 결과값(return)만 있는 함수는 변수에 대입하여 사용해야 한다.

  > 결과값을 받을 변수 = 함수명()



### 결과값이  없는  함수

```python
def sum(a, b)
	print("%d, %d의 합은 %d입니다." %(a, b, a+b))
    
sum(3, 4)
```

> 3, 4의 합은 7입니다.

- return과 print는 결과값이 있고 없고의 중요한 차이가 있다.

- 결과값이 없는 함수는 함수만  호출하여 사용한다. 즉, 변수에 대입할 수 없다.

  > 함수명 (입력 인수1, 2, ...)



###  입력값과 결과값이 모두 없는 함수

```python
def say()
	print('Hi')
    
say()
```

> Hi

- 입력인수도 결과값도 존재하지 않는 경우는 오로지 함수 호출로만 사용할 수 있다.

  > 함수명 ()



### 입력인수가 여러개인 경우

> def 함수명 ( *입력변수) :
>
> ​	수행할 문장
>
> ​	...
>
> ​	return

- 간단하게 입력변수 앞에 *을 써주면 된다.



### 입력인수에 초기값 설정하기

> def 함수명 (입력변수1, 입력변수2, ... 초기값=설정값)
>
> ​	수행할 문장
>
> ​	...
>
> ​	return

- 기존의 입력인수가 입력인수 이름만 주는 방식이었다면, 초기값은 = 연산자를 통해 특정 설정값으로 미리 초기화가 가능하다.

- 초기값을 주는 경우에 입력인수를 모두 적은 뒤에 적는게 좋은데, 만약 초기값이 입력인수 사이에 온다면 초기화가 제대로 이루어지지 않아서 오류가 발생한다.

  

###     피보나치 함수(재귀함수) 정의하기

```python
def fib(n):
	if n == 0 : return 0
	if n == 1 : return 1
	return fib(n-2) + fib(n-1)
fib(6) 
```

> 8 # 0부터 0, 1, 1, 2, 3, 5, 8

