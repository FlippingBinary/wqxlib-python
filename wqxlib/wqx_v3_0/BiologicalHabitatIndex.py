from yattag import Doc

from ..exceptions import WQXException
from .IndexType import IndexType
from .SimpleContent import (
    CommentText,
    IndexCalculatedDate,
    IndexIdentifier,
    IndexQualifierCode,
    IndexScore,
    MonitoringLocationIdentifier,
)


class BiologicalHabitatIndex:
    """
    This section allows for the reporting of habitat and biotic integrity indices as a
    representation of water quality conditions.
    """

    __indexIdentifier: IndexIdentifier
    __indexType: IndexType
    __indexScore: IndexScore
    __indexQualifierCode: IndexQualifierCode
    __indexCommentText: CommentText
    __indexCalculatedDate: IndexCalculatedDate
    __monitoringLocationIdentifier: MonitoringLocationIdentifier

    def __init__(
        self,
        o: dict = None,
        *,
        indexIdentifier: IndexIdentifier = None,
        indexType: IndexType = None,
        indexScore: IndexScore = None,
        indexQualifierCode: IndexQualifierCode = None,
        indexCommentText: CommentText = None,
        indexCalculatedDate: IndexCalculatedDate = None,
        monitoringLocationIdentifier: MonitoringLocationIdentifier = None
    ):
        if isinstance(o, BiologicalHabitatIndex):
            # Assign attributes from object without typechecking
            self.__indexIdentifier = o.indexIdentifier
            self.__indexType = o.indexType
            self.__indexScore = o.indexScore
            self.__indexQualifierCode = o.indexQualifierCode
            self.__indexCommentText = o.indexCommentText
            self.__indexCalculatedDate = o.indexCalculatedDate
            self.__monitoringLocationIdentifier = o.monitoringLocationIdentifier
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.indexIdentifier = o.get("indexIdentifier")
            self.indexType = o.get("indexType")
            self.indexScore = o.get("indexScore")
            self.indexQualifierCode = o.get("indexQualifierCode")
            self.indexCommentText = o.get("indexCommentText")
            self.indexCalculatedDate = o.get("indexCalculatedDate")
            self.monitoringLocationIdentifier = o.get("monitoringLocationIdentifier")
        else:
            # Assign attributes from named keywords with typechecking
            self.indexIdentifier = indexIdentifier
            self.indexType = indexType
            self.indexScore = indexScore
            self.indexQualifierCode = indexQualifierCode
            self.indexCommentText = indexCommentText
            self.indexCalculatedDate = indexCalculatedDate
            self.monitoringLocationIdentifier = monitoringLocationIdentifier

    @property
    def indexIdentifier(self) -> IndexIdentifier:
        return self.__indexIdentifier

    @indexIdentifier.setter
    def indexIdentifier(self, val: IndexIdentifier) -> None:
        self.__indexIdentifier = IndexIdentifier(val)

    @property
    def indexType(self) -> IndexType:
        return self.__indexType

    @indexType.setter
    def indexType(self, val: IndexType) -> None:
        self.__indexType = None if val is None else IndexType(val)

    @property
    def indexScore(self) -> IndexScore:
        return self.__indexScore

    @indexScore.setter
    def indexScore(self, val: IndexScore) -> None:
        self.__indexScore = IndexScore(val)

    @property
    def indexQualifierCode(self) -> IndexQualifierCode:
        return self.__indexQualifierCode

    @indexQualifierCode.setter
    def indexQualifierCode(self, val: IndexQualifierCode) -> None:
        self.__indexQualifierCode = None if val is None else IndexQualifierCode(val)

    @property
    def indexCommentText(self) -> CommentText:
        """
        Free text with general comments concerning the index.
        """
        return self.__indexCommentText

    @indexCommentText.setter
    def indexCommentText(self, val: CommentText) -> None:
        """
        Free text with general comments concerning the index.
        """
        self.__indexCommentText = None if val is None else CommentText(val)

    @property
    def indexCalculatedDate(self) -> IndexCalculatedDate:
        return self.__indexCalculatedDate

    @indexCalculatedDate.setter
    def indexCalculatedDate(self, val: IndexCalculatedDate) -> None:
        self.__indexCalculatedDate = None if val is None else IndexCalculatedDate(val)

    @property
    def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
        return self.__monitoringLocationIdentifier

    @monitoringLocationIdentifier.setter
    def monitoringLocationIdentifier(self, val: MonitoringLocationIdentifier) -> None:
        self.__monitoringLocationIdentifier = MonitoringLocationIdentifier(val)

    def generateXML(self, name: str = "BiologicalHabitatIndex") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__indexIdentifier is None:
                raise WQXException("Attribute 'indexIdentifier' is required.")
            line("IndexIdentifier", self.__indexIdentifier)
            if self.__indexType is None:
                raise WQXException("Attribute 'indexType' is required.")
            asis(self.__indexType.generateXML("IndexType"))
            if self.__indexScore is None:
                raise WQXException("Attribute 'indexScore' is required.")
            line("IndexScore", self.__indexScore)
            if self.__indexQualifierCode is not None:
                line("IndexQualifierCode", self.__indexQualifierCode)
            if self.__indexCommentText is not None:
                line("IndexCommentText", self.__indexCommentText)
            if self.__indexCalculatedDate is not None:
                line("IndexCalculatedDate", self.__indexCalculatedDate)
            if self.__monitoringLocationIdentifier is None:
                raise WQXException(
                    "Attribute 'monitoringLocationIdentifier' is required."
                )
            line("MonitoringLocationIdentifier", self.__monitoringLocationIdentifier)

        return doc.getvalue()
