
def rocketEquation(num):
    totel = 0
    for i in num:
        totel += (i // 3) - 2
    print(totel)


def secondGo(n):
    totel = 0
    for i in range(0, len(n)):
        t = (n[i] // 3) - 2
        totel += t
        while t >= 9:
            t = (t // 3) - 2
            totel += t
    print(totel)
