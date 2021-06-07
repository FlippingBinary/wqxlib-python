from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .BibliographicReference import BibliographicReference
from .SimpleContent import (
    CellFormName,
    CellShapeName,
    FunctionalFeedingGroupName,
    HabitName,
    TaxonomicPollutionTolerance,
    TaxonomicPollutionToleranceScaleText,
    TrophicLevelName,
    VoltinismName,
)


class TaxonomicDetails:
    """
    This section allows for the further definition of user-defined details for taxa.
    """

    __cellFormName: CellFormName
    __cellShapeName: CellShapeName
    __habitName: HabitName
    __voltinismName: VoltinismName
    __taxonomicPollutionTolerance: TaxonomicPollutionTolerance
    __taxonomicPollutionToleranceScaleText: TaxonomicPollutionToleranceScaleText
    __trophicLevelName: TrophicLevelName
    __functionalFeedingGroupName: FunctionalFeedingGroupName
    __taxonomicDetailsCitation: BibliographicReference

    def __init__(
        self,
        o: dict = None,
        *,
        cellFormName: CellFormName = None,
        cellShapeName: CellShapeName = None,
        habitName: HabitName = None,
        voltinismName: VoltinismName = None,
        taxonomicPollutionTolerance: TaxonomicPollutionTolerance = None,
        taxonomicPollutionToleranceScaleText: TaxonomicPollutionToleranceScaleText = None,
        trophicLevelName: TrophicLevelName = None,
        functionalFeedingGroupName: FunctionalFeedingGroupName = None,
        taxonomicDetailsCitation: BibliographicReference = None
    ):
        if isinstance(o, TaxonomicDetails):
            # Assign attributes from objects without typechecking
            self.__cellFormName = o.cellFormName
            self.__cellShapeName = o.cellShapeName
            self.__habitName = o.habitName
            self.__voltinismName = o.voltinismName
            self.__taxonomicPollutionTolerance = o.taxonomicPollutionTolerance
            self.__taxonomicPollutionToleranceScaleText = (
                o.taxonomicPollutionToleranceScaleText
            )
            self.__trophicLevelName = o.trophicLevelName
            self.__functionalFeedingGroupName = o.functionalFeedingGroupName
            self.__taxonomicDetailsCitation = o.taxonomicDetailsCitation
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.cellFormName = o.get("cellFormName")
            self.cellShapeName = o.get("cellShapeName")
            self.habitName = o.get("habitName")
            self.voltinismName = o.get("voltinismName")
            self.taxonomicPollutionTolerance = o.get("taxonomicPollutionTolerance")
            self.taxonomicPollutionToleranceScaleText = o.get(
                "taxonomicPollutionToleranceScaleText"
            )
            self.trophicLevelName = o.get("trophicLevelName")
            self.functionalFeedingGroupName = o.get("functionalFeedingGroupName")
            self.taxonomicDetailsCitation = o.get("taxonomicDetailsCitation")
        else:
            # Assign attributes from named keywords with typechecking
            self.cellFormName = cellFormName
            self.cellShapeName = cellShapeName
            self.habitName = habitName
            self.voltinismName = voltinismName
            self.taxonomicPollutionTolerance = taxonomicPollutionTolerance
            self.taxonomicPollutionToleranceScaleText = (
                taxonomicPollutionToleranceScaleText
            )
            self.trophicLevelName = trophicLevelName
            self.functionalFeedingGroupName = functionalFeedingGroupName
            self.taxonomicDetailsCitation = taxonomicDetailsCitation

    @property
    def cellFormName(self) -> CellFormName:
        return self.__cellFormName

    @cellFormName.setter
    def cellFormName(self, val: CellFormName) -> None:
        self.__cellFormName = None if val is None else CellFormName(val)

    @property
    def cellShapeName(self) -> CellShapeName:
        return self.__cellShapeName

    @cellShapeName.setter
    def cellShapeName(self, val: CellShapeName) -> None:
        self.__cellShapeName = None if val is None else CellShapeName(val)

    @property
    def habitName(self) -> HabitName:
        return self.__habitName

    @habitName.setter
    def habitName(self, val: Union[HabitName, List[HabitName]]) -> None:
        if val is None:
            self.__habitName = []
        elif isinstance(val, list):
            r: List[HabitName] = []
            for x in val:
                r.append(HabitName(x))
            self.__habitName = r
        else:
            self.__habitName = [HabitName(val)]

    @property
    def voltinismName(self) -> VoltinismName:
        return self.__voltinismName

    @voltinismName.setter
    def voltinismName(self, val: VoltinismName) -> None:
        self.__voltinismName = None if val is None else VoltinismName(val)

    @property
    def taxonomicPollutionTolerance(self) -> TaxonomicPollutionTolerance:
        return self.__taxonomicPollutionTolerance

    @taxonomicPollutionTolerance.setter
    def taxonomicPollutionTolerance(self, val: TaxonomicPollutionTolerance) -> None:
        self.__taxonomicPollutionTolerance = (
            None if val is None else TaxonomicPollutionTolerance(val)
        )

    @property
    def taxonomicPollutionToleranceScaleText(
        self,
    ) -> TaxonomicPollutionToleranceScaleText:
        return self.__taxonomicPollutionToleranceScaleText

    @taxonomicPollutionToleranceScaleText.setter
    def taxonomicPollutionToleranceScaleText(
        self, val: TaxonomicPollutionToleranceScaleText
    ) -> None:
        self.__taxonomicPollutionToleranceScaleText = (
            None if val is None else TaxonomicPollutionToleranceScaleText(val)
        )

    @property
    def trophicLevelName(self) -> TrophicLevelName:
        return self.__trophicLevelName

    @trophicLevelName.setter
    def trophicLevelName(self, val: TrophicLevelName) -> None:
        self.__trophicLevelName = None if val is None else TrophicLevelName(val)

    @property
    def functionalFeedingGroupName(self) -> FunctionalFeedingGroupName:
        return self.__functionalFeedingGroupName

    @functionalFeedingGroupName.setter
    def functionalFeedingGroupName(
        self, val: Union[FunctionalFeedingGroupName, List[FunctionalFeedingGroupName]]
    ) -> None:
        if val is None:
            self.__functionalFeedingGroupName = []
        elif isinstance(val, list):
            r: List[FunctionalFeedingGroupName] = []
            for x in val:
                r.append(FunctionalFeedingGroupName(x))
            self.__functionalFeedingGroupName = r
        else:
            self.__functionalFeedingGroupName = [FunctionalFeedingGroupName(val)]

    @property
    def taxonomicDetailsCitation(self) -> BibliographicReference:
        return self.__taxonomicDetailsCitation

    @taxonomicDetailsCitation.setter
    def taxonomicDetailsCitation(self, val: BibliographicReference) -> None:
        self.__taxonomicDetailsCitation = (
            None if val is None else BibliographicReference(val)
        )

    def generateXML(self, name: str = "TaxonomicDetails") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__cellFormName is not None:
                line("CellFormName", self.__cellFormName)
            if self.__cellShapeName is not None:
                line("CellShapeName", self.__cellShapeName)
            if len(self.__habitName) > 3:
                raise WQXException(
                    "Attribute 'habitName' must be a list of 0 to 3 HabitName objects."
                )
            for x in self.__habitName:
                line("HabitName", x)
            if self.__voltinismName is not None:
                line("VoltinismName", self.__voltinismName)
            if self.__taxonomicPollutionTolerance is not None:
                line("TaxonomicPollutionTolerance", self.__taxonomicPollutionTolerance)
            if self.__taxonomicPollutionToleranceScaleText is not None:
                line(
                    "TaxonomicPollutionToleranceScaleText",
                    self.__taxonomicPollutionToleranceScaleText,
                )
            if self.__trophicLevelName is not None:
                line("TrophicLevelName", self.__trophicLevelName)
            if len(self.__functionalFeedingGroupName) > 3:
                raise WQXException(
                    "Attribute 'functionalFeedingGroupName' must be a list of 0 to 3 "
                    "FunctionalFeedingGroupName objects."
                )
            for x in self.__functionalFeedingGroupName:
                line("FunctionalFeedingGroupName", x)
            if self.__taxonomicDetailsCitation is not None:
                asis(
                    self.__taxonomicDetailsCitation.generateXML(
                        "TaxonomicDetailsCitation"
                    )
                )

        return doc.getvalue()
