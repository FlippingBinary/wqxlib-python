from yattag import Doc

from ..exceptions import WQXException
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    ActivityLocationDescriptionText,
    HorizontalCollectionMethodName,
    HorizontalCoordinateReferenceSystemDatumName,
    LatitudeMeasure,
    LongitudeMeasure,
    SourceMapScale,
)


class ActivityLocation:
    """
    Geospatial description of monitoring site, if it is different from that described in
    the station description.
    """

    __latitudeMeasure: LatitudeMeasure
    __longitudeMeasure: LongitudeMeasure
    __sourceMapScale: SourceMapScale
    __horizontalAccuracyMeasure: MeasureCompact
    __horizontalCollectionMethodName: HorizontalCollectionMethodName
    __horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName
    __activityLocationDescriptionText: ActivityLocationDescriptionText

    def __init__(
        self,
        o: dict = None,
        *,
        latitudeMeasure: LatitudeMeasure = None,
        longitudeMeasure: LongitudeMeasure = None,
        sourceMapScale: SourceMapScale = None,
        horizontalAccuracyMeasure: MeasureCompact = None,
        horizontalCollectionMethodName: HorizontalCollectionMethodName = None,
        horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName = None,  # noqa: B950
        activityLocationDescriptionText: ActivityLocationDescriptionText = None
    ):
        if isinstance(o, ActivityLocation):
            # Assign attributes from object without typechecking
            self.__latitudeMeasure = o.latitudeMeasure
            self.__longitudeMeasure = o.longitudeMeasure
            self.__sourceMapScale = o.sourceMapScale
            self.__horizontalAccuracyMeasure = o.horizontalAccuracyMeasure
            self.__horizontalCollectionMethodName = o.horizontalCollectionMethodName
            self.__horizontalCoordinateReferenceSystemDatumName = (
                o.horizontalCoordinateReferenceSystemDatumName
            )
            self.__activityLocationDescriptionText = o.activityLocationDescriptionText
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.latitudeMeasure = o.get("latitudeMeasure")
            self.longitudeMeasure = o.get("longitudeMeasure")
            self.sourceMapScale = o.get("sourceMapScale")
            self.horizontalAccuracyMeasure = o.get("horizontalAccuracyMeasure")
            self.horizontalCollectionMethodName = o.get("horizontalCollectionMethodName")
            self.horizontalCoordinateReferenceSystemDatumName = o.get(
                "horizontalCoordinateReferenceSystemDatumName"
            )
            self.activityLocationDescriptionText = o.get(
                "activityLocationDescriptionText"
            )
        else:
            # Assign attributes from named keywords with typechecking
            self.latitudeMeasure = latitudeMeasure
            self.longitudeMeasure = longitudeMeasure
            self.sourceMapScale = sourceMapScale
            self.horizontalAccuracyMeasure = horizontalAccuracyMeasure
            self.horizontalCollectionMethodName = horizontalCollectionMethodName
            self.horizontalCoordinateReferenceSystemDatumName = (
                horizontalCoordinateReferenceSystemDatumName
            )
            self.activityLocationDescriptionText = activityLocationDescriptionText

    @property
    def latitudeMeasure(self) -> LatitudeMeasure:
        return self.__latitudeMeasure

    @latitudeMeasure.setter
    def latitudeMeasure(self, val: LatitudeMeasure) -> None:
        self.__latitudeMeasure = LatitudeMeasure(val)

    @property
    def longitudeMeasure(self) -> LongitudeMeasure:
        return self.__longitudeMeasure

    @longitudeMeasure.setter
    def longitudeMeasure(self, val: LongitudeMeasure) -> None:
        self.__longitudeMeasure = LongitudeMeasure(val)

    @property
    def sourceMapScale(self) -> SourceMapScale:
        return self.__sourceMapScale

    @sourceMapScale.setter
    def sourceMapScale(self, val: SourceMapScale) -> None:
        self.__sourceMapScale = None if val is None else SourceMapScale(val)

    @property
    def horizontalAccuracyMeasure(self) -> MeasureCompact:
        return self.__horizontalAccuracyMeasure

    @horizontalAccuracyMeasure.setter
    def horizontalAccuracyMeasure(self, val: MeasureCompact) -> None:
        self.__horizontalAccuracyMeasure = None if val is None else MeasureCompact(val)

    @property
    def horizontalCollectionMethodName(self) -> HorizontalCollectionMethodName:
        return self.__horizontalCollectionMethodName

    @horizontalCollectionMethodName.setter
    def horizontalCollectionMethodName(self, val: HorizontalCollectionMethodName) -> None:
        self.__horizontalCollectionMethodName = HorizontalCollectionMethodName(val)

    @property
    def horizontalCoordinateReferenceSystemDatumName(
        self,
    ) -> HorizontalCoordinateReferenceSystemDatumName:
        return self.__horizontalCoordinateReferenceSystemDatumName

    @horizontalCoordinateReferenceSystemDatumName.setter
    def horizontalCoordinateReferenceSystemDatumName(
        self, val: HorizontalCoordinateReferenceSystemDatumName
    ) -> None:
        self.__horizontalCoordinateReferenceSystemDatumName = HorizontalCoordinateReferenceSystemDatumName(  # noqa: B950
            val
        )

    @property
    def activityLocationDescriptionText(self) -> ActivityLocationDescriptionText:
        return self.__activityLocationDescriptionText

    @activityLocationDescriptionText.setter
    def activityLocationDescriptionText(
        self, val: ActivityLocationDescriptionText
    ) -> None:
        self.__activityLocationDescriptionText = (
            None if val is None else ActivityLocationDescriptionText(val)
        )

    def generateXML(self, name: str = "ActivityLocation") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__latitudeMeasure is None:
                raise WQXException("Attribute 'latitudeMeasure' is required.")
            line("LatitudeMeasure", self.__latitudeMeasure)
            if self.__longitudeMeasure is None:
                raise WQXException("Attribute 'longitudeMeasure' is required.")
            line("LongitudeMeasure", self.__longitudeMeasure)
            if self.__sourceMapScale is not None:
                line("SourceMapScale", self.__sourceMapScale)
            if self.__horizontalAccuracyMeasure is not None:
                asis(
                    self.__horizontalAccuracyMeasure.generateXML(
                        "HorizontalAccuracyMeasure"
                    )
                )
            if self.__horizontalCollectionMethodName is None:
                raise WQXException(
                    "Attribute 'horizontalCollectionMethodName' is required."
                )
            line("HorizontalCollectionMethodName", self.__horizontalCollectionMethodName)
            if self.__horizontalCoordinateReferenceSystemDatumName is None:
                raise WQXException(
                    "Attribute 'horizontalCoordinateReferenceSystemDatumName' is required."
                )
            line(
                "HorizontalCoordinateReferenceSystemDatumName",
                self.__horizontalCoordinateReferenceSystemDatumName,
            )
            if self.__activityLocationDescriptionText is not None:
                line(
                    "ActivityLocationDescriptionText",
                    self.__activityLocationDescriptionText,
                )

        return doc.getvalue()
