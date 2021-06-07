from typing import List

from .wqx_v3_0 import (
    Measure,
    MeasureCompact,
    MeasureQualifierCode,
    MeasureUnitCode,
    MeasureValue,
    Result,
    ResultDescription,
    ResultLabInformation,
    ResultMeasureValue,
)


class WQXResult(Result, ResultDescription, ResultLabInformation):
    def __init__(self,):
        ResultLabInformation.__init__(self)
        ResultDescription.__init__(self)
        Result.__init__(self)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass  # TODO: add rule test

    @property
    def resultMeasureValue(self) -> ResultMeasureValue:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        val = Measure(self.resultMeasure)
        return val.resultMeasureValue

    @resultMeasureValue.setter
    def resultMeasureValue(self, val: str) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        tmp = Measure(self.resultMeasure)
        if tmp is None:
            self.resultMeasure = Measure(resultMeasureValue=val)
        else:
            if val is None:
                tmp.resultMeasureValue = None
            else:
                tmp.resultMeasureValue = val
            self.resultMeasure = tmp

    @property
    def resultMeasureUnitCode(self) -> MeasureUnitCode:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        val = Measure(self.resultMeasure)
        return val.measureUnitCode

    @resultMeasureUnitCode.setter
    def resultMeasureUnitCode(self, val: MeasureUnitCode) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        tmp = Measure(self.resultMeasure)
        if tmp is None:
            self.resultMeasure = Measure(measureUnitCode=val)
        else:
            if val is None:
                tmp.measureUnitCode = None
            else:
                tmp.measureUnitCode = val
            self.resultMeasure = tmp

    @property
    def resultMeasureQualifierCode(self) -> MeasureQualifierCode:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        val = Measure(self.resultMeasure)
        return val.measureQualifierCode

    @resultMeasureQualifierCode.setter
    def resultMeasureQualifierCode(self, val: List[MeasureQualifierCode]) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        tmp = Measure(self.resultMeasure)
        if tmp is None:
            self.resultMeasure = Measure(measureQualifierCode=val)
        else:
            if val is None:
                tmp.measureQualifierCode = None
            else:
                tmp.measureQualifierCode = val
            self.resultMeasure = tmp

    @property
    def resultDepthHeightMeasureValue(self) -> MeasureValue:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        val = MeasureCompact(self.resultDepthHeightMeasure)
        return val.measureValue

    @resultDepthHeightMeasureValue.setter
    def resultDepthHeightMeasureValue(self, val: str) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        tmp = MeasureCompact(self.resultDepthHeightMeasure)
        if val is None:
            tmp.measureValue = None
        else:
            tmp.measureValue = val
        self.resultDepthHeightMeasure = tmp

    @property
    def resultDepthHeightMeasureUnitCode(self) -> MeasureUnitCode:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        val = MeasureCompact(self.resultDepthHeightMeasure)
        return val.measureUnitCode

    @resultDepthHeightMeasureUnitCode.setter
    def resultDepthHeightMeasureUnitCode(self, val: MeasureUnitCode) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        tmp = MeasureCompact(self.resultDepthHeightMeasure)
        if val is None:
            tmp.measureUnitCode = None
        else:
            tmp.measureUnitCode = val
        self.resultDepthHeightMeasure = tmp
