import random
import string

def dataSampling(**kwargs):
    res = []
    for key, value in kwargs.items():
        if key == 'int':
            res.append(random.sample(range(1, 101), value))
        elif key == 'float':
            res.append([round(random.uniform(0, 100), 2) for _ in range(value)])
        elif key == 'str':
            res.append([''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(value)])
    return tuple(res)


# 生成10个整数
print(dataSampling(int=10))

# 生成5个浮点数
print(dataSampling(float=5))

# 生成3个字符串
print(dataSampling(str=3))

# 生成2个整数、4个浮点数、3个字符串
print(dataSampling(int=2, float=4, str=3))
