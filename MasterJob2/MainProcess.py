from MLPackage.MLModels import MLModels
from StandardPackage.Standards import standards
from DataSampling.DataSampling import datasampling


@standards("ACC")
@MLModels("SVM")
def sentifictest(*args, **kwargs):
    # 1. create data
    return datasampling(*args, **kwargs)


sentifictest(5, data_type=int, range_start=0, range_end=9)
