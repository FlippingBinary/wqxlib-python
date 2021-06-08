from .wqx_v3_0 import ReferenceMethod, SampleDescription


class WQXSample(SampleDescription, ReferenceMethod):
    def __init__(self):
        ReferenceMethod.__init__(self)
        SampleDescription.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add a rule test
