#pattern 1
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
print()
#pattern 2
for i in range(1,6):
    for j in range(1,7-i):
        print(j, end=' ')
    print()
print()
#pattern 3
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=' ')
    print()
print()
#pattern 4
for i in range(1,6):
    for j in range(1,7-i):
        print("*", end=' ')
    print()
print()
#pattern 5
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=' ')
    print()
print()
#pattern 6
for i in range(69,64,-1):
    for j in range(65,i+1):
        print(chr(j), end=" ")
    print()
print()
#pattern 7
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=' ')
    print()
print()
#pattern 8
for i in range(1,6):
    for j in range(1,7-i):
        print(i, end=' ')
    print()
print()
#pattern 9
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i), end=' ')
    print()
print()
#pattern 10
for i in range(69,64,-1):
    for j in range(65,i+1):
        print(chr(i), end=" ")
    print()