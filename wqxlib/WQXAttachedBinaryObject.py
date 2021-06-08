from .wqx_v3_0 import AttachedBinaryObject


class WQXAttachedBinaryObject(AttachedBinaryObject):
    def __init__(self,):
        AttachedBinaryObject.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add a rule test
