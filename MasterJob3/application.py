import factory

fac = factory()
models = fac.connection_factory("SVM", "RNN")
for model in models:
    model.prediction()

