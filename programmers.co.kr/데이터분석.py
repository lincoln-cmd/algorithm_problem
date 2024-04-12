def solution(data, ext, val_ext, sort_by):
    data_type = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3}
    
    data2 = [a for a in data if a[data_type[ext]] < val_ext]
    
    answer = sorted(data2, key = lambda x: x[data_type[sort_by]])
    
    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"


print(solution(data, ext, val_ext, sort_by))