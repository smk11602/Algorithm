def solution(strArr):
    dictt = dict()
    for i in strArr :
        dictt[len(i)] = dictt.get(len(i),0) + 1 #get(키 값, 디폴트 반환값)
    return max(dictt.values())