from math import *

def func1(x, y, a):
    return floor(((sqrt(8+abs(x-y)**3)**1/3) / (sqrt((x**2) + (y**2) + 1.25))) + (0.05 * a) + log(4, 5))


def func2(x):
    return floor(exp(2 * x) * pow(1+pow(cos(x), 3), 2) + tan(13))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(func1(3, 5, 3))
    print(func2(4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
