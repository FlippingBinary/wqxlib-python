from yattag import Doc

from ..exceptions import WQXException
from .Organization import Organization


class WQX:
    """
    Main Schema used to transfer water monitoring results to EPA Office of Water.
    """

    __organization: Organization

    def __init__(self, o: dict = None, *, organization: Organization = None):
        if isinstance(o, WQX):
            # Assign attributes from object without typechecking
            self.__organization = o.organization
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.organization = o.get("organization")
        else:
            # Assign attributes from named keywords with typechecking
            self.organization = organization

    @property
    def organization(self) -> Organization:
        return self.__organization

    @organization.setter
    def organization(self, val: Organization) -> None:
        if val is not None and not isinstance(val, Organization):
            raise WQXException("Attribute 'organization' must be an Organization object.")
        self.__organization = None if val is None else Organization(val)

    def generateXML(self, name="WQX"):
        doc = Doc()
        asis = doc.asis
        tag = doc.tag

        with tag(
            name,
            ("xmlns", "http://www.exchangenetwork.net/schema/wqx/3"),
            ("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance"),
            (
                "xsi:schemaLocation",
                "http://www.exchangenetwork.net/schema/wqx/3 "
                "http://www.exchangenetwork.net/schema/wqx/3/index.xsd",
            ),
        ):
            if self.__organization is None:
                raise WQXException("Attribute 'organization' is required.")
            asis(self.__organization.generateXML("Organization"))

        return doc.getvalue()
