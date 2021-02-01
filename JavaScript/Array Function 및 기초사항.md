### #1 FUNDAMENTALS

#### #1.1 Arrow Functions

```javascript
function sayHello(name = "human"){
    return "Hello" + name
}
const nicolas = sayHello("Nicolas");
// 화살표 함수
const sayHello2 = (name) => "Hello" + name;

console.log(nicolas)
```

> Arrow Function을 사용할 때는 const를 하고 Arrow Function 을 안에 넣어야 함, return을 한다는게 함축되어있음

- {} 괄호를 하면 그 안에 어디선가 return을 하겠다는 의미
- {} 중괄호를 하지 않는다면 return을 쓰지 않아도 함축적으로 return 됨

- args 안에 default 값을 줄 수 있음 ex) name = "human"

```javascript
const button = document.querySelector("button");
const handleClick = event => console.log(event);
// #1. 
button.addEventListener("click",handleClick);
// #2. 화살표 함수 적용
button.addEventListener("click", event => console.log(event))
```

- Argument가 하나라면 괄호()를 하지 않아도 됨 하지만 두 개 이상이라면 괄호가 필요



#### #1.2 Template Literals

```javascript
const sayHello = (name = "Human") => "Hello" + name;
// ``backticks 사용
const sayHello = (name = "Human") => `Hello ${name}`;
```



#### #1.3 Object Destructuring

```javascript
const human = {
	name: "Nico",
	lastName: "Serrano",
	nationality: "Wish i was korean",
    favFood: {
        breackfast: "Sang",
        lunch: "Doncas",
        dinner: "milk"
    }
}
// 비효율적인 코드
const name = human.name;
const lastName = human.lastName;
// 보다 나은 코드Structuring 
cosnt { name, lastName, nationality:difName, 
    favFood: { breackfast,lunch,dinner }  
      } = human;
// -> human이라는 object로 가서 name의 값을 새로운 variable인 name에 넣는다 
// -> nationality의 값을 새로운 variable인 difName 에 넣는다
// -> " : " 이후 값을 다른 이름을 넣으면 Variable의 이름을 바꿔 저장
// -> " : " 이후 중괄호를 넣으면 해당 object의 안으로 들어감 
console.log(name, lastName, difName, breackfast, lunch, dinner)
```



#### #1.4 Spread Operator

배열로부터 아이템을 가지고와서 Unpack함 ( Object도 동일하게 작동)

```javascript
const days = ["Mon", "Tues", "Wed"];
const otherDays = ["Ths", "Fri","Sat"];
// Array 가 아닌 String을 변환 됨.
const allDays = dyas + otherDays;
// Unpack
const allDays = [ ...days, ...otherDays, "Sun"];
```



#### #1.5 Classes

```javascript
class Human {
    constructor(name, lastName) {
        this.name = name;
        this.lastName = lastName
    }
}

class Baby extends Human {
    cry() {
        console.log("Waaa");
    }
}

const nico = new Human("Nico", "Serrano")
console.log(nico);
// Human {name:"Nico",lastName:"Serrano", constructor: Object}

const myBaby = new Baby("mini", "me");
console.log(myBaby);
// Baby {name:"mini",lastName:"me", constructor: Object}

```

/