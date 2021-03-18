from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import (
    LocalAquiferCode,
    LocalAquiferCodeContext,
    LocalAquiferDescriptionText,
    LocalAquiferName,
)


class AquiferInformation:
    """
    Identifies the procedures, processes, and references required to determine the
    methods used to obtain a result.
    """

    __localAquiferCode: LocalAquiferCode
    __localAquiferCodeContext: LocalAquiferCodeContext
    __localAquiferName: LocalAquiferName
    __localAquiferDescriptionText: LocalAquiferDescriptionText

    def __init__(
        self,
        o: dict = None,
        *,
        localAquiferCode: LocalAquiferCode = None,
        localAquiferCodeContext: LocalAquiferCodeContext = None,
        localAquiferName: LocalAquiferName = None,
        localAquiferDescriptionText: LocalAquiferDescriptionText = None
    ):
        if isinstance(o, AquiferInformation):
            # Assign attributes from object without typechecking
            self.__localAquiferCode = o.localAquiferCode
            self.__localAquiferCodeContext = o.localAquiferCodeContext
            self.__localAquiferName = o.localAquiferName
            self.__localAquiferDescriptionText = o.localAquiferDescriptionText
        elif isinstance(o, dict):
            # Assign attribute from dictionary with typechecking
            self.localAquiferCode = o.get("localAquiferCode")
            self.localAquiferCodeContext = o.get("localAquiferCodeContext")
            self.localAquiferName = o.get("localAquiferName")
            self.localAquiferDescriptionText = o.get("localAquiferDescriptionText")
        else:
            # Assign attributes from named keywords with typechecking
            self.localAquiferCode = localAquiferCode
            self.localAquiferCodeContext = localAquiferCodeContext
            self.localAquiferName = localAquiferName
            self.localAquiferDescriptionText = localAquiferDescriptionText

    @property
    def localAquiferCode(self) -> LocalAquiferCode:
        return self.__localAquiferCode

    @localAquiferCode.setter
    def localAquiferCode(self, val: LocalAquiferCode) -> None:
        self.__localAquiferCode = LocalAquiferCode(val)

    @property
    def localAquiferCodeContext(self) -> LocalAquiferCodeContext:
        return self.__localAquiferCodeContext

    @localAquiferCodeContext.setter
    def localAquiferCodeContext(self, val: LocalAquiferCodeContext) -> None:
        self.__localAquiferCodeContext = LocalAquiferCodeContext(val)

    @property
    def localAquiferName(self) -> LocalAquiferName:
        return self.__localAquiferName

    @localAquiferName.setter
    def localAquiferName(self, val: LocalAquiferName) -> None:
        self.__localAquiferName = LocalAquiferName(val)

    @property
    def localAquiferDescriptionText(self) -> LocalAquiferDescriptionText:
        return self.__localAquiferDescriptionText

    @localAquiferDescriptionText.setter
    def localAquiferDescriptionText(self, val: LocalAquiferDescriptionText) -> None:
        self.__localAquiferDescriptionText = (
            None if val is None else LocalAquiferDescriptionText(val)
        )

    def generateXML(self, name: str = "AquiferInformation") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__localAquiferCode is None:
                raise WQXException("Attribute 'localAquiferCode' is required.")
            line("LocalAquiferCode", self.__localAquiferCode)
            if self.__localAquiferCodeContext is None:
                raise WQXException("Attribute 'localAquiferCodeContext' is required.")
            line("LocalAquiferCodeContext", self.__localAquiferCodeContext)
            if self.__localAquiferName is None:
                raise WQXException("Attribute 'localAquiferName' is required.")
            line("LocalAquiferName", self.__localAquiferName)
            if self.__localAquiferDescriptionText is not None:
                line("LocalAquiferDescriptionText", self.__localAquiferDescriptionText)

        return doc.getvalue()
