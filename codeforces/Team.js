var n = readline();
var cnt = 0;
 
for (var i = 0; i < n; i++){
    var arr = readline().split(" ");
    var sum = 0;
    for (var j = 0; j < arr.length; j++){
        if(arr[j] === '1'){
            sum++;
        }
    }
    if (sum >= 2){
        cnt += 1;
    }
}
 
print(cnt);