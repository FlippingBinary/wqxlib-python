from .wqx_v3_0 import ElectronicAddress


class WQXElectronicAddress(ElectronicAddress):
    def __init__(self,):
        ElectronicAddress.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add a rule test
