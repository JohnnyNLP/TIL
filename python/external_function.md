# 파이썬 함수2

## 목차

1. #### random



## 1. random



##### 	a. random.choice (한 개)

```python
import random

menu = ["피자", "치킨", "파스타", "돈까스", "불닭볶음면", "치즈찜닭"]
choice = random.choice(menu)
print(choice)
```

- 리스트 안에서 임의의 원소 하나를 리턴



##### 	b. random.sample (여러 개)

```python
import random

lotto = random.sample(range(1, 46), 6)
print(sorted(lotto))
```

- random.sample(a, b)는 a 리스트 범위 내에서 b 개의 원소를 임의로 추출해준다.
- 여러 개면 자동으로 배열을 리턴한다.

