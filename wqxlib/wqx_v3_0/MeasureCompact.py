from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import MeasureUnitCode, MeasureValue


class MeasureCompact:
    """
    Identifies only the value and the associated units of measure for measuring the
    observation or analytical result value.
    """

    __measureValue: MeasureValue
    __measureUnitCode: MeasureUnitCode

    def __init__(
        self,
        o: dict = None,
        *,
        measureValue: MeasureValue = None,
        measureUnitCode: MeasureUnitCode = None
    ):
        if isinstance(o, MeasureCompact):
            # Assign attributes from object without typechecking
            self.__measureValue = o.measureValue
            self.__measureUnitCode = o.measureUnitCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.measureValue = o.get("measureValue")
            self.measureUnitCode = o.get("measureUnitCode")
        else:
            # Assign attributes from named keywords with typechecking
            self.measureValue = measureValue
            self.measureUnitCode = measureUnitCode

    @property
    def measureValue(self) -> MeasureValue:
        return self.__measureValue

    @measureValue.setter
    def measureValue(self, val: MeasureValue) -> None:
        self.__measureValue = None if val is None else MeasureValue(val)

    @property
    def measureUnitCode(self) -> MeasureUnitCode:
        return self.__measureUnitCode

    @measureUnitCode.setter
    def measureUnitCode(self, val: MeasureUnitCode) -> None:
        self.__measureUnitCode = None if val is None else MeasureUnitCode(val)

    def generateXML(self, name: str = "MeasureCompact") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__measureValue is None:
                raise WQXException("Attribute 'measureValue' is required.")
            line("MeasureValue", self.__measureValue)
            if self.__measureUnitCode is None:
                raise WQXException("Attribute 'measureUnitCode' is required.")
            line("MeasureUnitCode", self.__measureUnitCode)

        return doc.getvalue()
