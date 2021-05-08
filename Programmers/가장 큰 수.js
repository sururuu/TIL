function solution(numbers) {
  var answer = '';
  numbers = numbers.map(num=>num.toString())
  answer = numbers.sort((a,b)=> (b+a)-(a+b)).join("")
  if (answer[0] == '0') {
      return '0'
  } 
  return answer;
}