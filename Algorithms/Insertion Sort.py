# n = input("Please type the length of the list: ")
# try:
#     n = int(n)
# except ValueError:
#     print("Please type a valid number!")
# a = []
# try:
#     for x in range(0, n):
#         y = int(input("Please type a number to be added to the list: "))
#         a.append(y)
# except ValueError:
#     print("Please type a valid number!")
# except TypeError:
#     print("Please type a valid number!")

def get_list_from_user():
    """Giving the user the ability to make his own list.
            n: length
        Returns:
            a: list of integers obtained from user input."""

    while True:
        try:
            n = int(input("Please type the length of the list: "))
            a = [int(input("Please type a number: ")) for _ in range(n)]
            return a
        except ValueError:
            print("Please type a valid number!")


def insertion_sort(a):
    """Sort a list in ascending order using the insertion sort algorithm.
             Args:
                 a: array/list to be sorted
             Returns:
                 The sorted list"""
    n = len(a)
    for x in range(1, n):
        y = x
        while y > 0 and a[y - 1] > a[y]:
            a[y - 1], a[y] = a[y], a[y - 1]
            y = y - 1
    return a


a = get_list_from_user()
print(insertion_sort(a))
