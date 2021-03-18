from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import MeasureQualifierCode, MeasureUnitCode, ResultMeasureValue


class Measure:
    """
    Identifies the value, associated units of measure, and qualifier for measuring the
    observation or analytical result value.
    """

    __resultMeasureValue: ResultMeasureValue
    __measureUnitCode: MeasureUnitCode
    __measureQualifierCode: List[MeasureQualifierCode]

    def __init__(
        self,
        o: dict = None,
        *,
        resultMeasureValue: ResultMeasureValue = None,
        measureUnitCode: MeasureUnitCode = None,
        measureQualifierCode: List[MeasureQualifierCode] = None
    ):
        if isinstance(o, Measure):
            # Assign attributes from object without typechecking
            self.__resultMeasureValue = o.resultMeasureValue
            self.__measureUnitCode = o.measureUnitCode
            self.__measureQualifierCode = o.measureQualifierCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.__resultMeasureValue = o.get("resultMeasureValue")
            self.__measureUnitCode = o.get("measureUnitCode")
            self.__measureQualifierCode = o.get("measureQualifierCode", [])
        else:
            # Assign attributes from named keywords with typechecking
            self.__resultMeasureValue = resultMeasureValue
            self.__measureUnitCode = measureUnitCode
            self.__measureQualifierCode = (
                measureQualifierCode if measureQualifierCode is not None else []
            )

    @property
    def resultMeasureValue(self) -> ResultMeasureValue:
        return self.__resultMeasureValue

    @resultMeasureValue.setter
    def resultMeasureValue(self, val: ResultMeasureValue) -> None:
        self.__resultMeasureValue = None if val is None else ResultMeasureValue(val)

    @property
    def measureUnitCode(self) -> MeasureUnitCode:
        return self.__measureUnitCode

    @measureUnitCode.setter
    def measureUnitCode(self, val: MeasureUnitCode) -> None:
        self.__measureUnitCode = None if val is None else MeasureUnitCode(val)

    @property
    def measureQualifierCode(self) -> List[MeasureQualifierCode]:
        return self.__measureQualifierCode

    @measureQualifierCode.setter
    def measureQualifierCode(
        self, val: Union[MeasureQualifierCode, List[MeasureQualifierCode]]
    ) -> None:
        if val is None:
            self.__measureQualifierCode = []
        elif isinstance(val, list):
            r: List[MeasureQualifierCode] = []
            for x in val:
                r.append(MeasureQualifierCode(x))
            self.__measureQualifierCode = r
        else:
            self.__measureQualifierCode = [MeasureQualifierCode(val)]

    def generateXML(self, name: str = "Measure") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__resultMeasureValue is not None:
                line("ResultMeasureValue", self.__resultMeasureValue)
            if self.__measureUnitCode is not None:
                line("MeasureUnitCode", self.__measureUnitCode)
            if len(self.__measureQualifierCode) > 6:
                raise WQXException(
                    "Attribute 'measureQualifierCode' must be a list of 0 to 6 "
                    "MeasureQualifierCode objects."
                )
            for x in self.__measureQualifierCode:
                line("MeasureQualifierCode", x)

        return doc.getvalue()
