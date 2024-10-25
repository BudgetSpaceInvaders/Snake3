"""int_array = [1, 5, 8, 9, 45, 12, 15]
char_array = ["s", "e", "i", "o", "u"]
float_array = [4.2, 4.5, 4.6, 4.7, 4.8]
bool_array = [True, False, False, True, True]

print("Length ", len(int_array), int_array)
print(len(char_array))
print(len(float_array))
print(len(bool_array))

print(int_array)

for i in range(0, len(char_array)):
    print(char_array[i], end=" ")

for i in float_array:
    print(i, end=" ")
print()

test = []
l = int(input("Lungimea listei: "))
for i in range(0, l):
    test.append(int(input("Enter element with index " + str(i) + ": ")))
print("Lungimea listei: ", len(test))
"""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1)

list1.append(45)
print(list1)

list1.clear()
print(list1)
list1 = [1, 2, 3, 4, 5]
print(list1.copy())
list1.extend(list2)
print(list1)
print(list1.index(6))
list1.insert(2, 9)
print(list1)
print(list1.pop(3))
list1.remove(9)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.append(9)
print(list1)
print(list1.count(9))
print(sum(list1))
