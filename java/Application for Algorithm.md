Application for Algorithm



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



## 자릿수의 합 구하기

- 기존에 자릿수의 합을 구하는 문제에서는 주어진 숫자가 두/세자리 수였기 때문에 10/100으로 나눈 값을 임의의 문자에 할당하여 일일이 더해주었다.
- 그러나 while 문을 이용하면 한번에 특정 숫자의 자릿수 합을 구할 수 있다는 것을 알게 되었다.

```java
while(temp!=0) {		
    sum += temp%10;
	temp /= 10;
}
```

- 간단한 수식이지만, num에 원하는 숫자를, sum에 0을 대입해두면 sum에 알아서 자릿수의 합이 차곡차곡 쌓인다.
- 나머지 정리를 이용한 방법으로, 수행 방식은 다음과 같다.
  1. temp를 10으로 나눈 나머지는 temp의 일의 자리 수이다.
  2. 이를 sum에 더해서 저장한다.
  3. temp를 10으로 나눈 값을 자기 자신에게 재할당한다.
  4. 이때 temp는 일의 자리 수가 지워진 값으로 저장된다.
- 이렇게 일의 자릿수부터 지워나가며 sum에 더하면 최종적으로 0이 되어 while문을 벗어난다.



## 리스트의 특정 값 지우기

- list.remove() 함수의 인자에는 두 가지가 들어갈 수 있다.
- 보통 우리가 사용하는 int 인자를 대입할 경우, list의 n번 인덱스의 값을 제거하게 된다.
- 그러나 이 경우에는 num라는 구체적인 값에 대응하는 원소를 지워야 한다는 점과, 지워나갈 때마다 list의 인덱스 역시 변화한다는 점을 고려해야 한다.

```java
list.remove((Integer) num);
```

- 이때 인자 앞에 **(Integer)**를 적어서 명시적 형변환을 해주면 우리가 원하는 대로 해당 값과 일치하는 원소를 지우게 된다.



## 배열의 초기 변수값 지정하기

```java
int[] array = new int[n]
```

- 다음은 정수 타입을 저장하는 n개의 원소를 지니는 배열의 생성문이다.
- 다음과 같이 배열을 생성했을 경우, 배열 안에 n개의 주소값이 부여되지만, 그 값은 아직 0인 상태이다.
- 이 때 일률적으로 배열값을 0이 아닌 다른 값으로 부여하고 싶다면 Arrays 클래스의 fill 함수를 사용한다.

```java
Arrays.fill(array, 1)
```

- 그러면 int의 모든 주소값에 1이라는 값이 부여된다.



## 최대공약수, 최소공배수 구하기

- 유클리드 호제법이란 두 자연수의 최대공약수를 구하는 알고리즘이다.

```java
	public static int lcm (int M, int N) {
		int big=M, small=N, r=1;
		if(M < N) {
			big = N;
			small = M;
		}
        
        // 유클리드 호제법
		while (r>0){
			r =  big % small;
			big = small;
			small = r;
		}
        
		return M*N/big;
	}
```

- 먼저 두 자연수 M과 N에 대하여, 큰수와 작은수를 판별해준다.
- 이후 r에 아무 값이나 부여한 뒤에, while문을 이용하여 계속해서 나누어줄 것이다.
- 최초 r에 큰수를 작은수로 나눈 몫을 부여하는데, 이때 이 r이 0이 되는 시점이 두 수가 나누어 떨어질 때이다.
- 이후 큰 수에 작은 수를, 작은 수에 r을 대입한 후 loop로 돌린다.
- while 문이 종료되었을 때 big에 저장된 값이 최대공약수가 된다.
- 최소공배수는 원래 두 수의 곱에 최대공약수를 나누면 된다.

>M=12, N=15일 때
>
>| r         | big            | small                     |
>| --------- | -------------- | ------------------------- |
>| 최초 시행 | 15             | 12                        |
>| 3         | 12             | 3                         |
>| 0         | 3              | 0                         |
>| break     | 최대공약수 : 3 | 최소공배수 : 15*12/3 = 60 |



## ArrayList의 sort() 메소드 사용하기

### Comparator 인터페이스

- Comparator 인터페이스를 이용하기 위해서는 compare() 메소드를 오버라이딩 해야 한다.
- compare() 메소드는 두 개의 인자를 받아 비교하고, 정수 값을 반환한다.
- 두 값이 같다면 0을, 전자가 크다면 양수를, 후자가 크다면 음수를 리턴한다.

