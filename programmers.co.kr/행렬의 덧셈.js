function solution(arr1, arr2) {
    var answer = [];
    
    for (var i = 0; i < arr1.length; i++){
        var a = arr1[i];
        var b = arr2[i];
        let c = new Array();
        for (var j = 0; j < a.length; j++){
            var d = a[j] + b[j];
            c.push(d);
        }
        answer.push(c);
    }
    return answer;
}