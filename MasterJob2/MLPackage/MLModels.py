# from sklearn.svm import svc
import random


class MLModels(object):

    def __init__(self, *args):
        self._model = args

    def __call__(self, func):
        # 1. receive data: where the data come from
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = list()
            # 2. call model: according to the parameters
            for model in self._model:
                if model == "SVM":
                    result = self.SVM()
                elif model == "RF":
                    result = self.RF(data)
                elif model == "CNN":
                    result = self.CNN(data)
                else:
                    result = self.RNN(data)
                results.append(result)
            # 3. return result
            data2 = list()
            data2.append(data)
            data2.append(results)
            print(data2)
            return data2
        return wrapper


    def SVM(self):
        result = random.randint(0, 1)
        return result

    def RF(self, data):
        results = list()
        for i in range(len(data[0])):
            col_data = [row[i] for row in data]
            unique_values = set(col_data)
            num_unique_values = len(unique_values)
            if None in unique_values:
                num_unique_values -= 1
            results.append(num_unique_values)
        return results

    def CNN(self, data):
        results = list()
        for i in range(len(data[0])):
            col_data = [row[i] for row in data]
            num_non_missing = sum(1 for val in col_data if val is not None)
            if num_non_missing < 2:
                results.append(None)
            else:
                sorted_vals = sorted(col_data)
                min_diff = float('inf')
                for j in range(1, len(sorted_vals)):
                    diff = sorted_vals[j] - sorted_vals[j - 1]
                    if diff < min_diff:
                        min_diff = diff
                cnn = min_diff / (max(col_data) - min(col_data))
                results.append(cnn)
        return results

    def RNN(self, data):
        results = list()
        for i in range(len(data[0])):
            col_data = [row[i] for row in data]
            num_non_missing = sum(1 for val in col_data if val is not None)
            if num_non_missing < 2:
                results.append(None)
            else:
                sorted_vals = sorted(col_data)
                max_diff = -float('inf')
                for j in range(1, len(sorted_vals)):
                    diff = sorted_vals[j] - sorted_vals[j - 1]
                    if diff > max_diff:
                        max_diff = diff
                rnn = max_diff / (max(col_data) - min(col_data))
                results.append(rnn)
        return results
