def solution(nums):
    return min(len(nums)/2, len(set(nums)))
# len(set(nums)) 까지는 생각했는데, len(nums)/2 를 고려해야되는 게
# 만약 [1,2,3,4]라면 종류가 다르더라도 최대 2개밖에 가져갈 수 없기 때문