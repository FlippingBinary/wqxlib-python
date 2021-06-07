from .wqx_v3_0 import OrganizationAddress


class WQXOrganizationAddress(OrganizationAddress):
    def __init__(self,):
        OrganizationAddress.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add a rule test
