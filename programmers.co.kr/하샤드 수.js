function solution(x) {
    var answer = true;
    
    var a = String(x);
    var b = 0;
    for (var i = 0; i < a.length; i++){
        b += Number(a[i]);
    }
    
    if (x % b === 0){
        return answer;
    }else{
        return false;
    }
}