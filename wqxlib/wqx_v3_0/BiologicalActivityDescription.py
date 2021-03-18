from yattag import Doc

from .BiologicalHabitatCollectionInformation import BiologicalHabitatCollectionInformation
from .SimpleContent import AssemblageSampledName, HabitatSelectionMethod, ToxicityTestType


class BiologicalActivityDescription:
    """
    Allows for the reporting of biological monitoring activities conducted at a
    Monitoring Location.
    """

    __assemblageSampledName: AssemblageSampledName
    __biologicalHabitatCollectionInformation: BiologicalHabitatCollectionInformation
    __toxicityTestType: ToxicityTestType
    __habitatSelectionMethod: HabitatSelectionMethod

    def __init__(
        self,
        o: dict = None,
        *,
        assemblageSampledName: AssemblageSampledName = None,
        biologicalHabitatCollectionInformation: BiologicalHabitatCollectionInformation = None,
        toxicityTestType: ToxicityTestType = None,
        habitatSelectionMethod: HabitatSelectionMethod = None
    ):
        if isinstance(o, BiologicalActivityDescription):
            # Assign attributes from object without typechecking
            self.__assemblageSampledName = o.assemblageSampledName
            self.__biologicalHabitatCollectionInformation = (
                o.biologicalHabitatCollectionInformation
            )
            self.__toxicityTestType = o.toxicityTestType
            self.__habitatSelectionMethod = o.habitatSelectionMethod
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.assemblageSampledName = o.get("assemblageSampledName")
            self.biologicalHabitatCollectionInformation = o.get(
                "biologicalHabitatCollectionInformation"
            )
            self.toxicityTestType = o.get("toxicityTestType")
            self.habitatSelectionMethod = o.get("habitatSelectionMethod")
        else:
            # Assign attributes from named keywords with typechecking
            self.assemblageSampledName = assemblageSampledName
            self.biologicalHabitatCollectionInformation = (
                biologicalHabitatCollectionInformation
            )
            self.toxicityTestType = toxicityTestType
            self.habitatSelectionMethod = habitatSelectionMethod

    @property
    def assemblageSampledName(self) -> AssemblageSampledName:
        return self.__assemblageSampledName

    @assemblageSampledName.setter
    def assemblageSampledName(self, val: AssemblageSampledName) -> None:
        self.__assemblageSampledName = None if val is None else AssemblageSampledName(val)

    @property
    def biologicalHabitatCollectionInformation(
        self,
    ) -> BiologicalHabitatCollectionInformation:
        return self.__biologicalHabitatCollectionInformation

    @biologicalHabitatCollectionInformation.setter
    def biologicalHabitatCollectionInformation(
        self, val: BiologicalHabitatCollectionInformation
    ) -> None:
        self.__biologicalHabitatCollectionInformation = (
            None if val is None else BiologicalHabitatCollectionInformation(val)
        )

    @property
    def toxicityTestType(self) -> ToxicityTestType:
        return self.__toxicityTestType

    @toxicityTestType.setter
    def toxicityTestType(self, val: ToxicityTestType) -> None:
        self.__toxicityTestType = None if val is None else ToxicityTestType(val)

    @property
    def habitatSelectionMethod(self) -> HabitatSelectionMethod:
        return self.__habitatSelectionMethod

    @habitatSelectionMethod.setter
    def habitatSelectionMethod(self, val: HabitatSelectionMethod) -> None:
        self.__habitatSelectionMethod = (
            None if val is None else HabitatSelectionMethod(val)
        )

    def generateXML(self, name: str = "BiologicalActivityDescription") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__assemblageSampledName is not None:
                line("AssemblageSampledName", self.__assemblageSampledName)
            if self.__biologicalHabitatCollectionInformation is not None:
                asis(
                    self.__biologicalHabitatCollectionInformation.generateXML(
                        "BiologicalHabitatCollectionInformation"
                    )
                )
            if self.__toxicityTestType is not None:
                line("ToxicityTestType", self.__toxicityTestType)
            if self.__habitatSelectionMethod is not None:
                line("HabitatSelectionMethod", self.__habitatSelectionMethod)

        return doc.getvalue()
