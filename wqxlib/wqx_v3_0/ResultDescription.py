from yattag import Doc

from .DataQualityIndicator import DataQuality
from .Measure import Measure
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    CharacteristicName,
    CharacteristicNameUserSupplied,
    CommentText,
    DataLoggerLineName,
    DepthAltitudeReferencePointText,
    MethodSpeciationName,
    ProportionSampleProcessedNumeric,
    RecordIdentifierUserSupplied,
    ResultDetectionConditionText,
    ResultParticleSizeBasisText,
    ResultSampleFractionText,
    ResultSamplingPointCommentText,
    ResultSamplingPointName,
    ResultSamplingPointPlaceInSeries,
    ResultSamplingPointType,
    ResultStatusIdentifier,
    ResultTemperatureBasisText,
    ResultTimeBasisText,
    ResultValueTypeName,
    ResultWeightBasisText,
    StatisticalBaseCode,
    StatisticalNValueNumeric,
    TargetCount,
)


class ResultDescription:
    """
    Describes the results of a field measurement, observation, or laboratory analysis.
    """

    __dataLoggerLineName: DataLoggerLineName
    __resultDetectionConditionText: ResultDetectionConditionText
    __characteristicName: CharacteristicName
    __characteristicNameUserSupplied: CharacteristicNameUserSupplied
    __methodSpeciationName: MethodSpeciationName
    __resultSampleFractionText: ResultSampleFractionText
    __resultMeasure: Measure
    __targetCount: TargetCount
    __proportionSampleProcessedNumeric: ProportionSampleProcessedNumeric
    __resultStatusIdentifier: ResultStatusIdentifier
    __statisticalBaseCode: StatisticalBaseCode
    __statisticalNValueNumeric: StatisticalNValueNumeric
    __resultValueTypeName: ResultValueTypeName
    __resultWeightBasisText: ResultWeightBasisText
    __resultTimeBasisText: ResultTimeBasisText
    __resultTemperatureBasisText: ResultTemperatureBasisText
    __resultParticleSizeBasisText: ResultParticleSizeBasisText
    __dataQuality: DataQuality
    __resultCommentText: CommentText
    __resultDepthHeightMeasure: MeasureCompact
    __resultDepthAltitudeReferencePointText: DepthAltitudeReferencePointText
    __resultSamplingPointName: ResultSamplingPointName
    __resultSamplingPointType: ResultSamplingPointType
    __resultSamplingPointPlaceInSeries: ResultSamplingPointPlaceInSeries
    __resultSamplingPointCommentText: ResultSamplingPointCommentText
    __recordIdentifierUserSupplied: RecordIdentifierUserSupplied

    def __init__(
        self,
        o: dict = None,
        *,
        dataLoggerLineName: DataLoggerLineName = None,
        resultDetectionConditionText: ResultDetectionConditionText = None,
        characteristicName: CharacteristicName = None,
        characteristicNameUserSupplied: CharacteristicNameUserSupplied = None,
        methodSpeciationName: MethodSpeciationName = None,
        resultSampleFractionText: ResultSampleFractionText = None,
        resultMeasure: Measure = None,
        targetCount: TargetCount = None,
        proportionSampleProcessedNumeric: ProportionSampleProcessedNumeric = None,
        resultStatusIdentifier: ResultStatusIdentifier = None,
        statisticalBaseCode: StatisticalBaseCode = None,
        statisticalNValueNumeric: StatisticalNValueNumeric = None,
        resultValueTypeName: ResultValueTypeName = None,
        resultWeightBasisText: ResultWeightBasisText = None,
        resultTimeBasisText: ResultTimeBasisText = None,
        resultTemperatureBasisText: ResultTemperatureBasisText = None,
        resultParticleSizeBasisText: ResultParticleSizeBasisText = None,
        dataQuality: DataQuality = None,
        resultCommentText: CommentText = None,
        resultDepthHeightMeasure: MeasureCompact = None,
        resultDepthAltitudeReferencePointText: DepthAltitudeReferencePointText = None,
        resultSamplingPointName: ResultSamplingPointName = None,
        resultSamplingPointType: ResultSamplingPointType = None,
        resultSamplingPointPlaceInSeries: ResultSamplingPointPlaceInSeries = None,
        resultSamplingPointCommentText: ResultSamplingPointCommentText = None,
        recordIdentifierUserSupplied: RecordIdentifierUserSupplied = None
    ):
        if isinstance(o, ResultDescription):
            # Assign attributes from object without typechecking
            self.__dataLoggerLineName = o.dataLoggerLineName
            self.__resultDetectionConditionText = o.resultDetectionConditionText
            self.__characteristicName = o.characteristicName
            self.__characteristicNameUserSupplied = o.characteristicNameUserSupplied
            self.__methodSpeciationName = o.methodSpeciationName
            self.__resultSampleFractionText = o.resultSampleFractionText
            self.__resultMeasure = o.resultMeasure
            self.__targetCount = o.targetCount
            self.__proportionSampleProcessedNumeric = o.proportionSampleProcessedNumeric
            self.__resultStatusIdentifier = o.resultStatusIdentifier
            self.__statisticalBaseCode = o.statisticalBaseCode
            self.__statisticalNValueNumeric = o.statisticalNValueNumeric
            self.__resultValueTypeName = o.resultValueTypeName
            self.__resultWeightBasisText = o.resultWeightBasisText
            self.__resultTimeBasisText = o.resultTimeBasisText
            self.__resultTemperatureBasisText = o.resultTemperatureBasisText
            self.__resultParticleSizeBasisText = o.resultParticleSizeBasisText
            self.__dataQuality = o.dataQuality
            self.__resultCommentText = o.resultCommentText
            self.__resultDepthHeightMeasure = o.resultDepthHeightMeasure
            self.__resultDepthAltitudeReferencePointText = (
                o.resultDepthAltitudeReferencePointText
            )
            self.__resultSamplingPointName = o.resultSamplingPointName
            self.__resultSamplingPointType = o.resultSamplingPointType
            self.__resultSamplingPointPlaceInSeries = o.resultSamplingPointPlaceInSeries
            self.__resultSamplingPointCommentText = o.resultSamplingPointCommentText
            self.__recordIdentifierUserSupplied = o.recordIdentifierUserSupplied
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.dataLoggerLineName = o.get("dataLoggerLineName")
            self.resultDetectionConditionText = o.get("resultDetectionConditionText")
            self.characteristicName = o.get("characteristicName")
            self.characteristicNameUserSupplied = o.get("characteristicNameUserSupplied")
            self.methodSpeciationName = o.get("methodSpeciationName")
            self.resultSampleFractionText = o.get("resultSampleFractionText")
            self.resultMeasure = o.get("resultMeasure")
            self.targetCount = o.get("targetCount")
            self.proportionSampleProcessedNumeric = o.get(
                "proportionSampleProcessedNumeric"
            )
            self.resultStatusIdentifier = o.get("resultStatusIdentifier")
            self.statisticalBaseCode = o.get("statisticalBaseCode")
            self.statisticalNValueNumeric = o.get("statisticalNValueNumeric")
            self.resultValueTypeName = o.get("resultValueTypeName")
            self.resultWeightBasisText = o.get("resultWeightBasisText")
            self.resultTimeBasisText = o.get("resultTimeBasisText")
            self.resultTemperatureBasisText = o.get("resultTemperatureBasisText")
            self.resultParticleSizeBasisText = o.get("resultParticleSizeBasisText")
            self.dataQuality = o.get("dataQuality")
            self.resultCommentText = o.get("resultCommentText")
            self.resultDepthHeightMeasure = o.get("resultDepthHeightMeasure")
            self.resultDepthAltitudeReferencePointText = o.get(
                "resultDepthAltitudeReferencePointText"
            )
            self.resultSamplingPointName = o.get("resultSamplingPointName")
            self.resultSamplingPointType = o.get("resultSamplingPointType")
            self.resultSamplingPointPlaceInSeries = o.get(
                "resultSamplingPointPlaceInSeries"
            )
            self.resultSamplingPointCommentText = o.get("resultSamplingPointCommentText")
            self.recordIdentifierUserSupplied = o.get("recordIdentifierUserSupplied")
        else:
            # Assign attributes from named keywords with typechecking
            self.dataLoggerLineName = dataLoggerLineName
            self.resultDetectionConditionText = resultDetectionConditionText
            self.characteristicName = characteristicName
            self.characteristicNameUserSupplied = characteristicNameUserSupplied
            self.methodSpeciationName = methodSpeciationName
            self.resultSampleFractionText = resultSampleFractionText
            self.resultMeasure = resultMeasure
            self.targetCount = targetCount
            self.proportionSampleProcessedNumeric = proportionSampleProcessedNumeric
            self.resultStatusIdentifier = resultStatusIdentifier
            self.statisticalBaseCode = statisticalBaseCode
            self.statisticalNValueNumeric = statisticalNValueNumeric
            self.resultValueTypeName = resultValueTypeName
            self.resultWeightBasisText = resultWeightBasisText
            self.resultTimeBasisText = resultTimeBasisText
            self.resultTemperatureBasisText = resultTemperatureBasisText
            self.resultParticleSizeBasisText = resultParticleSizeBasisText
            self.dataQuality = dataQuality
            self.resultCommentText = resultCommentText
            self.resultDepthHeightMeasure = resultDepthHeightMeasure
            self.resultDepthAltitudeReferencePointText = (
                resultDepthAltitudeReferencePointText
            )
            self.resultSamplingPointName = resultSamplingPointName
            self.resultSamplingPointType = resultSamplingPointType
            self.resultSamplingPointPlaceInSeries = resultSamplingPointPlaceInSeries
            self.resultSamplingPointCommentText = resultSamplingPointCommentText
            self.recordIdentifierUserSupplied = recordIdentifierUserSupplied

    @property
    def dataLoggerLineName(self) -> DataLoggerLineName:
        return self.__dataLoggerLineName

    @dataLoggerLineName.setter
    def dataLoggerLineName(self, val: DataLoggerLineName) -> None:
        self.__dataLoggerLineName = None if val is None else DataLoggerLineName(val)

    @property
    def resultDetectionConditionText(self) -> ResultDetectionConditionText:
        return self.__resultDetectionConditionText

    @resultDetectionConditionText.setter
    def resultDetectionConditionText(self, val: ResultDetectionConditionText) -> None:
        self.__resultDetectionConditionText = (
            None if val is None else ResultDetectionConditionText(val)
        )

    @property
    def characteristicName(self) -> CharacteristicName:
        return self.__characteristicName

    @characteristicName.setter
    def characteristicName(self, val: CharacteristicName) -> None:
        self.__characteristicName = None if val is None else CharacteristicName(val)

    @property
    def characteristicNameUserSupplied(self) -> CharacteristicNameUserSupplied:
        return self.__characteristicNameUserSupplied

    @characteristicNameUserSupplied.setter
    def characteristicNameUserSupplied(self, val: CharacteristicNameUserSupplied) -> None:
        self.__characteristicNameUserSupplied = (
            None if val is None else CharacteristicNameUserSupplied(val)
        )

    @property
    def methodSpeciationName(self) -> MethodSpeciationName:
        return self.__methodSpeciationName

    @methodSpeciationName.setter
    def methodSpeciationName(self, val: MethodSpeciationName) -> None:
        self.__methodSpeciationName = None if val is None else MethodSpeciationName(val)

    @property
    def resultSampleFractionText(self) -> ResultSampleFractionText:
        return self.__resultSampleFractionText

    @resultSampleFractionText.setter
    def resultSampleFractionText(self, val: ResultSampleFractionText) -> None:
        self.__resultSampleFractionText = (
            None if val is None else ResultSampleFractionText(val)
        )

    @property
    def resultMeasure(self) -> Measure:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        return self.__resultMeasure

    @resultMeasure.setter
    def resultMeasure(self, val: Measure) -> None:
        """
        The reportable measure of the result for the chemical, microbiological or other
        characteristic being analyzed.
        """
        self.__resultMeasure = None if val is None else Measure(val)

    @property
    def targetCount(self) -> TargetCount:
        return self.__targetCount

    @targetCount.setter
    def targetCount(self, val: TargetCount) -> None:
        self.__targetCount = None if val is None else TargetCount(val)

    @property
    def proportionSampleProcessedNumeric(self) -> ProportionSampleProcessedNumeric:
        return self.__proportionSampleProcessedNumeric

    @proportionSampleProcessedNumeric.setter
    def proportionSampleProcessedNumeric(
        self, val: ProportionSampleProcessedNumeric
    ) -> None:
        self.__proportionSampleProcessedNumeric = (
            None if val is None else ProportionSampleProcessedNumeric(val)
        )

    @property
    def resultStatusIdentifier(self) -> ResultStatusIdentifier:
        return self.__resultStatusIdentifier

    @resultStatusIdentifier.setter
    def resultStatusIdentifier(self, val: ResultStatusIdentifier) -> None:
        self.__resultStatusIdentifier = (
            None if val is None else ResultStatusIdentifier(val)
        )

    @property
    def statisticalBaseCode(self) -> StatisticalBaseCode:
        return self.__statisticalBaseCode

    @statisticalBaseCode.setter
    def statisticalBaseCode(self, val: StatisticalBaseCode) -> None:
        self.__statisticalBaseCode = None if val is None else StatisticalBaseCode(val)

    @property
    def statisticalNValueNumeric(self) -> StatisticalNValueNumeric:
        return self.__statisticalNValueNumeric

    @statisticalNValueNumeric.setter
    def statisticalNValueNumeric(self, val: StatisticalNValueNumeric) -> None:
        self.__statisticalNValueNumeric = (
            None if val is None else StatisticalNValueNumeric(val)
        )

    @property
    def resultValueTypeName(self) -> ResultValueTypeName:
        return self.__resultValueTypeName

    @resultValueTypeName.setter
    def resultValueTypeName(self, val: ResultValueTypeName) -> None:
        self.__resultValueTypeName = None if val is None else ResultValueTypeName(val)

    @property
    def resultWeightBasisText(self) -> ResultWeightBasisText:
        return self.__resultWeightBasisText

    @resultWeightBasisText.setter
    def resultWeightBasisText(self, val: ResultWeightBasisText) -> None:
        self.__resultWeightBasisText = None if val is None else ResultWeightBasisText(val)

    @property
    def resultTimeBasisText(self) -> ResultTimeBasisText:
        return self.__resultTimeBasisText

    @resultTimeBasisText.setter
    def resultTimeBasisText(self, val: ResultTimeBasisText) -> None:
        self.__resultTimeBasisText = None if val is None else ResultTimeBasisText(val)

    @property
    def resultTemperatureBasisText(self) -> ResultTemperatureBasisText:
        return self.__resultTemperatureBasisText

    @resultTemperatureBasisText.setter
    def resultTemperatureBasisText(self, val: ResultTemperatureBasisText) -> None:
        self.__resultTemperatureBasisText = (
            None if val is None else ResultTemperatureBasisText(val)
        )

    @property
    def resultParticleSizeBasisText(self) -> ResultParticleSizeBasisText:
        return self.__resultParticleSizeBasisText

    @resultParticleSizeBasisText.setter
    def resultParticleSizeBasisText(self, val: ResultParticleSizeBasisText) -> None:
        self.__resultParticleSizeBasisText = (
            None if val is None else ResultParticleSizeBasisText(val)
        )

    @property
    def dataQuality(self) -> DataQuality:
        return self.__dataQuality

    @dataQuality.setter
    def dataQuality(self, val: DataQuality) -> None:
        self.__dataQuality = None if val is None else DataQuality(val)

    @property
    def resultCommentText(self) -> CommentText:
        """
        Free text with general comments concerning the result.
        """
        return self.__resultCommentText

    @resultCommentText.setter
    def resultCommentText(self, val: CommentText) -> None:
        """
        Free text with general comments concerning the result.
        """
        self.__resultCommentText = None if val is None else CommentText(val)

    @property
    def resultDepthHeightMeasure(self) -> MeasureCompact:
        """
        A measurement of the vertical location (measured from a reference point) at which
        a result is obtained.
        """
        return self.__resultDepthHeightMeasure

    @resultDepthHeightMeasure.setter
    def resultDepthHeightMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the vertical location (measured from a reference point) at which
        a result is obtained.
        """
        self.__resultDepthHeightMeasure = None if val is None else MeasureCompact(val)

    @property
    def resultDepthAltitudeReferencePointText(self) -> DepthAltitudeReferencePointText:
        """
        The reference used to indicate the datum or reference used to establish the
        depth/altitude of a result.
        """
        return self.__resultDepthAltitudeReferencePointText

    @resultDepthAltitudeReferencePointText.setter
    def resultDepthAltitudeReferencePointText(
        self, val: DepthAltitudeReferencePointText
    ) -> None:
        """
        The reference used to indicate the datum or reference used to establish the
        depth/altitude of a result.
        """
        self.__resultDepthAltitudeReferencePointText = (
            None if val is None else DepthAltitudeReferencePointText(val)
        )

    @property
    def resultSamplingPointName(self) -> ResultSamplingPointName:
        return self.__resultSamplingPointName

    @resultSamplingPointName.setter
    def resultSamplingPointName(self, val: ResultSamplingPointName) -> None:
        self.__resultSamplingPointName = (
            None if val is None else ResultSamplingPointName(val)
        )

    @property
    def resultSamplingPointType(self) -> ResultSamplingPointType:
        return self.__resultSamplingPointType

    @resultSamplingPointType.setter
    def resultSamplingPointType(self, val: ResultSamplingPointType) -> None:
        self.__resultSamplingPointType = (
            None if val is None else ResultSamplingPointType(val)
        )

    @property
    def resultSamplingPointPlaceInSeries(self) -> ResultSamplingPointPlaceInSeries:
        return self.__resultSamplingPointPlaceInSeries

    @resultSamplingPointPlaceInSeries.setter
    def resultSamplingPointPlaceInSeries(
        self, val: ResultSamplingPointPlaceInSeries
    ) -> None:
        self.__resultSamplingPointPlaceInSeries = (
            None if val is None else ResultSamplingPointPlaceInSeries(val)
        )

    @property
    def resultSamplingPointCommentText(self) -> ResultSamplingPointCommentText:
        return self.__resultSamplingPointCommentText

    @resultSamplingPointCommentText.setter
    def resultSamplingPointCommentText(self, val: ResultSamplingPointCommentText) -> None:
        self.__resultSamplingPointCommentText = (
            None if val is None else ResultSamplingPointCommentText(val)
        )

    @property
    def recordIdentifierUserSupplied(self) -> RecordIdentifierUserSupplied:
        return self.__recordIdentifierUserSupplied

    @recordIdentifierUserSupplied.setter
    def recordIdentifierUserSupplied(self, val: RecordIdentifierUserSupplied) -> None:
        self.__recordIdentifierUserSupplied = (
            None if val is None else RecordIdentifierUserSupplied(val)
        )

    def generateXML(self, name: str = "ResultDescription") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__dataLoggerLineName is not None:
                line("DataLoggerLineName", self.__dataLoggerLineName)
            if self.__resultDetectionConditionText is not None:
                line("ResultDetectionConditionText", self.__resultDetectionConditionText)
            if self.__characteristicName is not None:
                line("CharacteristicName", self.__characteristicName)
            if self.__characteristicNameUserSupplied is not None:
                line(
                    "CharacteristicNameUserSupplied",
                    self.__characteristicNameUserSupplied,
                )
            if self.__methodSpeciationName is not None:
                line("MethodSpeciationName", self.__methodSpeciationName)
            if self.__resultSampleFractionText is not None:
                line("ResultSampleFractionText", self.__resultSampleFractionText)
            if self.__resultMeasure is not None:
                asis(self.__resultMeasure.generateXML("ResultMeasure"))
            if self.__targetCount is not None:
                line("TargetCount", self.__targetCount)
            if self.__proportionSampleProcessedNumeric is not None:
                line(
                    "ProportionSampleProcessedNumeric",
                    self.__proportionSampleProcessedNumeric,
                )
            if self.__resultStatusIdentifier is not None:
                line("ResultStatusIdentifier", self.__resultStatusIdentifier)
            if self.__statisticalBaseCode is not None:
                line("StatisticalBaseCode", self.__statisticalBaseCode)
            if self.__statisticalNValueNumeric is not None:
                line("StatisticalNValueNumeric", self.__statisticalNValueNumeric)
            if self.__resultValueTypeName is not None:
                line("ResultValueTypeName", self.__resultValueTypeName)
            if self.__resultWeightBasisText is not None:
                line("ResultWeightBasisText", self.__resultWeightBasisText)
            if self.__resultTimeBasisText is not None:
                line("ResultTimeBasisText", self.__resultTimeBasisText)
            if self.__resultTemperatureBasisText is not None:
                line("ResultTemperatureBasisText", self.__resultTemperatureBasisText)
            if self.__resultParticleSizeBasisText is not None:
                line("ResultParticleSizeBasisText", self.__resultParticleSizeBasisText)
            if self.__dataQuality is not None:
                asis(self.__dataQuality.generateXML("DataQuality"))
            if self.__resultCommentText is not None:
                line("ResultCommentText", self.__resultCommentText)
            if self.__resultDepthHeightMeasure is not None:
                asis(
                    self.__resultDepthHeightMeasure.generateXML(
                        "ResultDepthHeightMeasure"
                    )
                )
            if self.__resultDepthAltitudeReferencePointText is not None:
                line(
                    "ResultDepthAltitudeReferencePointText",
                    self.__resultDepthAltitudeReferencePointText,
                )
            if self.__resultSamplingPointName is not None:
                line("ResultSamplingPointName", self.__resultSamplingPointName)
            if self.__resultSamplingPointType is not None:
                line("ResultSamplingPointType", self.__resultSamplingPointType)
            if self.__resultSamplingPointPlaceInSeries is not None:
                line(
                    "ResultSamplingPointPlaceInSeries",
                    self.__resultSamplingPointPlaceInSeries,
                )
            if self.__resultSamplingPointCommentText is not None:
                line(
                    "ResultSamplingPointCommentText",
                    self.__resultSamplingPointCommentText,
                )
            if self.__recordIdentifierUserSupplied is not None:
                line("RecordIdentifierUserSupplied", self.__recordIdentifierUserSupplied)

        return doc.getvalue()
