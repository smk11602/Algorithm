def solution(numbers):
    sum = 0
    for num in numbers:
        sum += num
    
    average = sum / len(numbers)
    return average
