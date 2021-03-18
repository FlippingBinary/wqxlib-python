from typing import List, Union

from yattag import Doc

from .DetectionQuantitationLimit import DetectionQuantitationLimit
from .SimpleContent import (
    AnalysisEndDate,
    AnalysisStartDate,
    LaboratoryAccreditationAuthorityName,
    LaboratoryAccreditationIndicator,
    LaboratoryCommentText,
    LaboratoryName,
    LaboratorySampleSplitRatio,
    TaxonomistAccreditationAuthorityName,
    TaxonomistAccreditationIndicator,
)
from .WQXTime import WQXTime


class ResultLabInformation:
    """
    Describes information obtained by a laboratory related to a specific laboratory analysis.
    """

    __laboratoryName: LaboratoryName
    __analysisStartDate: AnalysisStartDate
    __analysisStartTime: WQXTime
    __analysisEndDate: AnalysisEndDate
    __analysisEndTime: WQXTime
    __laboratoryCommentText: LaboratoryCommentText
    __resultDetectionQuantitationLimit: List[DetectionQuantitationLimit]
    __laboratorySampleSplitRatio: LaboratorySampleSplitRatio
    __laboratoryAccreditationIndicator: LaboratoryAccreditationIndicator
    __laboratoryAccreditationAuthorityName: LaboratoryAccreditationAuthorityName
    __taxonomistAccreditationIndicator: TaxonomistAccreditationIndicator
    __taxonomistAccreditationAuthorityName: TaxonomistAccreditationAuthorityName

    def __init__(
        self,
        o: dict = None,
        *,
        laboratoryName: LaboratoryName = None,
        analysisStartDate: AnalysisStartDate = None,
        analysisStartTime: WQXTime = None,
        analysisEndDate: AnalysisEndDate = None,
        analysisEndTime: WQXTime = None,
        laboratoryCommentText: LaboratoryCommentText = None,
        resultDetectionQuantitationLimit: DetectionQuantitationLimit = None,
        laboratorySampleSplitRatio: LaboratorySampleSplitRatio = None,
        laboratoryAccreditationIndicator: LaboratoryAccreditationIndicator = None,
        laboratoryAccreditationAuthorityName: LaboratoryAccreditationAuthorityName = None,
        taxonomistAccreditationIndicator: TaxonomistAccreditationIndicator = None,
        taxonomistAccreditationAuthorityName: TaxonomistAccreditationAuthorityName = None
    ):
        if isinstance(o, ResultLabInformation):
            # Assign attributes from object without typechecking
            self.__laboratoryName = o.laboratoryName
            self.__analysisStartDate = o.analysisStartDate
            self.__analysisStartTime = o.analysisStartTime
            self.__analysisEndDate = o.analysisEndDate
            self.__analysisEndTime = o.analysisEndTime
            self.__laboratoryCommentText = o.laboratoryCommentText
            self.__resultDetectionQuantitationLimit = o.resultDetectionQuantitationLimit
            self.__laboratorySampleSplitRatio = o.laboratorySampleSplitRatio
            self.__laboratoryAccreditationIndicator = o.laboratoryAccreditationIndicator
            self.__laboratoryAccreditationAuthorityName = (
                o.laboratoryAccreditationAuthorityName
            )
            self.__taxonomistAccreditationIndicator = o.taxonomistAccreditationIndicator
            self.__taxonomistAccreditationAuthorityName = (
                o.taxonomistAccreditationAuthorityName
            )
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.laboratoryName = o.get("laboratoryName")
            self.analysisStartDate = o.get("analysisStartDate")
            self.analysisStartTime = o.get("analysisStartTime")
            self.analysisEndDate = o.get("analysisEndDate")
            self.analysisEndTime = o.get("analysisEndTime")
            self.laboratoryCommentText = o.get("laboratoryCommentText")
            self.resultDetectionQuantitationLimit = o.get(
                "resultDetectionQuantitationLimit"
            )
            self.laboratorySampleSplitRatio = o.get("laboratorySampleSplitRatio")
            self.laboratoryAccreditationIndicator = o.get(
                "laboratoryAccreditationIndicator"
            )
            self.laboratoryAccreditationAuthorityName = o.get(
                "laboratoryAccreditationAuthorityName"
            )
            self.taxonomistAccreditationIndicator = o.get(
                "taxonomistAccreditationIndicator"
            )
            self.taxonomistAccreditationAuthorityName = o.get(
                "taxonomistAccreditationAuthorityName"
            )
        else:
            # Assign attributes from named keywords with typechecking
            self.laboratoryName = laboratoryName
            self.analysisStartDate = analysisStartDate
            self.analysisStartTime = analysisStartTime
            self.analysisEndDate = analysisEndDate
            self.analysisEndTime = analysisEndTime
            self.laboratoryCommentText = laboratoryCommentText
            self.resultDetectionQuantitationLimit = resultDetectionQuantitationLimit
            self.laboratorySampleSplitRatio = laboratorySampleSplitRatio
            self.laboratoryAccreditationIndicator = laboratoryAccreditationIndicator
            self.laboratoryAccreditationAuthorityName = (
                laboratoryAccreditationAuthorityName
            )
            self.taxonomistAccreditationIndicator = taxonomistAccreditationIndicator
            self.taxonomistAccreditationAuthorityName = (
                taxonomistAccreditationAuthorityName
            )

    @property
    def laboratoryName(self) -> LaboratoryName:
        return self.__laboratoryName

    @laboratoryName.setter
    def laboratoryName(self, val: LaboratoryName) -> None:
        self.__laboratoryName = None if val is None else LaboratoryName(val)

    @property
    def analysisStartDate(self) -> AnalysisStartDate:
        return self.__analysisStartDate

    @analysisStartDate.setter
    def analysisStartDate(self, val: AnalysisStartDate) -> None:
        self.__analysisStartDate = None if val is None else AnalysisStartDate(val)

    @property
    def analysisStartTime(self) -> WQXTime:
        """
        The local time and relative time zone when the analysis began.
        """
        return self.__analysisStartTime

    @analysisStartTime.setter
    def analysisStartTime(self, val: WQXTime) -> None:
        """
        The local time and relative time zone when the analysis began.
        """
        self.__analysisStartTime = None if val is None else WQXTime(val)

    @property
    def analysisEndDate(self) -> AnalysisEndDate:
        return self.__analysisEndDate

    @analysisEndDate.setter
    def analysisEndDate(self, val: AnalysisEndDate) -> None:
        self.__analysisEndDate = None if val is None else AnalysisEndDate(val)

    @property
    def analysisEndTime(self) -> WQXTime:
        """
        The local time and relative time zone when the analysis was finished.
        """
        return self.__analysisEndTime

    @analysisEndTime.setter
    def analysisEndTime(self, val: WQXTime) -> None:
        """
        The local time and relative time zone when the analysis was finished.
        """
        self.__analysisEndTime = None if val is None else WQXTime(val)

    @property
    def laboratoryCommentText(self) -> LaboratoryCommentText:
        return self.__laboratoryCommentText

    @laboratoryCommentText.setter
    def laboratoryCommentText(self, val: LaboratoryCommentText) -> None:
        self.__laboratoryCommentText = None if val is None else LaboratoryCommentText(val)

    @property
    def resultDetectionQuantitationLimit(self) -> List[DetectionQuantitationLimit]:
        """
        Information that describes one of a variety of detection or quantitation limits
        determined in a laboratory.
        """
        return self.__resultDetectionQuantitationLimit

    @resultDetectionQuantitationLimit.setter
    def resultDetectionQuantitationLimit(
        self, val: Union[DetectionQuantitationLimit, List[DetectionQuantitationLimit]]
    ) -> None:
        """
        Information that describes one of a variety of detection or quantitation limits
        determined in a laboratory.
        """
        if val is None:
            self.__resultDetectionQuantitationLimit = []
        elif isinstance(val, list):
            r: List[DetectionQuantitationLimit] = []
            for x in val:
                r.append(DetectionQuantitationLimit(x))
            self.__resultDetectionQuantitationLimit = r
        else:
            self.__resultDetectionQuantitationLimit = [DetectionQuantitationLimit(val)]

    @property
    def laboratorySampleSplitRatio(self) -> LaboratorySampleSplitRatio:
        return self.__laboratorySampleSplitRatio

    @laboratorySampleSplitRatio.setter
    def laboratorySampleSplitRatio(self, val: LaboratorySampleSplitRatio) -> None:
        self.__laboratorySampleSplitRatio = (
            None if val is None else LaboratorySampleSplitRatio(val)
        )

    @property
    def laboratoryAccreditationIndicator(self) -> LaboratoryAccreditationIndicator:
        return self.__laboratoryAccreditationIndicator

    @laboratoryAccreditationIndicator.setter
    def laboratoryAccreditationIndicator(
        self, val: LaboratoryAccreditationIndicator
    ) -> None:
        self.__laboratoryAccreditationIndicator = (
            None if val is None else LaboratoryAccreditationIndicator(val)
        )

    @property
    def laboratoryAccreditationAuthorityName(
        self,
    ) -> LaboratoryAccreditationAuthorityName:
        return self.__laboratoryAccreditationAuthorityName

    @laboratoryAccreditationAuthorityName.setter
    def laboratoryAccreditationAuthorityName(
        self, val: LaboratoryAccreditationAuthorityName
    ) -> None:
        self.__laboratoryAccreditationAuthorityName = (
            None if val is None else LaboratoryAccreditationAuthorityName(val)
        )

    @property
    def taxonomistAccreditationIndicator(self) -> TaxonomistAccreditationIndicator:
        return self.__taxonomistAccreditationIndicator

    @taxonomistAccreditationIndicator.setter
    def taxonomistAccreditationIndicator(
        self, val: TaxonomistAccreditationIndicator
    ) -> None:
        self.__taxonomistAccreditationIndicator = (
            None if val is None else TaxonomistAccreditationIndicator(val)
        )

    @property
    def taxonomistAccreditationAuthorityName(
        self,
    ) -> TaxonomistAccreditationAuthorityName:
        return self.__taxonomistAccreditationAuthorityName

    @taxonomistAccreditationAuthorityName.setter
    def taxonomistAccreditationAuthorityName(
        self, val: TaxonomistAccreditationAuthorityName
    ) -> None:
        self.__taxonomistAccreditationAuthorityName = (
            None if val is None else TaxonomistAccreditationAuthorityName(val)
        )

    def generateXML(self, name: str = "ResultLabInformation") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__laboratoryName is not None:
                line("LaboratoryName", self.__laboratoryName)
            if self.__analysisStartDate is not None:
                line("AnalysisStartDate", self.__analysisStartDate)
            if self.__analysisStartTime is not None:
                asis(self.__analysisStartTime.generateXML("AnalysisStartTime"))
            if self.__analysisEndDate is not None:
                line("AnalysisEndDate", self.__analysisEndDate)
            if self.__analysisEndTime is not None:
                asis(self.__analysisEndTime.generateXML("AnalysisEndTime"))
            if self.__laboratoryCommentText is not None:
                line("LaboratoryCommentText", self.__laboratoryCommentText)
            for x in self.__resultDetectionQuantitationLimit:
                asis(x.generateXML("ResultDetectionQuantitationLimit"))
            if self.__laboratorySampleSplitRatio is not None:
                line("LaboratorySampleSplitRatio", self.__laboratorySampleSplitRatio)
            if self.__laboratoryAccreditationIndicator is not None:
                line(
                    "LaboratoryAccreditationIndicator",
                    self.__laboratoryAccreditationIndicator,
                )
            if self.__laboratoryAccreditationAuthorityName is not None:
                line(
                    "LaboratoryAccreditationAuthorityName",
                    self.__laboratoryAccreditationAuthorityName,
                )
            if self.__taxonomistAccreditationIndicator is not None:
                line(
                    "TaxonomistAccreditationIndicator",
                    self.__taxonomistAccreditationIndicator,
                )
            if self.__taxonomistAccreditationAuthorityName is not None:
                line(
                    "TaxonomistAccreditationAuthorityName",
                    self.__taxonomistAccreditationAuthorityName,
                )

        return doc.getvalue()
