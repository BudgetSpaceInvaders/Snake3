def fibonacci(n):
    num1 = 1
    num2 = 1
    list1 = [1, 1]
    if n < 1:
        return 1
    else:
        while num2 < n or num1 < n:
            num1 = num1 + num2
            list1.append(num1)
            num2 = num1 + num2
            list1.append(num2)
        if list1[-1] > n:
            list1 = list1.remove(list1[-1])
        if list1[-1] > n:
            list1 = list1.remove(list1[-1])
    return list1


print(fibonacci(13))
