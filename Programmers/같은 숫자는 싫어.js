function solution(arr)
{
    var answer = [];

    var i = 0;
    while(i != arr.length) {
        if (arr[i] == arr[i+1]) {
            i+=1
        }else if (arr[i] != arr[i+1]){
            answer.push(arr[i])
            i+=1
        }
    }
    return answer;
}