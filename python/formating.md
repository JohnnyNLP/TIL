# 문자열 포매팅

1. 숫자 바로 대입하기

2. 문자열 바로 대입하기

3. 숫자 값을 가진 변수로 대입하기

4. 2개 이상의 값 넣기

5. 이름으로 넣기

6. 인덱스와 이름을 혼용해서 넣기

7. 왼쪽 정렬

8. 오른쪽 정렬

9. 가운데 정렬

10.  공백 채우기
11. 소수점 표현하기
12. '{' 또는 '}' 문자 표현하기
13. 정리



## 1. 숫자 바로 대입하기

- 표현식

```python
"I eat {0} apples" .format(3)
```

- 결과물

```python
'I eat 3 apples'
```



## 2. 문자열 바로 대입하기

- 표현식

```python
"I eat {0} apples" .format("five")
```

- 결과물

```python
'I eat five apples'
```



## 3. 숫자 값을 가진 변수로 대입하기

- 표현식

```python
number = 3
"I eat {0} apples" .format(number)
```

- 결과물

```python
'I eat 3 apples'
```



## 4. 2개 이상의 값 넣기

- 표현식

```python
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days." .format(number, day)
```

- 결과물

```python
'I ate 10 apples. so I was sick for three days.'
```



## 5. 이름으로 넣기

- 표현식

```python
"I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3)
```

- 결과물

```python
'I ate 10 apples. so I was sick for 3 days.'
```



## 6. 인덱스와 이름을 혼용해서 넣기

- 표현식

```python
"I ate {0} apples. so I was sick for {day} days." .format(10, day=3)
```

- 결과물

```python
'I ate 10 apples. so I was sick for 3 days.'
```



## 7. 왼쪽 정렬

- 표현식

```python
"{0:<10}" .format("hi")
```

- 결과물

```python
'hi        '
```



## 8. 오른쪽 정렬

- 표현식

```python
"{0:>10}" .format("hi")
```

- 결과물

```python
'        hi'
```



## 9. 가운데 정렬

- 표현식

```python
"{0:^10}" .format("hi")
```

- 결과물

```python
'    hi    '
```



## 10. 공백 채우기

- 표현식

```python
"{0:=^10}" .formnat("hi")
"{0:!<10}" .format("hi")
```

- 결과물

```python
'====hi===='
'hi!!!!!!!!'
```



## 11. 소수점 표현하기

- 표현식

```python
y = 3.42134234
"{0:0.4f}" .format(y)
"{0:10.4f}" .format(y)
```

- 결과물

```python
'3.4213'
'    3.4213'
```

- 참고

```python
"%0.4f" %3.42134234
"%10.4f" %3.42134234
# 결과물은 각각 다음과 같다
'3.4213' # 소수점 4자리까지 표현
'    3.4213' # 위의 결과물을 총 10개의 문자열 공간에서 표현
```



## 12. '{' 또는 '}' 문자 표현하기

- 표현식

```python
"{{ and }}" .format()
```

- 결과물

```python
'{ and }'
```



## 13. 정리

- 문자열 내부에 {0}, {1} 꼴의 코드를 입력하면 .format(a, b)에 입력한 a와  b가 각각 순차적으로 들어간다.
- 문자열 내부에 {변수명} 꼴의 코드를  입력하면 .format(변수명)에 입력한 변수값이 그에 맞게 들어간다.
- .format 내부에 들어가는 문자는 정수, 문자, 변수명, 변수=값 의 형태가 있다.
- "{0:=<10}" 에서 ':'는 정렬을, <는 정렬 방향을, 10은 총 문자열의 길이를, =는 공백을 대신할 문자를 의미한다.
- "" 내부에 {}을 표현하고 싶다면 두 번씩 작성하면 된다.