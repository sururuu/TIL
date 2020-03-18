## 호이스팅(Hoisting)

> 변수의 정의가 그 범위에 따라 `선언과 할당`으로 분리되는 것

> 코드에 선언된 변수 및 함수를 코드 상단으로 끌어올리는 것

- 함수 내에서 선언한 함수 범위의 변수는, 해당 함수의 최상위로
- 함수 밖에서 선언한 전역범위의 전역 변수는 스크립트 단위의 최상위로 끌어 올려진다.

```javascript
console.log(a)
// Reference Error
```

```javascript
console.log(a);
// undefined
var a = 1;
console.log(a);
// 1
// hoisting 되어 오류가 아닌 undefined
```

```javascript
//hoisting 된 실제 실행 과정
var a;
consol.log(a);
// undefined
a=1;
console.log(a);
// 1
```

