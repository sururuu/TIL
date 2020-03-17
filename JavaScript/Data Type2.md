### 객체타입(object)

#### 1. Object 생성방법

> Object 생성자 함수

```javascript
var dog = new Object()
dog
// {}
dog.name ='back'
dog.age=5
dog
// {name:'back',age:5}
```



> 객체 리터럴

```javascript
var dog = {}
var dog2 = { name : 'bak',age : 3}
// dog2 
// { name : 'bak',age : 3}
// dog
// {}
```



```javascript
var person = {
    name : 'kim',
    greeting : function(){
        console.log('hi, ${this.name}')
    }
}
    
person.greeting()
// hi, kim
```



```javascript
var dog= {}
// undefined
dog.name = 'back'
// 'back'
console.log(dog)
// {name : back}
// undefined
```



```javascript
function Person(name){
    this.name = name;
    this.greeting = fucntion(){
        console.log('hi,${this.name}')
    };
}
// undefined
var p1= new Person('kim')
// undefined
p1.greeting()
// hi, kim
```



#### 2. Array 

##### 2.1 Array 생성

```javascript
var a = [1,2,'hi']
console.log(a)
// (3) [1,2,'hi']
var b = new Array()
b[0]=1
console.log(b)
//  [1]
typeof b
// 'object'
```

##### 2.2 배열 요소 접근

###### 2.2.1 인덱스를 이용하여 접근

```javascript
var fruits = ['banana','pear','mamgo'];
var myFavoritefruits = fruits[1];
console.log(myFavoritefruits);
// pear
```



###### 2.2.2 전체 배열에 접근

```javascript
var fruits = ['banana','pear','mamgo'];
document.getElementById('demo').innerHTML = fruits;
```



###### 2.2.3 인덱스 위치에 있는 요소 수정

```javascript
var fruits = ['banana','pear','mamgo'];
fruits[1]='melon';
console.log(fruits[1]);
// melon
```



##### 2.3 배열의 Method

###### 2.3.1 forEach() 

> 주어진 함수를 배열 요소 각각에 실행

```javascript
var array1 = ['a','b','c'];
array1.forEach(function(element){
	console.log(element);
})
// a,b,c
```



###### 2.3.2 indexOf()

> 배열 안 요소의 인덱스 찾기

```javascript
var fruits = ['banana','pear','mamgo'];
fruits.indexOf('pear')
// 1
```



###### 2.3.3 unshift()

> 배열의 앞에 요소 추가

```javascript
var arr = [];
arr.unshift(1);
arr.unshift(2);
console.log(arr);
// [2,1]
```



###### 2.3.4 push()

> 배열의 끝에 요소 추가

```javascript
var arr = [];
arr.push(1);
arr.push(2);
console.log(arr);
// [1,2]
```



###### 2.3.5 shift()

> 배열의 앞에 요소 제거

```javascript
var arr = [1,2,3];
arr.shift();
console.log(arr);
// [2,3]
```



###### 2.3.6 pop()

> 배열의 끝에 요소 제거

```javascript
var arr = [1,2,3];
arr.pop();
console.log(arr);
// [1,2]
```



###### 2.3.7 splice()

> 배열 조작

```javascript
var a= [1,2,3]
a.splice(1)
//[2,3]
console.log(a)
// [1]

var a=[1,2,3]
a.splice(1,2,'처음','두번')
console.log(a)
// [1, '처음','두번']
var a=[1,2,3]
a.splice(1,2,'처음')
a
// [1,'처음']
```



##### 2.3.8 slice

> 배열 자르기

```javascript
var a= [1,2,3]
a.slice(-2)
//[2,3]
a.slice(1,2)
//[2]
a.slice(1)
[2,3]
a.slice()
//[1,2,3]
```



#### 3 함수

> 함수 선언

```javascript
function add(n1,n2){
    return n1+n2;
}
```



```javascript
const sub = function(n1,n2){
    return n1-n2;
}
```

