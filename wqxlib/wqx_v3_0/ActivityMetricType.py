from yattag import Doc

from ..exceptions import WQXException
from .BibliographicReference import BibliographicReference
from .SimpleContent import (
    FormulaDescriptionText,
    MetricTypeIdentifier,
    MetricTypeIdentifierContext,
    MetricTypeName,
    MetricTypeScaleText,
)


class ActivityMetricType:
    """
    This section identifies the metric type reported as part of an activity metric.
    """

    __metricTypeIdentifier: MetricTypeIdentifier
    __metricTypeIdentifierContext: MetricTypeIdentifierContext
    __metricTypeName: MetricTypeName
    __metricTypeCitation: BibliographicReference
    __metricTypeScaleText: MetricTypeScaleText
    __formulaDescriptionText: FormulaDescriptionText

    def __init__(
        self,
        o: dict = None,
        *,
        metricTypeIdentifier: MetricTypeIdentifier = None,
        metricTypeIdentifierContext: MetricTypeIdentifierContext = None,
        metricTypeName: MetricTypeName = None,
        metricTypeCitation: BibliographicReference = None,
        metricTypeScaleText: MetricTypeScaleText = None,
        formulaDescriptionText: FormulaDescriptionText = None
    ):
        if isinstance(o, ActivityMetricType):
            # Assign attributes from object without typechecking
            self.__metricTypeIdentifier = o.metricTypeIdentifier
            self.__metricTypeIdentifierContext = o.metricTypeIdentifierContext
            self.__metricTypeName = o.metricTypeName
            self.__metricTypeCitation = o.metricTypeCitation
            self.__metricTypeScaleText = o.metricTypeScaleText
            self.__formulaDescriptionText = o.formulaDescriptionText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.metricTypeIdentifier = o.get("metricTypeIdentifier")
            self.metricTypeIdentifierContext = o.get("metricTypeIdentifierContext")
            self.metricTypeName = o.get("metricTypeName")
            self.metricTypeCitation = o.get("metricTypeCitation")
            self.metricTypeScaleText = o.get("metricTypeScaleText")
            self.formulaDescriptionText = o.get("formulaDescriptionText")
        else:
            # Assign attributes from named keywords with typechecking
            self.metricTypeIdentifier = metricTypeIdentifier
            self.metricTypeIdentifierContext = metricTypeIdentifierContext
            self.metricTypeName = metricTypeName
            self.metricTypeCitation = metricTypeCitation
            self.metricTypeScaleText = metricTypeScaleText
            self.formulaDescriptionText = formulaDescriptionText

    @property
    def metricTypeIdentifier(self) -> MetricTypeIdentifier:
        return self.__metricTypeIdentifier

    @metricTypeIdentifier.setter
    def metricTypeIdentifier(self, val: MetricTypeIdentifier) -> None:
        self.__metricTypeIdentifier = MetricTypeIdentifier(val)

    @property
    def metricTypeIdentifierContext(self) -> MetricTypeIdentifierContext:
        return self.__metricTypeIdentifierContext

    @metricTypeIdentifierContext.setter
    def metricTypeIdentifierContext(self, val: MetricTypeIdentifierContext) -> None:
        self.__metricTypeIdentifierContext = MetricTypeIdentifierContext(val)

    @property
    def metricTypeName(self) -> MetricTypeName:
        return self.__metricTypeName

    @metricTypeName.setter
    def metricTypeName(self, val: MetricTypeName) -> None:
        self.__metricTypeName = None if val is None else MetricTypeName(val)

    @property
    def metricTypeCitation(self) -> BibliographicReference:
        """
        Provides additional description of the source that created or defined the
        metric.
        """
        return self.__metricTypeCitation

    @metricTypeCitation.setter
    def metricTypeCitation(self, val: BibliographicReference) -> None:
        """
        Provides additional description of the source that created or defined the
        metric.
        """
        self.__metricTypeCitation = None if val is None else BibliographicReference(val)

    @property
    def metricTypeScaleText(self) -> MetricTypeScaleText:
        return self.__metricTypeScaleText

    @metricTypeScaleText.setter
    def metricTypeScaleText(self, val: MetricTypeScaleText) -> None:
        self.__metricTypeScaleText = None if val is None else MetricTypeScaleText(val)

    @property
    def formulaDescriptionText(self) -> FormulaDescriptionText:
        return self.__formulaDescriptionText

    @formulaDescriptionText.setter
    def formulaDescriptionText(self, val: FormulaDescriptionText) -> None:
        self.__formulaDescriptionText = (
            None if val is None else FormulaDescriptionText(val)
        )

    def generateXML(self, name: str = "ActivityMetricType") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__metricTypeIdentifier is None:
                raise WQXException("Attribute 'metricTypeIdentifier' is required.")
            line("MetricTypeIdentifier", self.__metricTypeIdentifier)
            if self.__metricTypeIdentifierContext is None:
                raise WQXException("Attribute 'metricTypeIdentifierContext' is required.")
            line("MetricTypeIdentifierContext", self.__metricTypeIdentifierContext)
            if self.__metricTypeName is not None:
                line("MetricTypeName", self.__metricTypeName)
            if self.__metricTypeCitation is not None:
                asis(self.__metricTypeCitation.generateXML("MetricTypeCitation"))
            if self.__metricTypeScaleText is not None:
                line("MetricTypeScaleText", self.__metricTypeScaleText)
            if self.__formulaDescriptionText is not None:
                line("FormulaDescriptionText", self.__formulaDescriptionText)

        return doc.getvalue()
