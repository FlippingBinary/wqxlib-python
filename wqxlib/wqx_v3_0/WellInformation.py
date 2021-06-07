from yattag import Doc

from ..exceptions import WQXException
from .AquiferInformation import AquiferInformation
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    AquiferTypeName,
    ConstructionDate,
    FormationTypeText,
    NationalAquiferCode,
    WellTypeText,
)


class WellInformation:
    """
    Description of the attributes of a well.
    """

    __wellTypeText: WellTypeText
    __aquiferTypeName: AquiferTypeName
    __nationalAquiferCode: NationalAquiferCode
    __aquiferInformation: AquiferInformation
    __formationTypeText: FormationTypeText
    __wellHoleDepthMeasure: MeasureCompact
    __constructionDate: ConstructionDate
    __wellDepthMeasure: MeasureCompact

    def __init__(
        self,
        o: dict = None,
        *,
        wellTypeText: WellTypeText = None,
        aquiferTypeName: AquiferTypeName = None,
        nationalAquiferCode: NationalAquiferCode = None,
        aquiferInformation: AquiferInformation = None,
        formationTypeText: FormationTypeText = None,
        wellHoleDepthMeasure: MeasureCompact = None,
        constructionDate: ConstructionDate = None,
        wellDepthMeasure: MeasureCompact = None
    ):
        if isinstance(o, WellInformation):
            # Assign attributes from object without typechecking
            self.__wellTypeText = o.wellTypeText
            self.__aquiferTypeName = o.aquiferTypeName
            self.__nationalAquiferCode = o.nationalAquiferCode
            self.__aquiferInformation = o.aquiferInformation
            self.__formationTypeText = o.formationTypeText
            self.__wellHoleDepthMeasure = o.wellHoleDepthMeasure
            self.__constructionDate = o.constructionDate
            self.__wellDepthMeasure = o.wellDepthMeasure
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.wellTypeText = o.get("wellTypeText")
            self.aquiferTypeName = o.get("aquiferTypeName")
            self.nationalAquiferCode = o.get("nationalAquiferCode")
            self.aquiferInformation = o.get("aquiferInformation")
            self.formationTypeText = o.get("formationTypeText")
            self.wellHoleDepthMeasure = o.get("wellHoleDepthMeasure")
            self.constructionDate = o.get("constructionDate")
            self.wellDepthMeasure = o.get("wellDepthMeasure")
        else:
            # Assign attributes from named keywords with typechecking
            self.wellTypeText = wellTypeText
            self.aquiferTypeName = aquiferTypeName
            self.nationalAquiferCode = nationalAquiferCode
            self.aquiferInformation = aquiferInformation
            self.formationTypeText = formationTypeText
            self.wellHoleDepthMeasure = wellHoleDepthMeasure
            self.constructionDate = constructionDate
            self.wellDepthMeasure = wellDepthMeasure

    @property
    def wellTypeText(self) -> WellTypeText:
        return self.__wellTypeText

    @wellTypeText.setter
    def wellTypeText(self, val: WellTypeText) -> None:
        self.__wellTypeText = WellTypeText(val)

    @property
    def aquiferTypeName(self) -> AquiferTypeName:
        return self.__aquiferTypeName

    @aquiferTypeName.setter
    def aquiferTypeName(self, val: AquiferTypeName) -> None:
        self.__aquiferTypeName = None if val is None else AquiferTypeName(val)

    @property
    def nationalAquiferCode(self) -> NationalAquiferCode:
        return self.__nationalAquiferCode

    @nationalAquiferCode.setter
    def nationalAquiferCode(self, val: NationalAquiferCode) -> None:
        self.__nationalAquiferCode = None if val is None else NationalAquiferCode(val)

    @property
    def aquiferInformation(self) -> AquiferInformation:
        return self.__aquiferInformation

    @aquiferInformation.setter
    def aquiferInformation(self, val: AquiferInformation) -> None:
        self.__aquiferInformation = None if val is None else AquiferInformation(val)

    @property
    def formationTypeText(self) -> FormationTypeText:
        return self.__formationTypeText

    @formationTypeText.setter
    def formationTypeText(self, val: FormationTypeText) -> None:
        self.__formationTypeText = None if val is None else FormationTypeText(val)

    @property
    def wellHoleDepthMeasure(self) -> MeasureCompact:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling.
        """
        return self.__wellHoleDepthMeasure

    @wellHoleDepthMeasure.setter
    def wellHoleDepthMeasure(self, val: MeasureCompact) -> None:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling.
        """
        self.__wellHoleDepthMeasure = None if val is None else MeasureCompact(val)

    @property
    def constructionDate(self) -> ConstructionDate:
        return self.__constructionDate

    @constructionDate.setter
    def constructionDate(self, val: ConstructionDate) -> None:
        self.__constructionDate = None if val is None else ConstructionDate(val)

    @property
    def wellDepthMeasure(self) -> MeasureCompact:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling. ie. completion depth
        """
        return self.__wellDepthMeasure

    @wellDepthMeasure.setter
    def wellDepthMeasure(self, val: MeasureCompact) -> None:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling. ie. completion depth
        """
        self.__wellDepthMeasure = None if val is None else MeasureCompact(val)

    def generateXML(self, name: str = "WellInformation") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__wellTypeText is None:
                raise WQXException("Attribute 'wellTypeText' is required.")
            line("WellTypeText", self.__wellTypeText)
            if self.__aquiferTypeName is not None:
                line("AquiferTypeName", self.__aquiferTypeName)
            if self.__nationalAquiferCode is not None:
                line("NationalAquiferCode", self.__nationalAquiferCode)
            if self.__aquiferInformation is not None:
                asis(self.__aquiferInformation.generateXML("AquiferInformation"))
            if self.__formationTypeText is not None:
                line("FormationTypeText", self.__formationTypeText)
            if self.__wellHoleDepthMeasure is not None:
                asis(self.__wellHoleDepthMeasure.generateXML("WellHoleDepthMeasure"))
            if self.__constructionDate is not None:
                line("ConstructionDate", self.__constructionDate)
            if self.__wellDepthMeasure is not None:
                asis(self.__wellDepthMeasure.generateXML("WellDepthMeasure"))

        return doc.getvalue()
