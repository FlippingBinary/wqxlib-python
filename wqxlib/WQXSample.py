from .wqx_v3_0 import ReferenceMethod, SampleDescription


class WQXSample(SampleDescription, ReferenceMethod):
    from . import WQXActivity

    __activity: WQXActivity  # parent activity

    def __init__(
        self, *, activity: WQXActivity = None,
    ):
        self.__activity = activity
        ReferenceMethod.__init__(self)
        SampleDescription.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add a rule test
