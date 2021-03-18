from yattag import Doc

from .ReferenceMethod import ReferenceMethod
from .SimpleContent import (
    PreparationEndDate,
    PreparationStartDate,
    SubstanceDilutionFactor,
)
from .WQXTime import WQXTime


class LabSamplePreparation:
    """
    Describes Lab Sample Preparation procedures which may alter the original state of
    the Sample and produce Lab subsamples.  These Lab Subsamples are analyized and
    reported by the Lab as Sample results.
    """

    __labSamplePreparationMethod: ReferenceMethod
    __preparationStartDate: PreparationStartDate
    __preparationStartTime: WQXTime
    __preparationEndDate: PreparationEndDate
    __preparationEndTime: WQXTime
    __substanceDilutionFactor: SubstanceDilutionFactor

    def __init__(
        self,
        o: dict = None,
        *,
        labSamplePreparationMethod: ReferenceMethod = None,
        preparationStartDate: PreparationStartDate = None,
        preparationStartTime: WQXTime = None,
        preparationEndDate: PreparationEndDate = None,
        preparationEndTime: WQXTime = None,
        substanceDilutionFactor: SubstanceDilutionFactor = None
    ):
        if isinstance(o, LabSamplePreparation):
            # Assign attributes from object without typechecking
            self.__labSamplePreparationMethod = o.labSamplePreparationMethod
            self.__preparationStartDate = o.preparationStartDate
            self.__preparationStartTime = o.preparationStartTime
            self.__preparationEndDate = o.preparationEndDate
            self.__preparationEndTime = o.preparationEndTime
            self.__substanceDilutionFactor = o.substanceDilutionFactor
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.labSamplePreparationMethod = o.get("labSamplePreparationMethod")
            self.preparationStartDate = o.get("preparationStartDate")
            self.preparationStartTime = o.get("preparationStartTime")
            self.preparationEndDate = o.get("preparationEndDate")
            self.preparationEndTime = o.get("preparationEndTime")
            self.substanceDilutionFactor = o.get("substanceDilutionFactor")
        else:
            # Assign attributes from named keywords with typechecking
            self.labSamplePreparationMethod = labSamplePreparationMethod
            self.preparationStartDate = preparationStartDate
            self.preparationStartTime = preparationStartTime
            self.preparationEndDate = preparationEndDate
            self.preparationEndTime = preparationEndTime
            self.substanceDilutionFactor = substanceDilutionFactor

    @property
    def labSamplePreparationMethod(self) -> ReferenceMethod:
        """
        Identifying information about the method followed to prepare a sample for
        analysis.
        """
        return self.__labSamplePreparationMethod

    @labSamplePreparationMethod.setter
    def labSamplePreparationMethod(self, val: ReferenceMethod) -> None:
        """
        Identifying information about the method followed to prepare a sample for
        analysis.
        """
        self.__labSamplePreparationMethod = None if val is None else ReferenceMethod(val)

    @property
    def preparationStartDate(self) -> PreparationStartDate:
        return self.__preparationStartDate

    @preparationStartDate.setter
    def preparationStartDate(self, val: PreparationStartDate) -> None:
        self.__preparationStartDate = None if val is None else PreparationStartDate(val)

    @property
    def preparationStartTime(self) -> WQXTime:
        """
        The local time when the preparation/extraction of the sample for analysis began.
        """
        return self.__preparationStartTime

    @preparationStartTime.setter
    def preparationStartTime(self, val: WQXTime) -> None:
        """
        The local time when the preparation/extraction of the sample for analysis began.
        """
        self.__preparationStartTime = None if val is None else WQXTime(val)

    @property
    def preparationEndDate(self) -> PreparationEndDate:
        return self.__preparationEndDate

    @preparationEndDate.setter
    def preparationEndDate(self, val: PreparationEndDate) -> None:
        self.__preparationEndDate = None if val is None else PreparationEndDate(val)

    @property
    def preparationEndTime(self) -> WQXTime:
        """
        The local time when the preparation/extraction of the sample for analysis was
        finished.
        """
        return self.__preparationEndTime

    @preparationEndTime.setter
    def preparationEndTime(self, val: WQXTime) -> None:
        """
        The local time when the preparation/extraction of the sample for analysis was
        finished.
        """
        self.__preparationEndTime = None if val is None else WQXTime(val)

    @property
    def substanceDilutionFactor(self) -> SubstanceDilutionFactor:
        return self.__substanceDilutionFactor

    @substanceDilutionFactor.setter
    def substanceDilutionFactor(self, val: SubstanceDilutionFactor) -> None:
        self.__substanceDilutionFactor = (
            None if val is None else SubstanceDilutionFactor(val)
        )

    def generateXML(self, name: str = "LabSamplePreparation") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__labSamplePreparationMethod is not None:
                asis(
                    self.__labSamplePreparationMethod.generateXML(
                        "LabSamplePreparationMethod"
                    )
                )
            if self.__preparationStartDate is not None:
                line("PreparationStartDate", self.__preparationStartDate)
            if self.__preparationStartTime is not None:
                asis(self.__preparationStartTime.generateXML("PreparationStartTime"))
            if self.__preparationEndDate is not None:
                line("PreparationEndDate", self.__preparationEndDate)
            if self.__preparationEndTime is not None:
                asis(self.__preparationEndTime.generateXML("PreparationEndTime"))
            if self.__substanceDilutionFactor is not None:
                line("SubstanceDilutionFactor", self.__substanceDilutionFactor)

        return doc.getvalue()
