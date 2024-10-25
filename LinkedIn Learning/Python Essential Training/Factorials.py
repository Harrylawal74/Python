def factorial(num):
    answer = num
    if type(num) != int:
        return None

    if num > 0 and type(num) != float:
       for i in range(1, num):
        answer = answer * (num-i)

    elif num == 0:
        return 1
        
    else:
        return  None

    return answer
