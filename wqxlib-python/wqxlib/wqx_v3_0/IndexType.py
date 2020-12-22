from yattag import Doc, indent
from .BibliographicReference import BibliographicReference
from .SimpleContent import *
from ..WQXException import WQXException

class IndexType:
  """This section identifies the index type reported as part of a biological or habitat index."""

  __indexTypeIdentifier: IndexTypeIdentifier
  __indexTypeIdentifierContext: IndexTypeIdentifierContext
  __indexTypeName: IndexTypeName
  __indexTypeCitation: BibliographicReference
  __indexTypeScaleText: IndexTypeScaleText

  def __init__(self):
    self.__indexTypeIdentifier = None
    self.__indexTypeIdentifierContext = None
    self.__indexTypeName = None
    self.__indexTypeCitation = None
    self.__indexTypeScaleText = None

  @property
  def indexTypeIdentifier(self) -> IndexTypeIdentifier:
    return self.__indexTypeIdentifier
  @indexTypeIdentifier.setter
  def indexTypeIdentifier(self, val:IndexTypeIdentifier) -> None:
    self.__indexTypeIdentifier = IndexTypeIdentifier(val)

  @property
  def indexTypeIdentifierContext(self) -> IndexTypeIdentifierContext:
    return self.__indexTypeIdentifierContext
  @indexTypeIdentifierContext.setter
  def indexTypeIdentifierContext(self, val:IndexTypeIdentifierContext) -> None:
    self.__indexTypeIdentifierContext = IndexTypeIdentifierContext(val)

  @property
  def indexTypeName(self) -> IndexTypeName:
    return self.__indexTypeName
  @indexTypeName.setter
  def indexTypeName(self, val:IndexTypeName) -> None:
    self.__indexTypeName = IndexTypeName(val)

  @property
  def indexTypeCitation(self) -> BibliographicReference:
    """Provides additional description of the source that created or defined the index."""
    return self.__indexTypeCitation
  @indexTypeCitation.setter
  def indexTypeCitation(self, val:BibliographicReference) -> None:
    """Provides additional description of the source that created or defined the index."""
    self.__indexTypeCitation = val

  @property
  def indexTypeScaleText(self) -> IndexTypeScaleText:
    return self.__indexTypeScaleText
  @indexTypeScaleText.setter
  def indexTypeScaleText(self, val:IndexTypeScaleText) -> None:
    self.__indexTypeScaleText = None if val is None else IndexTypeScaleText(val)

  def generateXML(self):
    if self.__indexTypeIdentifier is None:
      WQXException("Attribute 'indexTypeIdentifier' is required.")
    if self.__indexTypeIdentifierContext is None:
      WQXException("Attribute 'indexTypeIdentifierContext' is required.")
    if self.__indexTypeName is None:
      WQXException("Attribute 'indexTypeName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('IndexTypeIdentifier', self.__indexTypeIdentifier)
    line('IndexTypeIdentifierContext', self.__indexTypeIdentifierContext)
    line('IndexTypeName', self.__indexTypeName)
    if self.__indexTypeCitation is not None:
      with tag('IndexTypeCitation'):
        doc.asis(self.__indexTypeCitation.generateXML())
    if self.__indexTypeScaleText is not None:
      line('IndexTypeScaleText', self.__indexTypeScaleText)

    return indent(doc.getvalue(), indentation = ' '*2)
