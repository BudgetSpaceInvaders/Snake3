N = input("Please type the length of the list: ")
try:
    N = int(N)
except ValueError:
    print("Please type a valid number!")
a = []
try:
    for x in range(0, N):
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
        for i in range(1, N):
            for j in range(0, N - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        return list1
    except TypeError:
        print("Please type a valid number!")
    except ValueError:
        print("Please type a valid number!")


print(bubble_sort(a))
