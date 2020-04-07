def programAlarm(n):
    arr = [0 for k in range(0,100)]
    i = 0
    n[1] = 12
    n[2] = 2
    while n:
        firstVal = n[i + 1]
        secondVal = n[i + 2]
        thirdVal = n[i + 3]
        if n[i] > 2 or n[i] <= 0:
            print(n[0])
            break
        if n[i] == 1:
            total = n[firstVal] + n[secondVal]
        if n[i] == 2:
            total = n[firstVal] * n[secondVal]
        n[thirdVal] = total
        i += 4


def programAlarm2(n):
    for num1 in range(100):
        for num2 in range(100):
            arr = [x for x in n]
            arr[1] = num1
            arr[2] = num2
            i = 0
            while True:
                firstVal = arr[i + 1]
                secondVal = arr[i + 2]
                thirdVal = arr[i + 3]
                if arr[i] == 1:
                    arr[thirdVal] = arr[firstVal] + arr[secondVal]
                elif arr[i] == 2:
                    arr[thirdVal] = arr[firstVal] * arr[secondVal]
                else:
                    # print('n', n[0])
                    break
                i += 4
            if arr[0] == 19690720:
                print(num1, num2)



n = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0]
programAlarm2(n)















