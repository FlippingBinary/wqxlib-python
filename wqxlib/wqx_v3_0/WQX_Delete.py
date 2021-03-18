from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .Organization_Delete import OrganizationDelete


class WQXDelete:
    """
    Main Schema used to delete a portion of water monitoring results from EPA Office of
    Water system.
    """

    __organizationDelete: List[OrganizationDelete]

    def __init__(
        self, o: dict = None, *, organizationDelete: List[OrganizationDelete] = None
    ):
        if isinstance(o, WQXDelete):
            # Assign attributes from object without typechecking
            self.__organizationDelete = o.organizationDelete
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.organizationDelete = o.get("organizationDelete")
        else:
            # Assign attributes from named keywords with typechecking
            self.organizationDelete = organizationDelete

    @property
    def organizationDelete(self) -> List[OrganizationDelete]:
        return self.__organizationDelete

    @organizationDelete.setter
    def organizationDelete(
        self, val: Union[OrganizationDelete, List[OrganizationDelete]]
    ) -> None:
        if val is None:
            self.__organizationDelete = []
        elif isinstance(val, list):
            r: List[OrganizationDelete] = []
            for x in val:
                r.append(OrganizationDelete(x))
            self.__organizationDelete = r
        else:
            self.__organizationDelete = [OrganizationDelete(val)]

    def generateXML(self, name="WQXDelete"):
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
            if self.__organizationDelete is None:
                raise WQXException("Attribute 'organizationDelete' is required.")
            for x in self.__organizationDelete:
                asis(x.generateXML("OrganizationDelete"))

        return doc.getvalue()
