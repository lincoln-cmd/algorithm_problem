var n = readline();

for (var w = 0; w < n; w++){
    var word = readline();

    if (word.length > 10){
        var long = word.length - 2;
        print(word[0] + String(long) + word[word.length - 1]);
    }else{
        print(word);
    }
}