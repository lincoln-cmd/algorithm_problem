function solution(numbers) {
    var answer = 0;
    
    for (var i = 0; i < 10; i ++){
        if (!numbers.includes(i)){
            answer += i;
        } // 배열 numbers가 i를 포함하고 있지 않으면 answer에 더해줌
    }
    
    return answer;
}