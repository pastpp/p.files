q = [float(input("первое число: ")),input("действие: "), float(input("второе число: "))]
if q[1] == '+':
    x = q[0] + q[2]
    print(x)
elif q[1] == '-':
    x = q[0] - q[2]
    print(x)
elif q[1] == '*':
    x = q[0] * q[2]
    print(x)
elif q[1] == '/':
    x = q[0] / q[2]
    print(x)
elif q[1] == '%':
    x = q[0] % q[2]
    print(x)
elif q[1] == '**':
    x = q[0] ** q[2]
    print(x)
else:
    print('ошибка')