```java
// Comparator 오버라이딩
class Ascending implements Comparator<Integer> {
    @Override
    public int compare(Integer o1, Integer o2) {
        return o1.compareTo(o2);
    }
}
```

- 위 코드에서 compare 메소드는 정수 2개를 인수로 받아 두 값을 비교한다.
- 이렇게 Comparator의 compare() 함수를 오버라이딩한 Ascending 객체는 Collections.sort()함수의 두 번째 인수로 들어가게 된다.
- o1과 o2를 비교했을 때 o1이 작다면 -1이 반환된다. 짐작컨대 음수일 경우 o1과 o2를 그대로 두고, 양수일 경우 두 수의 자리를 바꾸는 식으로 동작하는 것 같다.



### Collections의 sort() 함수

- sort() 함수는 두 가지 방법으로 사용할 수 있다.

```java
public static <T> void sort(List<T> list, Comparator<? super T> c)
public static <T extends Comparable<? super T>> void sort(List<T> list)
```

- 두 가지 모두 T를 제네릭 타입으로 받는 List 타입을 인수로 받으며, Comparator T를 상속하는 Comparator 인자를 추가로 부여할 수 있다.
- 여기서 T 타입이란, Comparable 인터페이스를 오버라이딩한 객체여야 한다.
- 사실 Comparator라는 별도의 변수를 넘겨주지 않는다 해도 기본적으로 List타입의 객체라면 얼마든지 위 함수를 사용할 수가 있다.
- 왜냐하면 String, Integer 같은 클래스가 이미 Comparable 인터페이스를 상속(기본 오름차순)하고 있기 때문이다.
- 그런데 Comparator 타입 인자를 부여하면 이것을 내림차순으로 바꿀 수가 있다.



```java
// Comparator 오버라이딩
class Descending implements Comparator<Integer> {
    @Override
    public int compare(Integer o1, Integer o2) {
        return o2.compareTo(o1);
    }
}
```

- 즉, Comparator를 상속한 객체는 sort() 메소드에게 정렬 기준을 제시해준다.
- 위의 내용은 앞서 만든 Ascending 클래스와 리턴 부분에서의 o1, o2 순서만 다르다.
- 음수값이 리턴되는 경우가 그대로 두는 경우라면, o2가 o1보다 작을 때 그대로 두는 것이므로 왼쪽에 더 큰 수가 자리하게 된다.



### 다양한 객체의 정렬

- 추가로, 만약 넘겨주고 싶은 객체가 String, Integer 등의 타입이 아니라 하더라도 얼마든지 get/set 메소드를 통해 인수를 전달해줄 수 있고, 원하는 기준으로 오버라이딩하여 정렬하는 것이 가능하다.

```java
public class Student implements Comparable<Student>{
       private int mAge;
       private String mName;
       
       public Student(int age, String name) {
              mAge = age;
              mName = name;
       }
       
       public int getAge() { return mAge; }
       
       public String getName() { return mName;  }
       
       public String toString() {
              return "age : " + mAge + " / name : " + mName;
       }

       @Override
       public int compareTo(Student arg0) {
              // TODO Auto-generated method stub
              int targetAge = arg0.getAge();
              if(mAge == targetAge) return 0;
              else if(mAge > targetAge) return 1;
              else return -1;
       }
}

// 출처: https://manorgass.tistory.com/60 [생각하는 개발자]
```

- 위 코드는 Student라는 객체를 정의하고 있는 클래스에 Comparable 인터페이스를 상속함으로써 compareTo 메소드를 수정하고 있는 모습이다.
- 앞서 compare 메소드를 수정하였지만, 이런 식으로 직접적으로 비교하는 방식 자체를 재정의할 수도 있는 듯하다.
- 위의 compareTo 메소드는 인수로 전달받은 Student 객체에서 자기 자신(o1-mAge)과 비교 대상(o2-targetAge)의 나이를 비교한 후, 자신의 나이가 나이가 많다면 1을 리턴하게 하여 오름차순으로 정렬하게끔 만들고 있다.
- 이와 같이 비교하는 대상에 대하여 오버라이딩을 통해 구현해준다면 Comparator.naturalOrder()이나 Comparator.reverseOrder()과 같은 메소드를 통해서도 정렬이 가능해진다.



