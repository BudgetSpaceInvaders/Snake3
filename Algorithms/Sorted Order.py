global list1
global cntr
list1 = []
cntr = 0


def sort_order(list1, cntr):
    try:
        crntnr = int(input("Please type a new number: "))
        while crntnr != 0:
            list1.append(crntnr)
            cntr += 1
            crntnr = int(input("Please type a new number: "))
        else:
            list1 = sorted(list1)
            for x in range(0, cntr):
                print(list1[x])
    except ValueError:
        print("Please enter a number!")
        sort_order(list1, cntr)


sort_order(list1, cntr)
