def square_digits(num):
    sq_list_num = [str(int(a) ** 2) for a in str(num)]
    return int(''.join(sq_list_num))

print(square_digits(9119))
print(square_digits(0))
