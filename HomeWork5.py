def same_by(func, val):
    return len(set(map(func, val))) == 1 if val else True

values1 = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values1):
    print('same')
else:
    print('different')

values2 = [1, 2, 3, 4]

if same_by(lambda x: x % 2, values2):
    print('same')
else:
    print('different')
