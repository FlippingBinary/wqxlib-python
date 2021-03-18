from enum import Enum

from yattag import Doc

from .exceptions import WQXException
from .wqx_v3_0.WQX import WQX
from .wqx_v3_0.WQX_Delete import WQXDelete
from .wqx_v3_0.WQX_Update_Identifiers import WQXUpdateIdentifiers


class OperationType(Enum):
    UPDATE_INSERT = "Update-Insert"
    DELETE = "Delete"


class Payload:
    """
    The Payload section of the document contains the WQX data.
    """

    __operation: OperationType
    __wqx: WQX
    __wqxUpdateIdentifiers: WQXUpdateIdentifiers
    __wqxDelete: WQXDelete

    UPDATE_INSERT = OperationType.UPDATE_INSERT
    DELETE = OperationType.DELETE

    def __init__(
        self,
        o: dict = None,
        *,
        operation=None,
        wqx=None,
        wqxUpdateIdentifiers=None,
        wqxDelete=None
    ):
        if isinstance(o, Payload):
            # Assign attributes from other Payload without typechecking
            self.__operation = o.operation
            self.__wqx = o.wqx
            self.__wqxUpdateIdentifiers = o.wqxUpdateIdentifiers
            self.__wqxDelete = o.wqxDelete
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.operation = o.get("operation")
            self.wqx = o.get("wqx")
            self.wqxUpdateIdentifiers = o.get("wqxUpdateIdentifiers")
            self.wqxDelete = o.get("wqxDelete")
        else:
            # Assign attributes from named keywords with typechecking
            self.operation = operation
            self.wqx = wqx
            self.wqxUpdateIdentifiers = wqxUpdateIdentifiers
            self.wqxDelete = wqxDelete

    @property
    def operation(self) -> OperationType:
        return self.__operation

    @operation.setter
    def operation(self, val: OperationType) -> None:
        self.__operation = None if val is None else OperationType(val)

    @property
    def wqx(self) -> WQX:
        return self.__wqx

    @wqx.setter
    def wqx(self, val: WQX) -> None:
        if val is not None and not isinstance(val, WQX):
            raise WQXException("Attribute 'wqx' must be a WQX object, if provided.")
        self.__wqx = None if val is None else WQX(val)

    @property
    def wqxUpdateIdentifiers(self) -> WQXUpdateIdentifiers:
        return self.__wqxUpdateIdentifiers

    @wqxUpdateIdentifiers.setter
    def wqxUpdateIdentifiers(self, val: WQXUpdateIdentifiers) -> None:
        if val is not None and not isinstance(val, WQXUpdateIdentifiers):
            raise WQXException(
                "Attribute 'wqxUpdateIdentifiers' must be a WQXUpdateIdentifiers object, "
                "if provided."
            )
        self.__wqxUpdateIdentifiers = None if val is None else WQXUpdateIdentifiers(val)

    @property
    def wqxDelete(self) -> WQXDelete:
        return self.__wqxDelete

    @wqxDelete.setter
    def wqxDelete(self, val: WQXDelete) -> None:
        if val is not None and not isinstance(val, WQXDelete):
            raise WQXException(
                "Attribute 'wqxDelete' must be a WQXDelete object, if provided."
            )
        self.__wqxDelete = None if val is None else WQXDelete(val)

    def generateXML(self, name: str = "Payload") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis

        if self.__operation is None:
            raise WQXException("Attribute 'operation' is required.")
        with doc.tag(name, ("Operation", self.__operation.value)):
            if self.__operation == OperationType.UPDATE_INSERT:
                if self.__wqxDelete is not None:
                    raise WQXException(
                        "Attribute 'wqxDelete' must be set to None for 'Update-Insert' "
                        "operation."
                    )
                if self.__wqx is None and self.__wqxUpdateIdentifiers is None:
                    raise WQXException(
                        "One of attributes 'wqx' or 'wqxUpdateIdentifiers' are required "
                        "for 'Update-Insert' operation."
                    )
                elif self.__wqx is not None and self.__wqxUpdateIdentifiers is not None:
                    raise WQXException(
                        "One of attributes 'wqx' or 'wqxUpdateIdentifiers' must be set "
                        "to None for 'Update-Insert' operation."
                    )
                elif self.__wqx is None and self.__wqxUpdateIdentifiers is None:
                    raise WQXException(
                        "One of attributes 'wqx' or 'wqxUpdateIdentifiers' must be set "
                        "for 'Update-Insert' operation."
                    )
                elif self.__wqx is not None and self.__wqxUpdateIdentifiers is None:
                    asis(self.__wqx.generateXML("WQX"))
                elif self.__wqxUpdateIdentifiers is not None and self.__wqx is None:
                    asis(self.__wqxUpdateIdentifiers.generateXML("WQXUpdateIdentifiers"))
            elif self.__operation == OperationType.DELETE:
                if self.__wqx is not None:
                    raise WQXException(
                        "Attribute 'wqx' must be set to None for 'Delete' operation."
                    )
                if self.__wqxUpdateIdentifiers is not None:
                    raise WQXException(
                        "Attribute 'wqxUpdateIdentifiers' must be set to None for "
                        "'Delete' operation."
                    )
                if self.__wqxDelete is None:
                    raise WQXException(
                        "Attribute 'wqxDelete' is required for 'Delete' operation."
                    )
                asis(self.__wqxDelete.generateXML("WQXDelete"))
            else:
                raise WQXException(
                    "Attribute 'operation' must be either 'Update-Insert' or 'Delete'."
                )

        return doc.getvalue()
