function solution(a, b) {
    var answer = '';
    var daylist = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    
    var day = new Date('2016-' + String(a) + '-' + String(b)).getDay();
    answer = daylist[day];
    
    
    return answer;
}