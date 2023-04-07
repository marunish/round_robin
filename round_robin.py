members = int(input("number of member: "))
print(members)

n = members
w = 1
x = [i for i in range(1, n, 2)]
y = [i for i in range(2, n+1, 2)]

print(x)
print(y)

print("Week {}".format(w))

for i in range(len(x)):
    print("{}-{}".format(x[i], y[i]))

for w in range(2, n+1):
    print("Week {}".format(w))

    x.append(y[-1])
    y.insert(0, x[1])
    x.pop(1)
    y.pop()

    print(x)
    print(y)

    for i in range(len(x)):
        print("{}-{}".format(x[i], y[i]))

print("Week {}".format(w+1))
print("{}-{}".format(x[0], y[0]))
