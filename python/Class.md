# Class

- 클래스는 특정 기능을 담고 있는 메소드들의 집합체이다.
- 궁극적인 목표는 코드의 재사용으로 파일을 가능한 한 반복 없이 가볍게 만드는 것이다.
- 클래스로 만들어낸 객체를 인스턴스라고 한다.
- 코드 내에서 사용할 수 있는 메소드, 변수 등을 객체라고 하는데, 특정 클래스에 의해 만들어진 객체를 그 클래스의 인스턴스라고 명명한다.
- 



## self인수

- 파이썬은 클래스 내부에 메소드를 생성할 때 항상 첫 번째 인수로 self를 설정해주어야 한다.
- self는 호출 시에 이용했던 인스턴스 자신을 지칭한다.
- 이후 클래스 내부에서 특정 인수를 생성해 사용하고자 한다면 'self.변수명 = 대입값'의 형태로 지정해줄 수 있다.



## \__init__

- \__init__ 메소드는 자바의 생성자와 기능이 유사하다.
- \__init__을 통해 특정 매개 변수를 입력받을 수 있다.
- 이렇게 입력받은 매개 변수는 인스턴스 내의 지역 변수처럼 활용이 가능하다.



## 사칙연산 클래스 만들기

```python
class FourCal :
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self) :
        result = self.first + self.second
        return result
    def mul(self) :
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result
    
a = FourCal()
a.setdata(3,6)
a.sum()
a.mul()
a.sub()
a.div()
```

> 9
>
> 18
>
> -3
>
> 0.5



## 상속과 오버라이딩 예제

```python
class HouseLee :
    lastname = "이"
    def __init__ (self, name) :
        self.fullname = self.lastname + name
    def travel (self, where) :
        print("%s, %s 여행을 가다." %(self.fullname, where))
    def love (self, other) :
        print("%s, %s 사랑에 빠지다." %(self.fullname, other.fullname))
    def fight (self, other) :
        print("%s, %s 싸우다" %(self.fullname, other.fullname))
    def __add__ (self, other) :
        print("%s, %s 결혼하다" %(self.fullname, other.fullname))
    def __sub__ (self, other) :
        print("%s, %s 이혼하다" %(self.fullname, other.fullname))
        
class HouseSeong(HouseLee) :
    lastname = "성"
    def travel(self, where, day) :
        print("%s, %s 여행 %d일 가다" %(self.fullname, where, day))
        
mongryong = HouseLee("몽룡")
chunhyang = HouseSeong("춘향")
mongryong.travel("남원") 
chunhyang.travel("남원", 3)
mongryong.love(chunhyang)
mongryong + chunhyang
mongryong.fight(chunhyang)
mongryong - chunhyang
    
```

> 이몽룡, 남원 여행을 가다.
>
> 성춘향, 남원 여행 3일 가다
>
> 이몽룡, 성춘향 사랑에 빠지다
>
> 이몽룡, 성춘향 결혼하다
>
> 이몽룡, 성춘향 싸우다
>
> 이몽룡, 성춘향 이혼하다

- 클래스를 상속하려면 'class 클래스명 (상속 클래스명)' 의 형태로 선언해주면 된다.

  - ```python
    class HouseSeong(HouseLee) :
    ```

- 특정 인수를 추가로 받고 싶다면 같은 함수를 다르게 정의내리면 되는데, 이를 오버라이딩이라고 한다.

  - ```python
    class HouseLee :
        def travel (self, where) :
                print("%s, %s 여행을 가다." %(self.fullname, where))
                
    class HouseSeong(HouseLee) :
        def travel(self, where, day) :
            print("%s, %s 여행 %d일 가다" %(self.fullname, where, day))
    ```





