def mysum(a):
    result = 0
    for i in range (1, a+1):
        result += i
    return result

def gugu(a):
    for i in range(1, 10):
        print('{} x {} = {}'.format(a, i, a*i))

if __name__ == "__main__":
    mysum(100)