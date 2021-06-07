from yattag import Doc

from ..exceptions import WQXException
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    DetectionQuantitationLimitCommentText,
    DetectionQuantitationLimitTypeName,
)


class DetectionQuantitationLimit:
    """
    Information that describes one of a variety of detection or quantitation limits
    determined in a laboratory.
    """

    __detectionQuantitationLimitTypeName: DetectionQuantitationLimitTypeName
    __detectionQuantitationLimitMeasure: MeasureCompact
    __detectionQuantitationLimitCommentText: DetectionQuantitationLimitCommentText

    def __init__(
        self,
        o: dict = None,
        *,
        detectionQuantitationLimitTypeName: DetectionQuantitationLimitTypeName = None,
        detectionQuantitationLimitMeasure: MeasureCompact = None,
        detectionQuantitationLimitCommentText: DetectionQuantitationLimitCommentText = None
    ):
        if isinstance(o, DetectionQuantitationLimit):
            # Assign attributes from object without typechecking
            self.__detectionQuantitationLimitTypeName = (
                o.detectionQuantitationLimitTypeName
            )
            self.__detectionQuantitationLimitMeasure = o.detectionQuantitationLimitMeasure
            self.__detectionQuantitationLimitCommentText = (
                o.detectionQuantitationLimitCommentText
            )
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.detectionQuantitationLimitTypeName = o.get(
                "detectionQuantitationLimitTypeName"
            )
            self.detectionQuantitationLimitMeasure = o.get(
                "detectionQuantitationLimitMeasure"
            )
            self.detectionQuantitationLimitCommentText = o.get(
                "detectionQuantitationLimitCommentText"
            )
        else:
            # Assign attributes from named keywords with typechecking
            self.detectionQuantitationLimitTypeName = detectionQuantitationLimitTypeName
            self.detectionQuantitationLimitMeasure = detectionQuantitationLimitMeasure
            self.detectionQuantitationLimitCommentText = (
                detectionQuantitationLimitCommentText
            )

    @property
    def detectionQuantitationLimitTypeName(self) -> DetectionQuantitationLimitTypeName:
        return self.__detectionQuantitationLimitTypeName

    @detectionQuantitationLimitTypeName.setter
    def detectionQuantitationLimitTypeName(
        self, val: DetectionQuantitationLimitTypeName
    ) -> None:
        self.__detectionQuantitationLimitTypeName = DetectionQuantitationLimitTypeName(
            val
        )

    @property
    def detectionQuantitationLimitMeasure(self) -> MeasureCompact:
        return self.__detectionQuantitationLimitMeasure

    @detectionQuantitationLimitMeasure.setter
    def detectionQuantitationLimitMeasure(self, val: MeasureCompact) -> None:
        self.__detectionQuantitationLimitMeasure = MeasureCompact(val)

    @property
    def detectionQuantitationLimitCommentText(
        self,
    ) -> DetectionQuantitationLimitCommentText:
        return self.__detectionQuantitationLimitCommentText

    @detectionQuantitationLimitCommentText.setter
    def detectionQuantitationLimitCommentText(
        self, val: DetectionQuantitationLimitCommentText
    ) -> None:
        self.__detectionQuantitationLimitCommentText = (
            None if val is None else DetectionQuantitationLimitCommentText(val)
        )

    def generateXML(self, name: str = "DetectionQuantitationLimit") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__detectionQuantitationLimitTypeName is None:
                raise WQXException(
                    "Attribute 'detectionQuantitationLimitTypeName' is required."
                )
            line(
                "DetectionQuantitationLimitTypeName",
                self.__detectionQuantitationLimitTypeName,
            )
            if self.__detectionQuantitationLimitMeasure is None:
                raise WQXException(
                    "Attribute 'detectionQuantitationLimitMeasure' is required."
                )
            asis(
                self.__detectionQuantitationLimitMeasure.generateXML(
                    "DetectionQuantitationLimitMeasure"
                )
            )
            if self.__detectionQuantitationLimitCommentText is not None:
                line(
                    "DetectionQuantitationLimitCommentText",
                    self.__detectionQuantitationLimitCommentText,
                )

        return doc.getvalue()
