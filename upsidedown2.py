import copy, time

# include bad ones in case we get bad starting point 
progression = {'0': '1', '1':'6', '6': '8', '8': '9', '9': '0',
               '2': '6', '3': '6', '4': '6', '5': '6', '7': '8'}
swap180 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6',
           '2': 'x', '3': 'x', '4': 'x', '5': 'x', '7': 'x'}

def eq180(num):
    l = len(num) - 1
    if num[0] in ['0', '1', '8'] and num[0] != num[l]:
        return False
    if num[0] == '6' and num[l] != '9':
        return False
    if num[0] == '9' and num [l] != '6':
        return False
    rotatenum = [swap180[c] for c in num[::-1]]
    return (rotatenum == num)

def next_num(num, maxlen):
    return_num = num.copy()
    numlen = len(num)
    place = numlen - 1
    while place >= 0:
        return_num[place] = progression[return_num[place]]
        if return_num[place] == '0':
            if place == 0:
                if numlen < maxlen:
                    return_num.insert(0, '0')
                    numlen = numlen + 1
                else:
                    return '-1'
            else:
                place = place - 1
        else:
            break
    return return_num

def upsidedown(x, y):
    count = 0
    maxlen = len(str(y))
    testnum = list(str(x))
    while True:
        # print("checking:", testnum)
        if eq180(testnum):
            count = count + 1
            # print('count is now:', count)
        testnum = next_num(testnum, maxlen)
        if testnum == '-1' or int(''.join(testnum)) > y:
            break
    return count

if __name__ == '__main__':
    start = time.time()
    print(upsidedown(0,10))
    print(upsidedown(10, 100))
    print(upsidedown(100, 1000))
    print(upsidedown(1000, 10000))
    print(upsidedown(10000,15000))
    print(upsidedown(15000,20000))
    print(upsidedown(60000,70000))
    print(upsidedown(60000,130000))

    print(upsidedown(6, 25))
    print(upsidedown(10000, 1234567890))

    end = time.time()
    print("Time: ", end-start)

    