## MergeSort

- 리스트 객체를 정렬하는 한가지 방법으로, 재귀호출을 통해 리스트를 계속해서 반으로 쪼갠 다음, 그렇게 반으로 나뉜 좌/우의 리스트 원소 값들을 각각 비교하여 작은 값을 먼저 카피하여 반환한다.
- 이를 위해 필요로 하는 인자는 다음과 같다.

> int[] arr : 우리가 정렬하고자 하는 배열
>
> int[] tmp : 이를 복사하여 임시적으로 저장하기 위한 배열
>
> int start : 왼쪽 배열의 시작 인덱스 값
>
> int mid : 오른쪽 배열의 시작 인덱스 값
>
> int end : 오른쪽 배열의 끝 인덱스 값



### 활용 의의

- MergeSort의 이점은 무엇보다도 속도이다.
- 얼핏 보았을 때는 재귀호출이라는 형태와, 배열을 계속 복사해나가는 구조 때문에 비효율적이라고 생각할  수 있으나, 배열이 커지면 커질수록 원소의 개수를 일일이 비교하여 정렬하는 방식보다 반으로 쪼개어 나누는 방식이 더 효율적일 수밖에 없다.
- MergeSort의 예상 응답시간은 O(n*logn)이라고 한다.



### 구현 과정

1. 먼저 정렬하고자 하는 배열을 인수로 받는 mergeSort(int[] arr)을 호출한다.
2. 이 함수는 `본래의 배열(int[] arr)`, `임시 배열(int[] tmp)`, `배열의 시작(기본 0)`, `배열의 끝(arr.length-1)`을 인수로 넘겨주면서 오버로딩된 함수를 호출한다.
3. 일종의 break문으로써 if(start>=end) return 을 사용하거나, if(start<end) 이후에 구현부를 작성한다.
4. 오버로딩 함수에서는 본격적으로 배열을 반으로 쪼개어(위의 시작, 끝 인덱스를 조정하면 된다) 자기 자신을 호출한다.
5. 이렇게 쪼개어진 배열을 합치기 위한 merge 함수를 구현한다.
6. merge에서는 tmp에 arr을 복사한다.
7. 이후 우리가 임의로 쪼갠 좌우의 배열 원소값을 while을 이용하여 비교한 후, 작은 쪽부터 다시 arr에 담는다.
8. 만약 복사를 마친 뒤에 왼쪽 배열에 값이 남아있다면(원래 값은 가운데 위치했다는 뜻이므로) for문을 이용하여 마저 복사해준다.
9. 만약 우측 배열에 값이 남아있다면(원래 값이 끝에 위치했다는 뜻이므로) 다시 복사해줄 필요가 없으므로 병합을 마친다.



### 결과물

```java
package practice;

public class MergeSortTest {
	
	private static void mergeSort(int[] arr) {
		int[] tmp = new int[arr.length];
		mergeSort(arr, tmp, 0, arr.length-1);
	}
	
	private static void mergeSort(int[] arr, int[] tmp, int start, int end) {
		if(start < end) {
			int mid = (start+end)/2;
			mergeSort(arr, tmp, start, mid);
			mergeSort(arr, tmp, mid+1, end);
			merge(arr, tmp, start, mid, end);
		}
	}
	
	private static void merge(int[] arr, int[] tmp, int start, int mid, int end) {
		for(int i=start; i<= end; i++) {
			tmp[i] = arr[i];
		}
		int part1 = start;
		int part2 = mid+1;
		int index = start;
		while (part1 <= mid && part2 <= end) {
			if(tmp[part1] <= tmp[part2]) {
				arr[index] = tmp[part1];
				part1++;
			} else {
				arr[index] = tmp[part2];
				part2++;
			}
			index++;
		}
		for (int i = 0; i <= mid-part1; i++) {
			arr[index+i] = tmp[part1+i];
		}
	}
	
	private static void printArray(int[] arr) {
		for(int data : arr) {
			System.out.print(data + ", ");
		}
		System.out.println();
	}
	
	
	public static void main(String[] args) {
		int[] arr = {3,9,4,7,5,0,1,6,8,2};
		printArray(arr);
		mergeSort(arr);
		printArray(arr);
	}
}

// 참고 : https://www.youtube.com/watch?v=QAyl79dCO_k
```

