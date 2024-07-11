from datetime import datetime

def solution(date1, date2):
    date01 = datetime(date1[0], date1[1], date1[2])
    date02 = datetime(date2[0], date2[1], date2[2])
    
    return 1 if date01 < date02 else 0