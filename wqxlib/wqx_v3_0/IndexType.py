from yattag import Doc

from ..exceptions import WQXException
from .BibliographicReference import BibliographicReference
from .SimpleContent import (
    IndexTypeIdentifier,
    IndexTypeIdentifierContext,
    IndexTypeName,
    IndexTypeScaleText,
)


class IndexType:
    """
    This section identifies the index type reported as part of a biological or habitat
    index.
    """

    __indexTypeIdentifier: IndexTypeIdentifier
    __indexTypeIdentifierContext: IndexTypeIdentifierContext
    __indexTypeName: IndexTypeName
    __indexTypeCitation: BibliographicReference
    __indexTypeScaleText: IndexTypeScaleText

    def __init__(
        self,
        o: dict = None,
        *,
        indexTypeIdentifier: IndexTypeIdentifier = None,
        indexTypeIdentifierContext: IndexTypeIdentifierContext = None,
        indexTypeName: IndexTypeName = None,
        indexTypeCitation: BibliographicReference = None,
        indexTypeScaleText: IndexTypeScaleText = None
    ):
        if isinstance(o, IndexType):
            # Assign attributes from object without typechecking
            self.__indexTypeIdentifier = o.indexTypeIdentifier
            self.__indexTypeIdentifierContext = o.indexTypeIdentifierContext
            self.__indexTypeName = o.indexTypeName
            self.__indexTypeCitation = o.indexTypeCitation
            self.__indexTypeScaleText = o.indexTypeScaleText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.indexTypeIdentifier = o.get("indexTypeIdentifier")
            self.indexTypeIdentifierContext = o.get("indexTypeIdentifierContext")
            self.indexTypeName = o.get("indexTypeName")
            self.indexTypeCitation = o.get("indexTypeCitation")
            self.indexTypeScaleText = o.get("indexTypeScaleText")
        else:
            # Assign attributes from named keywords with typechecking
            self.indexTypeIdentifier = indexTypeIdentifier
            self.indexTypeIdentifierContext = indexTypeIdentifierContext
            self.indexTypeName = indexTypeName
            self.indexTypeCitation = indexTypeCitation
            self.indexTypeScaleText = indexTypeScaleText

    @property
    def indexTypeIdentifier(self) -> IndexTypeIdentifier:
        return self.__indexTypeIdentifier

    @indexTypeIdentifier.setter
    def indexTypeIdentifier(self, val: IndexTypeIdentifier) -> None:
        self.__indexTypeIdentifier = IndexTypeIdentifier(val)

    @property
    def indexTypeIdentifierContext(self) -> IndexTypeIdentifierContext:
        return self.__indexTypeIdentifierContext

    @indexTypeIdentifierContext.setter
    def indexTypeIdentifierContext(self, val: IndexTypeIdentifierContext) -> None:
        self.__indexTypeIdentifierContext = IndexTypeIdentifierContext(val)

    @property
    def indexTypeName(self) -> IndexTypeName:
        return self.__indexTypeName

    @indexTypeName.setter
    def indexTypeName(self, val: IndexTypeName) -> None:
        self.__indexTypeName = IndexTypeName(val)

    @property
    def indexTypeCitation(self) -> BibliographicReference:
        """
        Provides additional description of the source that created or defined the index.
        """
        return self.__indexTypeCitation

    @indexTypeCitation.setter
    def indexTypeCitation(self, val: BibliographicReference) -> None:
        """
        Provides additional description of the source that created or defined the index.
        """
        self.__indexTypeCitation = None if val is None else BibliographicReference(val)

    @property
    def indexTypeScaleText(self) -> IndexTypeScaleText:
        return self.__indexTypeScaleText

    @indexTypeScaleText.setter
    def indexTypeScaleText(self, val: IndexTypeScaleText) -> None:
        self.__indexTypeScaleText = None if val is None else IndexTypeScaleText(val)

    def generateXML(self, name: str = "IndexType") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__indexTypeIdentifier is None:
                raise WQXException("Attribute 'indexTypeIdentifier' is required.")
            line("IndexTypeIdentifier", self.__indexTypeIdentifier)
            if self.__indexTypeIdentifierContext is None:
                raise WQXException("Attribute 'indexTypeIdentifierContext' is required.")
            line("IndexTypeIdentifierContext", self.__indexTypeIdentifierContext)
            if self.__indexTypeName is None:
                raise WQXException("Attribute 'indexTypeName' is required.")
            line("IndexTypeName", self.__indexTypeName)
            if self.__indexTypeCitation is not None:
                asis(self.__indexTypeCitation.generateXML("IndexTypeCitation"))
            if self.__indexTypeScaleText is not None:
                line("IndexTypeScaleText", self.__indexTypeScaleText)

        return doc.getvalue()
