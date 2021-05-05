function solution(numbers, target) {
  var answer = [0];
  for (var i=0; i<numbers.length; i++) {
      const temp = [];
      for (var j=0; j<answer.length; j++) {
          temp.push(answer[j] + numbers[i])
          temp.push(answer[j] - numbers[i])
      }
      answer = temp
  }
  let cnt 
= answer.filter(element => target === element).length;
  
  return cnt;
}