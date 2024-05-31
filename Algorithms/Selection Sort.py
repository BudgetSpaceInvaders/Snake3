n = input("Please type the length of the list: ")
# Deciding the length of the list
try:
    n = int(n)
except ValueError:
    print("Please type a valid number!")
list1 = []
try:
    # Making the list
    for x in range(0, n):
        y = int(input("Please type a number to be added to the list: "))
        list1.append(y)
except ValueError:
    print("Please type a valid number!")
except TypeError:
    print("Please type a valid number!")


def selection_sort(list1):
    """Sort a list in ascending order using the selection sort algorithm.
             Args:
                 list1: array/list to be sorted
             Returns:
                 The sorted list"""
    for x in range(0, n - 1):
        min = x
        for i in range(x + 1, n):
            if list1[i] < list1[min]:
                min = i
        if min != x:
            list1[x], list1[i] = list1[i], list1[x]
    return list1


print(selection_sort(list1))
