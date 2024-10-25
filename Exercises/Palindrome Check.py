palin = input("Please enter a word: ")
palin = palin.lower()


def pal_check(pal):
    if pal[0] != pal[-1]:
        return False
    elif len(pal) <= 1:
        return True
    else:
        return pal_check(pal[1:-1])


if pal_check(palin):
    print(f"{palin.capitalize()} is a palindrome!")
else:
    print(f"{palin.capitalize()} is not a palindrome!")

print(pal_check(palin))
