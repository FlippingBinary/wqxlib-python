from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import GearProcedureUnitCode, MeasureValue


class CollectionEffort:
    """
    The fields to describe the effort used a collection.
    """

    __measureValue: MeasureValue
    __gearProcedureUnitCode: GearProcedureUnitCode

    def __init__(
        self,
        o: dict = None,
        *,
        measureValue: MeasureValue = None,
        gearProcedureUnitCode: GearProcedureUnitCode = None
    ):
        if isinstance(o, CollectionEffort):
            # Assign attributes from object without typechecking
            self.__measureValue = o.measureValue
            self.__gearProcedureUnitCode = o.gearProcedureUnitCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.measureValue = o.get("measureValue")
            self.gearProcedureUnitCode = o.get("gearProcedureUnitCode")
        else:
            # Assign attributes from named keywords with typechecking
            self.measureValue = measureValue
            self.gearProcedureUnitCode = gearProcedureUnitCode

    @property
    def measureValue(self) -> MeasureValue:
        return self.__measureValue

    @measureValue.setter
    def measureValue(self, val: MeasureValue) -> None:
        self.__measureValue = MeasureValue(val)

    @property
    def gearProcedureUnitCode(self) -> GearProcedureUnitCode:
        return self.__gearProcedureUnitCode

    @gearProcedureUnitCode.setter
    def gearProcedureUnitCode(self, val: GearProcedureUnitCode) -> None:
        self.__gearProcedureUnitCode = GearProcedureUnitCode(val)

    def generateXML(self, name: str = "CollectionEffort") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__measureValue is None:
                raise WQXException("Attribute 'measureValue' is required.")
            line("MeasureValue", self.__measureValue)
            if self.__gearProcedureUnitCode is None:
                raise WQXException("Attribute 'gearProcedureUnitCode' is required.")
            line("GearProcedureUnitCode", self.__gearProcedureUnitCode)

        return doc.getvalue()
