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


def mergesort(a):
    """Make small lists.
            n: length of the list
        Returns:
            The merged list
            """
    n = len(a)
    mid = n // 2
    if n <= 1:
        return a

    left = a[:mid]
    right = a[mid:]

    ar1 = mergesort(left)
    ar2 = mergesort(right)

    return merge(ar1, ar2)


def merge(ar1, ar2):
    """Sorting the small lists and uniting them into a bigger one.
                ar1 and ar2: the small lists that will be united
            Returns:
                ar3: the final result"""
    ar3 = []
    while ar1 and ar2:
        if ar1[0] <= ar2[0]:
            ar3.append(ar1.pop(0))
        else:
            ar3.append(ar2.pop(0))
    ar3.extend(ar1 or ar2)
    return ar3
    # while len(ar1) != 0 and len(ar2) != 0:
    #     if ar1[0] > ar2[0]:
    #         ar3.append(ar2[0])
    #         ar2.remove(ar2[0])
    #     else:
    #         ar3.append(ar1[0])
    #         ar1.remove(ar1[0])
    #
    # while len(ar1) > 0:
    #     ar3.append(ar1[0])
    #     ar1.remove(ar1[0])
    #
    # while len(ar2) > 0:
    #     ar3.append(ar2[0])
    #     ar2.remove(ar2[0])
    #
    # return ar3


print(mergesort(get_list_from_user()))
