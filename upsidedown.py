def solve(a, b):
    translation = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    nogood = set(['2', '3', '4', '5', '7'])
    count = 0
    for test in range(a, b):
        stest = str(test)
        # print('testing:', stest)
        if set(stest) & nogood:
            # print('skipped')
            continue
        sconvert = (''.join([translation[letter] for letter in stest]))[::-1]
        if stest == sconvert:
            count += 1
        # print('count:', count)
    return count

if __name__ == '__main__':
    print(solve(0,10))
    print(solve(10,100))
    print(solve(100, 1000))
    print(solve(1000, 10000))
    print(solve(10000, 100000))
    print(solve(100000, 1000000))
    print(solve(1000000, 10000000))
    # print(solve(15000, 20000))
    # print(solve(60000, 70000))
    # print(solve(60000, 130000))