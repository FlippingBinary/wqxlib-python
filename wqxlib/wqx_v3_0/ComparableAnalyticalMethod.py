from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import (
    MethodIdentifier,
    MethodIdentifierContext,
    MethodModificationText,
)


class ComparableAnalyticalMethod:
    """
    Identifies the procedures, processes, and references required to determine the
    analytical methods used to obtain a result.
    """

    __methodIdentifier: MethodIdentifier
    __methodIdentifierContext: MethodIdentifierContext
    __methodModificationText: MethodModificationText

    def __init__(
        self,
        o: dict = None,
        *,
        methodIdentifier: MethodIdentifier = None,
        methodIdentifierContext: MethodIdentifierContext = None,
        methodModificationText: MethodModificationText = None
    ):
        if isinstance(o, ComparableAnalyticalMethod):
            # Assign attributes from object without typechecking
            self.__methodIdentifier = o.methodIdentifier
            self.__methodIdentifierContext = o.methodIdentifierContext
            self.__methodModificationText = o.methodModificationText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.methodIdentifier = o.get("methodIdentifier")
            self.methodIdentifierContext = o.get("methodIdentifierContext")
            self.methodModificationText = o.get("methodModificationText")
        else:
            # Assign attributes from named keywords with typechecking
            self.methodIdentifier = methodIdentifier
            self.methodIdentifierContext = methodIdentifierContext
            self.methodModificationText = methodModificationText

    @property
    def methodIdentifier(self) -> MethodIdentifier:
        return self.__methodIdentifier

    @methodIdentifier.setter
    def methodIdentifier(self, val: MethodIdentifier) -> None:
        self.__methodIdentifier = MethodIdentifier(val)

    @property
    def methodIdentifierContext(self) -> MethodIdentifierContext:
        return self.__methodIdentifierContext

    @methodIdentifierContext.setter
    def methodIdentifierContext(self, val: MethodIdentifierContext) -> None:
        self.__methodIdentifierContext = MethodIdentifierContext(val)

    @property
    def methodModificationText(self) -> MethodModificationText:
        return self.__methodModificationText

    @methodModificationText.setter
    def methodModificationText(self, val: MethodModificationText) -> None:
        self.__methodModificationText = (
            None if val is None else MethodModificationText(val)
        )

    def generateXML(self, name: str = "ComparableAnalyticalMethod") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__methodIdentifier is None:
                raise WQXException("Attribute 'methodIdentifier' is required.")
            line("MethodIdentifier", self.__methodIdentifier)
            if self.__methodIdentifierContext is None:
                raise WQXException("Attribute 'methodIdentifierContext' is required.")
            line("MethodIdentifierContext", self.__methodIdentifierContext)
            if self.__methodModificationText is not None:
                line("MethodModificationText", self.__methodModificationText)

        return doc.getvalue()
