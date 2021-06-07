from .wqx_v3_0 import Telephonic


class WQXTelephonic(Telephonic):
    def __init__(self,):
        Telephonic.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # TODO: add a rule test
