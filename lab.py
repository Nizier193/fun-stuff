n, k, d = list(map(int, input().split()))

arr = [0 for i in range(d)]
day = 0
c_num = n

while day != d:
    c_num = str(c_num) + str(arr[day])

    if int(c_num) % k == 0:
        day += 1
        c_num = int(c_num)

    else:
        c_num = int(c_num[:-1])
        arr[day] += 1

        if arr[day] > 9:
            c_num = -1
            break

print(c_num)