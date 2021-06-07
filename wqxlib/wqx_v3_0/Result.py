from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .AttachedBinaryObject import AttachedBinaryObject
from .BiologicalResultDescription import BiologicalResultDescription
from .ComparableAnalyticalMethod import ComparableAnalyticalMethod
from .LabSamplePreparation import LabSamplePreparation
from .ResultAnalyticalMethod import ResultAnalyticalMethod
from .ResultDescription import ResultDescription
from .ResultLabInformation import ResultLabInformation


class Result:
    """
    Describes the results of a field measurement, observation, or laboratory analysis.
    """

    __resultDescription: ResultDescription
    __biologicalResultDescription: BiologicalResultDescription
    __attachedBinaryObject: List[AttachedBinaryObject]
    __resultAnalyticalMethod: ResultAnalyticalMethod
    __comparableAnalyticalMethod: ComparableAnalyticalMethod
    __resultLabInformation: ResultLabInformation
    __labSamplePreparation: List[LabSamplePreparation]

    def __init__(
        self,
        o: dict = None,
        *,
        resultDescription: ResultDescription = None,
        biologicalResultDescription: BiologicalResultDescription = None,
        attachedBinaryObject: List[AttachedBinaryObject] = None,
        resultAnalyticalMethod: ResultAnalyticalMethod = None,
        comparableAnalyticalMethod: ComparableAnalyticalMethod = None,
        resultLabInformation: ResultLabInformation = None,
        labSamplePreparation: List[LabSamplePreparation] = None
    ):
        if isinstance(o, Result):
            # Assign attributes from object without typechecking
            self.__resultDescription = o.resultDescription
            self.__biologicalResultDescription = o.biologicalResultDescription
            self.__attachedBinaryObject = o.attachedBinaryObject
            self.__resultAnalyticalMethod = o.resultAnalyticalMethod
            self.__comparableAnalyticalMethod = o.comparableAnalyticalMethod
            self.__resultLabInformation = o.resultLabInformation
            self.__labSamplePreparation = o.labSamplePreparation
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.resultDescription = o.get("resultDescription")
            self.biologicalResultDescription = o.get("biologicalResultDescription")
            self.attachedBinaryObject = o.get("attachedBinaryObject")
            self.resultAnalyticalMethod = o.get("resultAnalyticalMethod")
            self.comparableAnalyticalMethod = o.get("comparableAnalyticalMethod")
            self.resultLabInformation = o.get("resultLabInformation")
            self.labSamplePreparation = o.get("labSamplePreparation")
        else:
            # Assign attributes from named keywords with typechecking
            self.resultDescription = resultDescription
            self.biologicalResultDescription = biologicalResultDescription
            self.attachedBinaryObject = attachedBinaryObject
            self.resultAnalyticalMethod = resultAnalyticalMethod
            self.comparableAnalyticalMethod = comparableAnalyticalMethod
            self.resultLabInformation = resultLabInformation
            self.labSamplePreparation = labSamplePreparation

    @property
    def resultDescription(self) -> ResultDescription:
        return self.__resultDescription

    @resultDescription.setter
    def resultDescription(self, val: ResultDescription) -> None:
        self.__resultDescription = None if val is None else ResultDescription(val)

    @property
    def biologicalResultDescription(self) -> BiologicalResultDescription:
        return self.__biologicalResultDescription

    @biologicalResultDescription.setter
    def biologicalResultDescription(self, val: BiologicalResultDescription) -> None:
        self.__biologicalResultDescription = (
            None if val is None else BiologicalResultDescription(val)
        )

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
    def resultAnalyticalMethod(self) -> ResultAnalyticalMethod:
        return self.__resultAnalyticalMethod

    @resultAnalyticalMethod.setter
    def resultAnalyticalMethod(self, val: ResultAnalyticalMethod) -> None:
        self.__resultAnalyticalMethod = (
            None if val is None else ResultAnalyticalMethod(val)
        )

    @property
    def comparableAnalyticalMethod(self) -> ComparableAnalyticalMethod:
        return self.__comparableAnalyticalMethod

    @comparableAnalyticalMethod.setter
    def comparableAnalyticalMethod(self, val: ComparableAnalyticalMethod) -> None:
        self.__comparableAnalyticalMethod = (
            None if val is None else ComparableAnalyticalMethod(val)
        )

    @property
    def resultLabInformation(self) -> ResultLabInformation:
        return self.__resultLabInformation

    @resultLabInformation.setter
    def resultLabInformation(self, val: ResultLabInformation) -> None:
        self.__resultLabInformation = None if val is None else ResultLabInformation(val)

    @property
    def labSamplePreparation(self) -> List[LabSamplePreparation]:
        return self.__labSamplePreparation

    @labSamplePreparation.setter
    def labSamplePreparation(
        self, val: Union[LabSamplePreparation, List[LabSamplePreparation]]
    ) -> None:
        if val is None:
            self.__labSamplePreparation = []
        elif isinstance(val, list):
            r: List[LabSamplePreparation] = []
            for x in val:
                r.append(LabSamplePreparation(x))
            self.__labSamplePreparation = r
        else:
            self.__labSamplePreparation = [LabSamplePreparation(val)]

    def generateXML(self, name: str = "Result") -> str:
        doc = Doc()
        asis = doc.asis
        tag = doc.tag

        with tag(name):
            if self.__resultDescription is None:
                raise WQXException("Attribute 'resultDescription' is required.")
            asis(self.__resultDescription.generateXML("ResultDescription"))
            if self.__biologicalResultDescription is not None:
                asis(
                    self.__biologicalResultDescription.generateXML(
                        "BiologicalResultDescription"
                    )
                )
            for x in self.__attachedBinaryObject:
                asis(x.generateXML("AttachedBinaryObject"))
            if self.__resultAnalyticalMethod is not None:
                asis(self.__resultAnalyticalMethod.generateXML("ResultAnalyticalMethod"))
            if self.__comparableAnalyticalMethod is not None:
                asis(
                    self.__comparableAnalyticalMethod.generateXML(
                        "ComparableAnalyticalMethod"
                    )
                )
            if self.__resultLabInformation is not None:
                asis(self.__resultLabInformation.generateXML("ResultLabInformation"))
            for x in self.__labSamplePreparation:
                asis(x.generateXML("LabSamplePreparation"))

        return doc.getvalue()
