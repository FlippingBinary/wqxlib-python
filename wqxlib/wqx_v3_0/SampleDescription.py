from yattag import Doc

from ..exceptions import WQXException
from .ReferenceMethod import ReferenceMethod
from .SamplePreparation import SamplePreparation
from .SimpleContent import (
    HydrologicCondition,
    HydrologicEvent,
    SampleCollectionEquipmentCommentText,
    SampleCollectionEquipmentName,
)


class SampleDescription:
    """
    Basic identification information for the sample collected as part of a monitoring
    activity.
    """

    __sampleCollectionMethod: ReferenceMethod = None
    __sampleCollectionEquipmentName: SampleCollectionEquipmentName = None
    __sampleCollectionEquipmentCommentText: SampleCollectionEquipmentCommentText = None
    __samplePreparation: SamplePreparation = None
    __hydrologicCondition: HydrologicCondition = None
    __hydrologicEvent: HydrologicEvent = None

    def __init__(
        self,
        o: dict = None,
        *,
        sampleCollectionMethod: ReferenceMethod = None,
        sampleCollectionEquipmentName: SampleCollectionEquipmentName = None,
        sampleCollectionEquipmentCommentText: SampleCollectionEquipmentCommentText = None,
        samplePreparation: SamplePreparation = None,
        hydrologicCondition: HydrologicCondition = None,
        hydrologicEvent: HydrologicEvent = None
    ):
        if isinstance(o, SampleDescription):
            # Assign attributes from object without typechecking
            self.__sampleCollectionMethod = o.sampleCollectionMethod
            self.__sampleCollectionEquipmentName = o.sampleCollectionEquipmentName
            self.__sampleCollectionEquipmentCommentText = (
                o.sampleCollectionEquipmentCommentText
            )
            self.__samplePreparation = o.samplePreparation
            self.__hydrologicCondition = o.hydrologicCondition
            self.__hydrologicEvent = o.hydrologicEvent
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.sampleCollectionMethod = o.get("sampleCollectionMethod")
            self.sampleCollectionEquipmentName = o.get("sampleCollectionEquipmentName")
            self.sampleCollectionEquipmentCommentText = o.get(
                "sampleCollectionEquipmentCommentText"
            )
            self.samplePreparation = o.get("samplePreparation")
            self.hydrologicCondition = o.get("hydrologicCondition")
            self.hydrologicEvent = o.get("hydrologicEvent")
        else:
            # Assign attributes from named keywords with typechecking
            self.sampleCollectionMethod = sampleCollectionMethod
            self.sampleCollectionEquipmentName = sampleCollectionEquipmentName
            self.sampleCollectionEquipmentCommentText = (
                sampleCollectionEquipmentCommentText
            )
            self.samplePreparation = samplePreparation
            self.hydrologicCondition = hydrologicCondition
            self.hydrologicEvent = hydrologicEvent

    @property
    def sampleCollectionMethod(self) -> ReferenceMethod:
        """
        Identifies sample collection or measurement method procedures. Where a
        documented sample collection method has been employed, this enables the data
        provider to indicate the documented method that was employed during the field
        sample collection. Otherwise, the sample collection procedure will best be
        described in a freeform text.
        """
        return self.__sampleCollectionMethod

    @sampleCollectionMethod.setter
    def sampleCollectionMethod(self, val: ReferenceMethod) -> None:
        """
        Identifies sample collection or measurement method procedures. Where a documented
        sample collection method has been employed, this enables the data provider to
        indicate the documented method that was employed during the field sample
        collection. Otherwise, the sample collection procedure will best be described in
        a freeform text.
        """
        self.__sampleCollectionMethod = None if val is None else ReferenceMethod(val)

    @property
    def sampleCollectionEquipmentName(self) -> SampleCollectionEquipmentName:
        return self.__sampleCollectionEquipmentName

    @sampleCollectionEquipmentName.setter
    def sampleCollectionEquipmentName(self, val: SampleCollectionEquipmentName) -> None:
        self.__sampleCollectionEquipmentName = (
            None if val is None else SampleCollectionEquipmentName(val)
        )

    @property
    def sampleCollectionEquipmentCommentText(
        self,
    ) -> SampleCollectionEquipmentCommentText:
        return self.__sampleCollectionEquipmentCommentText

    @sampleCollectionEquipmentCommentText.setter
    def sampleCollectionEquipmentCommentText(
        self, val: SampleCollectionEquipmentCommentText
    ) -> None:
        self.__sampleCollectionEquipmentCommentText = (
            None if val is None else SampleCollectionEquipmentCommentText(val)
        )

    @property
    def samplePreparation(self) -> SamplePreparation:
        return self.__samplePreparation

    @samplePreparation.setter
    def samplePreparation(self, val: SamplePreparation) -> None:
        self.__samplePreparation = None if val is None else SamplePreparation(val)

    @property
    def hydrologicCondition(self) -> HydrologicCondition:
        return self.__hydrologicCondition

    @hydrologicCondition.setter
    def hydrologicCondition(self, val: HydrologicCondition) -> None:
        self.__hydrologicCondition = None if val is None else HydrologicCondition(val)

    @property
    def hydrologicEvent(self) -> HydrologicEvent:
        return self.__hydrologicEvent

    @hydrologicEvent.setter
    def hydrologicEvent(self, val: HydrologicEvent) -> None:
        self.__hydrologicEvent = None if val is None else HydrologicEvent(val)

    def generateXML(self, name: str = "SampleDescription") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__sampleCollectionMethod is not None:
                asis(self.__sampleCollectionMethod.generateXML("SampleCollectionMethod"))
            if self.__sampleCollectionEquipmentName is None:
                raise WQXException(
                    "Attribute 'sampleCollectionEquipmentName' is required."
                )
            line("SampleCollectionEquipmentName", self.__sampleCollectionEquipmentName)
            if self.__sampleCollectionEquipmentCommentText is not None:
                line(
                    "SampleCollectionEquipmentCommentText",
                    self.__sampleCollectionEquipmentCommentText,
                )
            if self.__samplePreparation is not None:
                asis(self.__samplePreparation.generateXML("SamplePreparation"))
            if self.__hydrologicCondition is not None:
                line("HydrologicCondition", self.__hydrologicCondition)
            if self.__hydrologicEvent is not None:
                line("HydrologicEvent", self.__hydrologicEvent)

        return doc.getvalue()
