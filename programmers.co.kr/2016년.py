import datetime as dt
from datetime import date

daylist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
def solution(a, b):
    c = dt.datetime(2016, a, b).weekday()
    answer = daylist[c]
    
    
    return answer