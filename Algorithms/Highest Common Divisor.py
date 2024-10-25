def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    try:
        a = int(input("Please enter a number: "))
        b = int(input("Please enter another number: "))
        r = gcd(a, b)
        print(f"The greatest common divisor of {a} and {b} is {r}")
    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    main()
