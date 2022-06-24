var input = readline().split(' ');
var n = input[0], k = input[1];
var cnt = 0;

var arr = readline().split(' ');

for (var i = 0; i < n; i++){
    if (parseInt(arr[i], 10) >= parseInt(arr[k - 1], 10) && parseInt(arr[i], 10) > 0){
        cnt++;
    }
}

print(cnt);