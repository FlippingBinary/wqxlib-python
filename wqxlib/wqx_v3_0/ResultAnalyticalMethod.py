from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import (
    MethodDescriptionText,
    MethodIdentifier,
    MethodIdentifierContext,
    MethodName,
    MethodQualifierTypeName,
)


class ResultAnalyticalMethod:
    """
    Identifies the procedures, processes, and references required to determine the
    analytical methods used to obtain a result.
    """

    __methodIdentifier: MethodIdentifier
    __methodIdentifierContext: MethodIdentifierContext
    __methodName: MethodName
    __methodQualifierTypeName: MethodQualifierTypeName
    __methodDescriptionText: MethodDescriptionText

    def __init__(
        self,
        o: dict = None,
        *,
        methodIdentifier: MethodIdentifier = None,
        methodIdentifierContext: MethodIdentifierContext = None,
        methodName: MethodName = None,
        methodQualifierTypeName: MethodQualifierTypeName = None,
        methodDescriptionText: MethodDescriptionText = None
    ):
        if isinstance(o, ResultAnalyticalMethod):
            # Assign attributes from object without typechecking
            self.__methodIdentifier = o.methodIdentifier
            self.__methodIdentifierContext = o.methodIdentifierContext
            self.__methodName = o.methodName
            self.__methodQualifierTypeName = o.methodQualifierTypeName
            self.__methodDescriptionText = o.methodDescriptionText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.methodIdentifier = o.get("methodIdentifier")
            self.methodIdentifierContext = o.get("methodIdentifierContext")
            self.methodName = o.get("methodName")
            self.methodQualifierTypeName = o.get("methodQualifierTypeName")
            self.methodDescriptionText = o.get("methodDescriptionText")
        else:
            # Assign attributes from named keywords with typechecking
            self.methodIdentifier = methodIdentifier
            self.methodIdentifierContext = methodIdentifierContext
            self.methodName = methodName
            self.methodQualifierTypeName = methodQualifierTypeName
            self.methodDescriptionText = methodDescriptionText

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
    def methodName(self) -> MethodName:
        return self.__methodName

    @methodName.setter
    def methodName(self, val: MethodName) -> None:
        self.__methodName = None if val is None else MethodName(val)

    @property
    def methodQualifierTypeName(self) -> MethodQualifierTypeName:
        return self.__methodQualifierTypeName

    @methodQualifierTypeName.setter
    def methodQualifierTypeName(self, val: MethodQualifierTypeName) -> None:
        self.__methodQualifierTypeName = (
            None if val is None else MethodQualifierTypeName(val)
        )

    @property
    def methodDescriptionText(self) -> MethodDescriptionText:
        return self.__methodDescriptionText

    @methodDescriptionText.setter
    def methodDescriptionText(self, val: MethodDescriptionText) -> None:
        self.__methodDescriptionText = None if val is None else MethodDescriptionText(val)

    def generateXML(self, name: str = "ResultAnalyticalMethod") -> str:
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
            if self.__methodName is not None:
                line("MethodName", self.__methodName)
            if self.__methodQualifierTypeName is not None:
                line("MethodQualifierTypeName", self.__methodQualifierTypeName)
            if self.__methodDescriptionText is not None:
                line("MethodDescriptionText", self.__methodDescriptionText)

        return doc.getvalue()
