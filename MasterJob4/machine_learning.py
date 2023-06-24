import random


def machineLearningDecorator(*args):
    def decorator(func):
        def wrapper(**kwargs):
            result = func(**kwargs)

            # 执行机器学习方法
            for method in args:
                print(f"Applying {method} machine learning method...")
                # 这里假设执行机器学习方法的代码

            # 执行精度指标操作
            for metric in ['ACC', 'MCC', 'F1', 'RECALL']:
                if metric in args:
                    print(f"Calculating {metric} accuracy...")
                    # 这里假设执行精度指标操作的代码

            return result

        return wrapper

    return decorator


@machineLearningDecorator('SVM', 'RF', 'ACC', 'F1')
def dataSampling(**kwargs):
    result = []

    for data_type, data_range in kwargs.items():
        if data_type == 'int':
            result.append(random.randint(*data_range))
        elif data_type == 'float':
            result.append(random.uniform(*data_range))
        elif data_type == 'str':
            result.append(''.join(random.choices(data_range, k=random.randint(1, 10))))

    return result


# 调用示例
data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='abcdefghijklmnopqrstuvwxyz')
print(data)
