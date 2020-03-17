## Data Type

### 원시 타입

> 원시 타입의 값은 `변경 불가능한 값`(immutable value)이며 pass-by-value(값에 의한 전달)이다. 

#### 1. Number(숫자형)

1.1 변수 할당 및 연산

```javascript
var num = 1;
var num2 = num*2;
// console.log(num2); -> 2
var remainder1 = 30 %4;
// 2
var remainder2 = 100%5;
// 0
```



1.2 비교 및 같은 수 판별

```javascript
var result = 3>7;
// false
var result2 = 3>=1;
// true

// 일치연산자(===)
var one = 5;
var two = 5;
console.log(one ===two);
// true
```



1.3 유효하지 않는 숫자 연산

```javascript
var a=0;
var b=0;
var c=a/b;
console.log(c);
// NaN
```



1.4 무한대 표현

```javascript
var pInf = 10/0;
console.log(pInf);
// Infinity
var nInf = 10/-0;
console.log(nInf);
// -Infinity
```



#### 2. String (문자열)

2.1 문자열 더하기

```javascript
var s1 = 'some';
var s2 = 'thing';
var result = s1+s2;
console.log(result)
// 'something'
```



2.2 문자열 비교

```javascript
var s1= 'abc';
var s2 = 'abc';
var result = s2===s1;
console.log(result)
// true
var s3 = 'abc ';
var result2 = s1===s3;
console.log(result2)
//false 
//공백포함 해도 문자열에 포함하여 false출력
```



2.3 문자열 길이

> `.length`를 이용하여 길이 출력

```javascript
var str1 = '   '; // 공백 3칸
console.log(str1.length)
// 3
```



#### 3. Boolean(논리형)

> 0,-0,null,flase,NaN,undefined,빈 문자열("")은 `false`로 간주됨. 그 외 모든 다른 값은 초기값을 `true`로 설정

> ```javascript
> var t = true
> // 항상 이렇게 사용!
> var o = new Boolean(ture);
> //이렇게 쓰면 안됨./!
> ```



#### 4. null

> `null`은 의도적으로 변수에 값이 없다는 것을 명시할 떄 사용

> javascipr의 설계상의 오류 ; 

```javascript
var f = null;
console.log(typeof f);
// null이 아닌 object가 출력
```

> null 타입 확인하기

```javascript
var f = null;
console.log(typeof f ===null);
// false
console.log(f ===null);
//true
```



#### 5. undefined

> 어떤 변수를 만들고 그 값을 정의해주지 않을때 , `undefined` 반환

> null 과 undefined 차이

```javascript
// 변수를 생성, 값은 없음.
var k;
console.log(k);
// undefined
// 아무 값도 대입하지 않아도 undefined 출력

var o=undefined;
// 위 코드처럼 undefined를 명시적으로 대입해주는 코드는 사용x

```

```javascript
var obj= {
    name : 'kim'
};
obj=null
// obj를 더이상 사용하지 않을 계획이라 의도적으로 null을 표현.
```



### 객체 타입(Object type, Reference type)

> 객체는 데이터와 그 데이터에 관련된 동작을 모두 포함할 수 있는 개념적 존재.,
>
> Property와 Method를 포함 할 수 있는 독립적 주체

> 원시 타입을 제외한 나머지 (배열,함수 등)은 모두 객체이다. 

