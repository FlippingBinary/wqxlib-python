from yattag import Doc

from .SimpleContent import (
    TelephoneExtensionNumberText,
    TelephoneNumberText,
    TelephoneNumberTypeName,
)


class Telephonic:
    """
    An identification of a telephone connection.
    """

    __telephoneNumberText: TelephoneNumberText
    __telephoneNumberTypeName: TelephoneNumberTypeName
    __telephoneExtensionNumberText: TelephoneExtensionNumberText

    def __init__(
        self,
        o: dict = None,
        *,
        telephoneNumberText: TelephoneNumberText = None,
        telephoneNumberTypeName: TelephoneNumberTypeName = None,
        telephoneExtensionNumberText: TelephoneExtensionNumberText = None
    ):
        if isinstance(o, Telephonic):
            # Assign attributes from object without typechecking
            self.__telephoneNumberText = o.telephoneNumberText
            self.__telephoneNumberTypeName = o.telephoneNumberTypeName
            self.__telephoneExtensionNumberText = o.telephoneExtensionNumberText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.telephoneNumberText = o.get("telephoneNumberText")
            self.telephoneNumberTypeName = o.get("telephoneNumberTypeName")
            self.telephoneExtensionNumberText = o.get("telephoneExtensionNumberText")
        else:
            # Assign attributes from named keywords with typechecking
            self.telephoneNumberText = telephoneNumberText
            self.telephoneNumberTypeName = telephoneNumberTypeName
            self.telephoneExtensionNumberText = telephoneExtensionNumberText

    @property
    def telephoneNumberText(self) -> TelephoneNumberText:
        return self.__telephoneNumberText

    @telephoneNumberText.setter
    def telephoneNumberText(self, val: TelephoneNumberText) -> None:
        self.__telephoneNumberText = None if val is None else TelephoneNumberText(val)

    @property
    def telephoneNumberTypeName(self) -> TelephoneNumberTypeName:
        return self.__telephoneNumberTypeName

    @telephoneNumberTypeName.setter
    def telephoneNumberTypeName(self, val: TelephoneNumberTypeName) -> None:
        self.__telephoneNumberTypeName = (
            None if val is None else TelephoneNumberTypeName(val)
        )

    @property
    def telephoneExtensionNumberText(self) -> TelephoneExtensionNumberText:
        return self.__telephoneExtensionNumberText

    @telephoneExtensionNumberText.setter
    def telephoneExtensionNumberText(self, val: TelephoneExtensionNumberText) -> None:
        self.__telephoneExtensionNumberText = (
            None if val is None else TelephoneExtensionNumberText(val)
        )

    def generateXML(self, name: str = "Telephonic") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__telephoneNumberText is not None:
                line("TelephoneNumberText", self.__telephoneNumberText)
            if self.__telephoneNumberTypeName is not None:
                line("TelephoneNumberTypeName", self.__telephoneNumberTypeName)
            if self.__telephoneExtensionNumberText is not None:
                line("TelephoneExtensionNumberText", self.__telephoneExtensionNumberText)

        return doc.getvalue()
