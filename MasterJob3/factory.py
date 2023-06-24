from CNN import CNN
from RF import RF
from RNN import RNN
from SVM import SVM


class FactoryML(object):
    def __init__(self, *args):
        self._model = args

    def connection_factory(self, *args):
        result = list()
        for model in self._model:
            if model == "SVM":
                connector = SVM()
                result.append(connector)
            elif model == "CNN":
                connector = CNN()
                result.append(connector)
            elif model == "RF":
                connector = RF()
                result.append(connector)
            elif model == "RNN":
                connector = RNN()
                result.append(connector)
            else:
                raise ValueError('Cannot connect to {}'.format(*args))
            return result


