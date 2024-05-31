n = input("Please type the length of the list: ")
try:
    n = int(n)
except ValueError:
    print("Please type a valid number!")
a = []
try:
    for x in range(0, n):
        y = int(input("Please type a number to be added to the list: "))
        a.append(y)
except ValueError:
    print("Please type a valid number!")
except TypeError:
    print("Please type a valid number!")


def bubble_sort(list1):
    """Sort a list in ascending order using the bubble sort algorithm.
    Args:
        list1: array/list to be sorted
    Returns:
        The sorted list
    """
    try:
        m = len(a)
        for i in range(1, m):
            for j in range(0, m - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        return list1
    except TypeError:
        print("Please type a valid number!")
    except ValueError:
        print("Please type a valid number!")


print(bubble_sort(a))
