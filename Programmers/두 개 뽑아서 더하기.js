function solution(numbers) {
  var answer = [];
  var l = numbers.length;
  for (var i=0; i<l-1; i++) {
      for (var j=i+1; j<l; j++) {
          answer.push(Math.abs(numbers[i]+numbers[j]));
      }
      const set = Array.from(new Set(answer));
      answer = set;
  }

  
  answer.sort(function (a,b){ 
      return a-b; });

  return answer;
}