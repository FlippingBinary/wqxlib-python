from yattag import Doc

from ..exceptions import WQXException
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    CountryCode,
    CountyCode,
    HorizontalCollectionMethodName,
    HorizontalCoordinateReferenceSystemDatumName,
    LatitudeMeasure,
    LongitudeMeasure,
    SourceMapScale,
    StateCode,
    VerticalCollectionMethodName,
    VerticalCoordinateReferenceSystemDatumName,
)


class MonitoringLocationGeospatial:
    """
    Monitoring location geographic location.
    """

    __latitudeMeasure: LatitudeMeasure
    __longitudeMeasure: LongitudeMeasure
    __sourceMapScale: SourceMapScale
    __horizontalAccuracyMeasure: MeasureCompact
    __verticalAccuracyMeasure: MeasureCompact
    __horizontalCollectionMethodName: HorizontalCollectionMethodName
    __horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName
    __verticalMeasure: MeasureCompact
    __verticalCollectionMethodName: VerticalCollectionMethodName
    __verticalCoordinateReferenceSystemDatumName: VerticalCoordinateReferenceSystemDatumName
    __countryCode: CountryCode
    __stateCode: StateCode
    __countyCode: CountyCode

    def __init__(
        self,
        o: dict = None,
        *,
        latitudeMeasure: LatitudeMeasure = None,
        longitudeMeasure: LongitudeMeasure = None,
        sourceMapScale: SourceMapScale = None,
        horizontalAccuracyMeasure: MeasureCompact = None,
        verticalAccuracyMeasure: MeasureCompact = None,
        horizontalCollectionMethodName: HorizontalCollectionMethodName = None,
        horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName = None,  # noqa: B950
        verticalMeasure: MeasureCompact = None,
        verticalCollectionMethodName: VerticalCollectionMethodName = None,
        verticalCoordinateReferenceSystemDatumName: VerticalCoordinateReferenceSystemDatumName = None,  # noqa: B950
        countryCode: CountryCode = None,
        stateCode: StateCode = None,
        countyCode: CountyCode = None
    ):
        if isinstance(o, MonitoringLocationGeospatial):
            # Assign attributes from object without typechecking
            self.__latitudeMeasure = o.latitudeMeasure
            self.__longitudeMeasure = o.longitudeMeasure
            self.__sourceMapScale = o.sourceMapScale
            self.__horizontalAccuracyMeasure = o.horizontalAccuracyMeasure
            self.__verticalAccuracyMeasure = o.verticalAccuracyMeasure
            self.__horizontalCollectionMethodName = o.horizontalCollectionMethodName
            self.__horizontalCoordinateReferenceSystemDatumName = (
                o.horizontalCoordinateReferenceSystemDatumName
            )
            self.__verticalMeasure = o.verticalMeasure
            self.__verticalCollectionMethodName = o.verticalCollectionMethodName
            self.__verticalCoordinateReferenceSystemDatumName = (
                o.verticalCoordinateReferenceSystemDatumName
            )
            self.__countryCode = o.countryCode
            self.__stateCode = o.stateCode
            self.__countyCode = o.countyCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.latitudeMeasure = o.get("latitudeMeasure")
            self.longitudeMeasure = o.get("longitudeMeasure")
            self.sourceMapScale = o.get("sourceMapScale")
            self.horizontalAccuracyMeasure = o.get("horizontalAccuracyMeasure")
            self.verticalAccuracyMeasure = o.get("verticalAccuracyMeasure")
            self.horizontalCollectionMethodName = o.get("horizontalCollectionMethodName")
            self.horizontalCoordinateReferenceSystemDatumName = o.get(
                "horizontalCoordinateReferenceSystemDatumName"
            )
            self.verticalMeasure = o.get("verticalMeasure")
            self.verticalCollectionMethodName = o.get("verticalCollectionMethodName")
            self.verticalCoordinateReferenceSystemDatumName = o.get(
                "verticalCoordinateReferenceSystemDatumName"
            )
            self.countryCode = o.get("countryCode")
            self.stateCode = o.get("stateCode")
            self.countyCode = o.get("countyCode")
        else:
            # Assign attributes from named keywords with typechecking
            self.latitudeMeasure = latitudeMeasure
            self.longitudeMeasure = longitudeMeasure
            self.sourceMapScale = sourceMapScale
            self.horizontalAccuracyMeasure = horizontalAccuracyMeasure
            self.verticalAccuracyMeasure = verticalAccuracyMeasure
            self.horizontalCollectionMethodName = horizontalCollectionMethodName
            self.horizontalCoordinateReferenceSystemDatumName = (
                horizontalCoordinateReferenceSystemDatumName
            )
            self.verticalMeasure = verticalMeasure
            self.verticalCollectionMethodName = verticalCollectionMethodName
            self.verticalCoordinateReferenceSystemDatumName = (
                verticalCoordinateReferenceSystemDatumName
            )
            self.countryCode = countryCode
            self.stateCode = stateCode
            self.countyCode = countyCode

    @property
    def latitudeMeasure(self) -> LatitudeMeasure:
        return self.__latitudeMeasure

    @latitudeMeasure.setter
    def latitudeMeasure(self, val: LatitudeMeasure) -> None:
        self.__latitudeMeasure = None if val is None else LatitudeMeasure(val)

    @property
    def longitudeMeasure(self) -> LongitudeMeasure:
        return self.__longitudeMeasure

    @longitudeMeasure.setter
    def longitudeMeasure(self, val: LongitudeMeasure) -> None:
        self.__longitudeMeasure = None if val is None else LongitudeMeasure(val)

    @property
    def sourceMapScale(self) -> SourceMapScale:
        return self.__sourceMapScale

    @sourceMapScale.setter
    def sourceMapScale(self, val: SourceMapScale) -> None:
        self.__sourceMapScale = None if val is None else SourceMapScale(val)

    @property
    def horizontalAccuracyMeasure(self) -> MeasureCompact:
        """
        The horizontal measure of the relative accuracy of the latitude and longitude
        coordinates.
        """
        return self.__horizontalAccuracyMeasure

    @horizontalAccuracyMeasure.setter
    def horizontalAccuracyMeasure(self, val: MeasureCompact) -> None:
        """
        The horizontal measure of the relative accuracy of the latitude and longitude
        coordinates.
        """
        self.__horizontalAccuracyMeasure = None if val is None else MeasureCompact(val)

    @property
    def verticalAccuracyMeasure(self) -> MeasureCompact:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling.
        """
        return self.__verticalAccuracyMeasure

    @verticalAccuracyMeasure.setter
    def verticalAccuracyMeasure(self, val: MeasureCompact) -> None:
        """
        Depth below land surface datum (LSD) to the bottom of the hole on completion of
        drilling.
        """
        self.__verticalAccuracyMeasure = None if val is None else MeasureCompact(val)

    @property
    def horizontalCollectionMethodName(self) -> HorizontalCollectionMethodName:
        return self.__horizontalCollectionMethodName

    @horizontalCollectionMethodName.setter
    def horizontalCollectionMethodName(self, val: HorizontalCollectionMethodName) -> None:
        self.__horizontalCollectionMethodName = (
            None if val is None else HorizontalCollectionMethodName(val)
        )

    @property
    def horizontalCoordinateReferenceSystemDatumName(
        self,
    ) -> HorizontalCoordinateReferenceSystemDatumName:
        return self.__horizontalCoordinateReferenceSystemDatumName

    @horizontalCoordinateReferenceSystemDatumName.setter
    def horizontalCoordinateReferenceSystemDatumName(
        self, val: HorizontalCoordinateReferenceSystemDatumName
    ) -> None:
        self.__horizontalCoordinateReferenceSystemDatumName = (
            None if val is None else HorizontalCoordinateReferenceSystemDatumName(val)
        )

    @property
    def verticalMeasure(self) -> MeasureCompact:
        """
        The measure of elevation (i.e., the altitude), above or below a reference datum.
        """
        return self.__verticalMeasure

    @verticalMeasure.setter
    def verticalMeasure(self, val: MeasureCompact) -> None:
        """
        The measure of elevation (i.e., the altitude), above or below a reference datum.
        """
        self.__verticalMeasure = None if val is None else MeasureCompact(val)

    @property
    def verticalCollectionMethodName(self) -> VerticalCollectionMethodName:
        return self.__verticalCollectionMethodName

    @verticalCollectionMethodName.setter
    def verticalCollectionMethodName(self, val: VerticalCollectionMethodName) -> None:
        self.__verticalCollectionMethodName = (
            None if val is None else VerticalCollectionMethodName(val)
        )

    @property
    def verticalCoordinateReferenceSystemDatumName(
        self,
    ) -> VerticalCoordinateReferenceSystemDatumName:
        return self.__verticalCoordinateReferenceSystemDatumName

    @verticalCoordinateReferenceSystemDatumName.setter
    def verticalCoordinateReferenceSystemDatumName(
        self, val: VerticalCoordinateReferenceSystemDatumName
    ) -> None:
        self.__verticalCoordinateReferenceSystemDatumName = (
            None if val is None else VerticalCoordinateReferenceSystemDatumName(val)
        )

    @property
    def countryCode(self) -> CountryCode:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, val: CountryCode) -> None:
        self.__countryCode = None if val is None else CountryCode(val)

    @property
    def stateCode(self) -> StateCode:
        return self.__stateCode

    @stateCode.setter
    def stateCode(self, val: StateCode) -> None:
        self.__stateCode = None if val is None else StateCode(val)

    @property
    def countyCode(self) -> CountyCode:
        return self.__countyCode

    @countyCode.setter
    def countyCode(self, val: CountyCode) -> None:
        self.__countyCode = None if val is None else CountyCode(val)

    def generateXML(  # noqa: C901
        self, name: str = "MonitoringLocationGeospatial"
    ) -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__latitudeMeasure is None:
                raise WQXException("Attribute 'LatitudeMeasure' is required.")
            line("LatitudeMeasure", str(self.__latitudeMeasure))
            if self.__longitudeMeasure is None:
                raise WQXException("Attribute 'LongitudeMeasure' is required.")
            line("LongitudeMeasure", str(self.__longitudeMeasure))
            if self.__sourceMapScale is not None:
                line("SourceMapScale", self.__sourceMapScale)
            if self.__horizontalAccuracyMeasure is not None:
                asis(
                    self.__horizontalAccuracyMeasure.generateXML(
                        "HorizontalAccuracyMeasure"
                    )
                )
            if self.__verticalAccuracyMeasure is not None:
                asis(
                    self.__verticalAccuracyMeasure.generateXML("VerticalAccuracyMeasure")
                )
            if self.__horizontalCollectionMethodName is None:
                raise WQXException(
                    "Attribute 'HorizontalCollectionMethodName' is required."
                )
            line("HorizontalCollectionMethodName", self.__horizontalCollectionMethodName)
            if self.__horizontalCoordinateReferenceSystemDatumName is None:
                raise WQXException(
                    "Attribute 'HorizontalCoordinateReferenceSystemDatumName' is required."
                )
            line(
                "HorizontalCoordinateReferenceSystemDatumName",
                self.__horizontalCoordinateReferenceSystemDatumName,
            )
            if self.__verticalMeasure is not None:
                asis(self.__verticalMeasure.generateXML("VerticalMeasure"))
            if self.__verticalCollectionMethodName is not None:
                line("VerticalCollectionMethodName", self.__verticalCollectionMethodName)
            if self.__verticalCoordinateReferenceSystemDatumName is not None:
                line(
                    "VerticalCoordinateReferenceSystemDatumName",
                    self.__verticalCoordinateReferenceSystemDatumName,
                )
            if self.__countryCode is not None:
                line("CountryCode", self.__countryCode)
            if self.__stateCode is not None:
                line("StateCode", self.__stateCode)
            if self.__countyCode is not None:
                line("CountyCode", self.__countyCode)

        return doc.getvalue()
