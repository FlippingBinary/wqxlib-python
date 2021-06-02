from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .ActivityDescription import ActivityDescription
from .ActivityLocation import ActivityLocation
from .ActivityMetric import ActivityMetric
from .AttachedBinaryObject import AttachedBinaryObject
from .BiologicalActivityDescription import BiologicalActivityDescription
from .Result import Result
from .SampleDescription import SampleDescription


class Activity:
    """
    Allows for the reporting of monitoring activities conducted at a Monitoring Location.
    """

    __activityDescription: ActivityDescription = None
    __activityLocation: ActivityLocation = None
    __biologicalActivityDescription: BiologicalActivityDescription = None
    __sampleDescription: SampleDescription = None
    __activityMetric: List[ActivityMetric] = []
    __attachedBinaryObject: List[AttachedBinaryObject] = []
    __results: List[Result] = []

    def __init__(
        self,
        o: dict = None,
        *,
        activityDescription: ActivityDescription = None,
        activityLocation: ActivityLocation = None,
        biologicalActivityDescription: BiologicalActivityDescription = None,
        sampleDescription: SampleDescription = None,
        activityMetric: List[ActivityMetric] = None,
        attachedBinaryObject: List[AttachedBinaryObject] = None,
        results: List[Result] = None
    ):
        if isinstance(o, Activity):
            # Assign attributes from object without typechecking
            self.__activityDescription = o.activityDescription
            self.__activityLocation = o.activityLocation
            self.__biologicalActivityDescription = o.biologicalActivityDescription
            self.__sampleDescription = o.sampleDescription
            self.__activityMetric = o.activityMetric
            self.__attachedBinaryObject = o.attachedBinaryObject
            self.__results = o.results
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.activityDescription = o.get("activityDescription")
            self.activityLocation = o.get("activityLocation")
            self.biologicalActivityDescription = o.get("biologicalActivityDescription")
            self.sampleDescription = o.get("sampleDescription")
            self.activityMetric = o.get(activityMetric, [])
            self.attachedBinaryObject = o.get("attachedBinaryObject", [])
            self.results = o.get("results", [])
        else:
            # Assign attributes from named keywords with typechecking
            self.activityDescription = activityDescription
            self.activityLocation = activityLocation
            self.biologicalActivityDescription = biologicalActivityDescription
            self.sampleDescription = sampleDescription
            self.activityMetric = activityMetric
            self.attachedBinaryObject = attachedBinaryObject
            self.results = results

    @property
    def activityDescription(self) -> ActivityDescription:
        return self.__activityDescription

    @activityDescription.setter
    def activityDescription(self, val: ActivityDescription) -> None:
        self.__activityDescription = None if val is None else ActivityDescription(val)

    @property
    def activityLocation(self) -> ActivityLocation:
        return self.__activityLocation

    @activityLocation.setter
    def activityLocation(self, val: ActivityLocation) -> None:
        self.__activityLocation = None if val is None else ActivityLocation(val)

    @property
    def biologicalActivityDescription(self) -> BiologicalActivityDescription:
        return self.__biologicalActivityDescription

    @biologicalActivityDescription.setter
    def biologicalActivityDescription(self, val: BiologicalActivityDescription) -> None:
        self.__biologicalActivityDescription = (
            None if val is None else BiologicalActivityDescription(val)
        )

    @property
    def sampleDescription(self) -> SampleDescription:
        return self.__sampleDescription

    @sampleDescription.setter
    def sampleDescription(self, val: SampleDescription) -> None:
        self.__sampleDescription = None if val is None else SampleDescription(val)

    @property
    def activityMetric(self) -> List[ActivityMetric]:
        return self.__activityMetric

    @activityMetric.setter
    def activityMetric(self, val: Union[ActivityMetric, List[ActivityMetric]]) -> None:
        if val is None:
            self.__activityMetric = []
        elif isinstance(val, list):
            r: List[ActivityMetric] = []
            for x in val:
                r.append(ActivityMetric(x))
            self.__activityMetric = r
        else:
            self.__activityMetric = [ActivityMetric(val)]

    @property
    def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
        return self.__attachedBinaryObject

    @attachedBinaryObject.setter
    def attachedBinaryObject(
        self, val: Union[AttachedBinaryObject, List[AttachedBinaryObject]]
    ) -> None:
        if val is None:
            self.__attachedBinaryObject = []
        elif isinstance(val, list):
            r: List[AttachedBinaryObject] = []
            for x in val:
                r.append(AttachedBinaryObject(x))
            self.__attachedBinaryObject = r
        else:
            self.__attachedBinaryObject = [AttachedBinaryObject(val)]

    @property
    def results(self) -> List[Result]:
        return self.__results

    @results.setter
    def results(self, val: Union[Result, List[Result]]) -> None:
        if val is None:
            self.__results = []
        elif isinstance(val, list):
            r: List[Result] = []
            for x in val:
                r.append(Result(x))
            self.__results = r
        else:
            self.__results = [Result(val)]

    def generateXML(self, name: str = "Activity") -> str:
        doc = Doc()
        asis = doc.asis
        tag = doc.tag

        with tag(name):
            if self.__activityDescription is None:
                raise WQXException("Attribute 'activityDescription' is required.")
            asis(self.__activityDescription.generateXML("ActivityDescription"))
            if self.__activityLocation is not None:
                asis(self.__activityLocation.generateXML("ActivityLocation"))
            if self.__biologicalActivityDescription is not None:
                asis(
                    self.__biologicalActivityDescription.generateXML(
                        "BiologicalActivityDescription"
                    )
                )
            if self.__sampleDescription is not None:
                asis(self.__sampleDescription.generateXML("SampleDescription"))
            for x in self.__activityMetric:
                asis(x.generateXML("ActivityMetric"))
            for x in self.__attachedBinaryObject:
                asis(x.generateXML("AttachedBinaryObject"))
            for x in self.__results:
                asis(x.generateXML("Result"))

        return doc.getvalue()
