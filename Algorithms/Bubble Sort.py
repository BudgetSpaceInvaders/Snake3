a = [5, 7, 2, 4, 1, 9]
N = len(a)

for i in range(1, N):
    for j in range(0, N - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
# TO DO: WRITE THE PROGRAM IN A FUNCTION AND MAKE THE USER WRITE THE LIST BY INPUT AND NO EXCEPTIONS (TRY AND EXCEPT)
