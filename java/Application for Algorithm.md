# Application for Algorithm



## int형 숫자의 자릿수 구하기

- String 객체의 경우, 길이를 구하기 위해 String.length() 함수를 이용할 수 있다.
- 그러나 이와 유사한 Integer 객체의 .SIZE()라는 함수는 해당 정수의 바이트 값을 return해주는 다른 용도의 함수이다.
- int의 자릿수를 구하기 위해서는 수학적 접근 방식을 취해야 한다.

```java
int length = (int)(Math.log10(a)+1);
```

- 밑이 10인 로그는 해당 정수에 10이 총 몇번 곱해졌는지를 알려준다.
- 즉, 일의 자릿수를 제외한 자릿수의 개수인 셈이다.
- 그러므로 총 자릿수는 그 값에 1을 더해주어야 한다.
- 그런데 Math.log() 함수의 return 값은 double이기 때문에 int로 형변환 해주어야 한다.