from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .FrequencyClassInformation import FrequencyClassInformation
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    BiologicalIndividualIdentifier,
    BiologicalIntentName,
    GroupSummaryCount,
    SampleTissueAnatomyName,
    SubjectTaxonomicName,
    SubjectTaxonomicNameUserSupplied,
    SubjectTaxonomicNameUserSuppliedReferenceText,
    UnidentifiedSpeciesIdentifier,
)
from .TaxonomicDetails import TaxonomicDetails


class BiologicalResultDescription:
    """
    Allows for the reporting of biological result information.
    """

    __biologicalIntentName: BiologicalIntentName
    __biologicalIndividualIdentifier: BiologicalIndividualIdentifier
    __subjectTaxonomicName: SubjectTaxonomicName
    __subjectTaxonomicNameUserSupplied: SubjectTaxonomicNameUserSupplied
    __subjectTaxonomicNameUserSuppliedReferenceText: SubjectTaxonomicNameUserSuppliedReferenceText
    __unidentifiedSpeciesIdentifier: UnidentifiedSpeciesIdentifier
    __sampleTissueAnatomyName: SampleTissueAnatomyName
    __groupSummaryCount: GroupSummaryCount
    __groupSummaryWeightMeasure: MeasureCompact
    __taxonomicDetails: TaxonomicDetails
    __frequencyClassInformation: List[FrequencyClassInformation]

    def __init__(
        self,
        o: dict = None,
        *,
        biologicalIntentName: BiologicalIntentName = None,
        biologicalIndividualIdentifier: BiologicalIndividualIdentifier = None,
        subjectTaxonomicName: SubjectTaxonomicName = None,
        subjectTaxonomicNameUserSupplied: SubjectTaxonomicNameUserSupplied = None,
        subjectTaxonomicNameUserSuppliedReferenceText: SubjectTaxonomicNameUserSuppliedReferenceText = None,  # noqa: B950
        unidentifiedSpeciesIdentifier: UnidentifiedSpeciesIdentifier = None,
        sampleTissueAnatomyName: SampleTissueAnatomyName = None,
        groupSummaryCount: GroupSummaryCount = None,
        groupSummaryWeightMeasure: MeasureCompact = None,
        taxonomicDetails: TaxonomicDetails = None,
        frequencyClassInformation: FrequencyClassInformation = None
    ):
        if isinstance(o, BiologicalResultDescription):
            # Assign attributes from object without typechecking
            self.__biologicalIntentName = o.biologicalIntentName
            self.__biologicalIndividualIdentifier = o.biologicalIndividualIdentifier
            self.__subjectTaxonomicName = o.subjectTaxonomicName
            self.__subjectTaxonomicNameUserSupplied = o.subjectTaxonomicNameUserSupplied
            self.__subjectTaxonomicNameUserSuppliedReferenceText = (
                o.subjectTaxonomicNameUserSuppliedReferenceText
            )
            self.__unidentifiedSpeciesIdentifier = o.unidentifiedSpeciesIdentifier
            self.__sampleTissueAnatomyName = o.sampleTissueAnatomyName
            self.__groupSummaryCount = o.groupSummaryCount
            self.__groupSummaryWeightMeasure = o.groupSummaryWeightMeasure
            self.__taxonomicDetails = o.taxonomicDetails
            self.__frequencyClassInformation = o.frequencyClassInformation
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.biologicalIntentName = o.get("biologicalIntentName")
            self.biologicalIndividualIdentifier = o.get("biologicalIndividualIdentifier")
            self.subjectTaxonomicName = o.get("subjectTaxonomicName")
            self.subjectTaxonomicNameUserSupplied = o.get(
                "subjectTaxonomicNameUserSupplied"
            )
            self.subjectTaxonomicNameUserSuppliedReferenceText = o.get(
                "subjectTaxonomicNameUserSuppliedReferenceText"
            )
            self.unidentifiedSpeciesIdentifier = o.get("unidentifiedSpeciesIdentifier")
            self.sampleTissueAnatomyName = o.get("sampleTissueAnatomyName")
            self.groupSummaryCount = o.get("groupSummaryCount")
            self.groupSummaryWeightMeasure = o.get("groupSummaryWeightMeasure")
            self.taxonomicDetails = o.get("taxonomicDetails")
            self.frequencyClassInformation = o.get("frequencyClassInformation")
        else:
            # Assign attributes from named keywords with typechecking
            self.biologicalIntentName = biologicalIntentName
            self.biologicalIndividualIdentifier = biologicalIndividualIdentifier
            self.subjectTaxonomicName = subjectTaxonomicName
            self.subjectTaxonomicNameUserSupplied = subjectTaxonomicNameUserSupplied
            self.subjectTaxonomicNameUserSuppliedReferenceText = (
                subjectTaxonomicNameUserSuppliedReferenceText
            )
            self.unidentifiedSpeciesIdentifier = unidentifiedSpeciesIdentifier
            self.sampleTissueAnatomyName = sampleTissueAnatomyName
            self.groupSummaryCount = groupSummaryCount
            self.groupSummaryWeightMeasure = groupSummaryWeightMeasure
            self.taxonomicDetails = taxonomicDetails
            self.frequencyClassInformation = frequencyClassInformation

    @property
    def biologicalIntentName(self) -> BiologicalIntentName:
        return self.__biologicalIntentName

    @biologicalIntentName.setter
    def biologicalIntentName(self, val: BiologicalIntentName) -> None:
        self.__biologicalIntentName = None if val is None else BiologicalIntentName(val)

    @property
    def biologicalIndividualIdentifier(self) -> BiologicalIndividualIdentifier:
        return self.__biologicalIndividualIdentifier

    @biologicalIndividualIdentifier.setter
    def biologicalIndividualIdentifier(self, val: BiologicalIndividualIdentifier) -> None:
        self.__biologicalIndividualIdentifier = (
            None if val is None else BiologicalIndividualIdentifier(val)
        )

    @property
    def subjectTaxonomicName(self) -> SubjectTaxonomicName:
        return self.__subjectTaxonomicName

    @subjectTaxonomicName.setter
    def subjectTaxonomicName(self, val: SubjectTaxonomicName) -> None:
        self.__subjectTaxonomicName = None if val is None else SubjectTaxonomicName(val)

    @property
    def subjectTaxonomicNameUserSupplied(self) -> SubjectTaxonomicNameUserSupplied:
        return self.__subjectTaxonomicNameUserSupplied

    @subjectTaxonomicNameUserSupplied.setter
    def subjectTaxonomicNameUserSupplied(
        self, val: SubjectTaxonomicNameUserSupplied
    ) -> None:
        self.__subjectTaxonomicNameUserSupplied = (
            None if val is None else SubjectTaxonomicNameUserSupplied(val)
        )

    @property
    def subjectTaxonomicNameUserSuppliedReferenceText(
        self,
    ) -> SubjectTaxonomicNameUserSuppliedReferenceText:
        return self.__subjectTaxonomicNameUserSuppliedReferenceText

    @subjectTaxonomicNameUserSuppliedReferenceText.setter
    def subjectTaxonomicNameUserSuppliedReferenceText(
        self, val: SubjectTaxonomicNameUserSuppliedReferenceText
    ) -> None:
        self.__subjectTaxonomicNameUserSuppliedReferenceText = (
            None if val is None else SubjectTaxonomicNameUserSuppliedReferenceText(val)
        )

    @property
    def unidentifiedSpeciesIdentifier(self) -> UnidentifiedSpeciesIdentifier:
        return self.__unidentifiedSpeciesIdentifier

    @unidentifiedSpeciesIdentifier.setter
    def unidentifiedSpeciesIdentifier(self, val: UnidentifiedSpeciesIdentifier) -> None:
        self.__unidentifiedSpeciesIdentifier = (
            None if val is None else UnidentifiedSpeciesIdentifier(val)
        )

    @property
    def sampleTissueAnatomyName(self) -> SampleTissueAnatomyName:
        return self.__sampleTissueAnatomyName

    @sampleTissueAnatomyName.setter
    def sampleTissueAnatomyName(self, val: SampleTissueAnatomyName) -> None:
        self.__sampleTissueAnatomyName = (
            None if val is None else SampleTissueAnatomyName(val)
        )

    @property
    def groupSummaryCount(self) -> GroupSummaryCount:
        """
        Captures the total count or total sample weight for a Group Summary.
        """
        return self.__groupSummaryCount

    @groupSummaryCount.setter
    def groupSummaryCount(self, val: GroupSummaryCount) -> None:
        """
        Captures the total count or total sample weight for a Group Summary.
        """
        self.__groupSummaryCount = None if val is None else GroupSummaryCount(val)

    @property
    def groupSummaryWeightMeasure(self) -> MeasureCompact:
        return self.__groupSummaryWeightMeasure

    @groupSummaryWeightMeasure.setter
    def groupSummaryWeightMeasure(self, val: MeasureCompact) -> None:
        self.__groupSummaryWeightMeasure = None if val is None else MeasureCompact(val)

    @property
    def taxonomicDetails(self) -> TaxonomicDetails:
        return self.__taxonomicDetails

    @taxonomicDetails.setter
    def taxonomicDetails(self, val: TaxonomicDetails) -> None:
        self.__taxonomicDetails = None if val is None else TaxonomicDetails(val)

    @property
    def frequencyClassInformation(self) -> FrequencyClassInformation:
        return self.__frequencyClassInformation

    @frequencyClassInformation.setter
    def frequencyClassInformation(
        self, val: Union[FrequencyClassInformation, List[FrequencyClassInformation]]
    ) -> None:
        if val is None:
            self.__frequencyClassInformation = []
        elif isinstance(val, list):
            r: List[FrequencyClassInformation] = []
            for x in val:
                r.append(FrequencyClassInformation(x))
            self.__frequencyClassInformation = r
        else:
            self.__frequencyClassInformation = [FrequencyClassInformation(val)]

    def generateXML(self, name: str = "BiologicalResultDescription") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__biologicalIntentName is None:
                raise WQXException("Attribute 'biologicalIntentName' is required.")
            line("BiologicalIntentName", self.__biologicalIntentName)
            if self.__biologicalIndividualIdentifier is not None:
                line(
                    "BiologicalIndividualIdentifier",
                    self.__biologicalIndividualIdentifier,
                )
            if self.__subjectTaxonomicName is None:
                raise WQXException("Attribute 'subjectTaxonomicName' is required.")
            line("SubjectTaxonomicName", self.__subjectTaxonomicName)
            if self.__subjectTaxonomicNameUserSupplied is not None:
                line(
                    "SubjectTaxonomicNameUserSupplied",
                    self.__subjectTaxonomicNameUserSupplied,
                )
            if self.__subjectTaxonomicNameUserSuppliedReferenceText is not None:
                line(
                    "SubjectTaxonomicNameUserSuppliedReferenceText",
                    self.__subjectTaxonomicNameUserSuppliedReferenceText,
                )
            if self.__unidentifiedSpeciesIdentifier is not None:
                line(
                    "UnidentifiedSpeciesIdentifier", self.__unidentifiedSpeciesIdentifier,
                )
            if self.__sampleTissueAnatomyName is not None:
                line("SampleTissueAnatomyName", self.__sampleTissueAnatomyName)
            if self.__groupSummaryCount is not None:
                line("GroupSummaryCount", self.__groupSummaryCount)
            if self.__groupSummaryWeightMeasure is not None:
                asis(
                    self.__groupSummaryWeightMeasure.generateXML(
                        "GroupSummaryWeightMeasure"
                    )
                )
            if self.__taxonomicDetails is not None:
                asis(self.__taxonomicDetails.generateXML("TaxonomicDetails"))
            if len(self.__frequencyClassInformation) > 3:
                raise WQXException(
                    "Attribute frequencyClassInformation must be a list of 0 to 3 "
                    "FrequencyClassInformation objects."
                )
            for x in self.__frequencyClassInformation:
                asis(x.generateXML("FrequencyClassInformation"))

        return doc.getvalue()
