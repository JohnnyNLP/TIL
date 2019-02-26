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

## 3. len

## 4. range

```python
numbers = range (1, 46)
print(numbers)
```

- range (a, b) 는 a 이상 b 미만의 범위를 설정해준다.
- range 객체를 리턴한다.
- 결과물이 그대로 (1, 46)으로 리턴됨



## 5. sorted

## 6. str

## 7. def

- 함수를 정의하고 싶을 땐 def 함수를 사용한다.

###     피보나치 함수(재귀함수) 정의하기

```python
def fib(n):
	if n == 0 : return 0
	if n == 1 : return 1
	return fib(n-2) + fib(n-1)
fib(6) 
```

> 8 # 0부터 0, 1, 1, 2, 3, 5, 8

