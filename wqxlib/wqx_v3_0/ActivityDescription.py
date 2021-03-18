from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    ActivityConductingOrganizationText,
    ActivityEndDate,
    ActivityIdentifier,
    ActivityIdentifierUserSupplied,
    ActivityMediaName,
    ActivityMediaSubdivisionName,
    ActivityRelativeDepthName,
    ActivityStartDate,
    ActivityTypeCode,
    CommentText,
    DepthAltitudeReferencePointText,
    MonitoringLocationIdentifier,
    ProjectIdentifier,
    SamplingComponentName,
)
from .WQXTime import WQXTime


class ActivityDescription:
    """
    Basic identification information for an activity conducted within a project.
    """

    __activityIdentifier: ActivityIdentifier
    __activityIdentifierUserSupplied: ActivityIdentifierUserSupplied
    __activityTypeCode: ActivityTypeCode
    __activityMediaName: ActivityMediaName
    __activityMediaSubdivisionName: ActivityMediaSubdivisionName
    __activityStartDate: ActivityStartDate
    __activityStartTime: WQXTime
    __activityEndDate: ActivityEndDate
    __activityEndTime: WQXTime
    __activityRelativeDepthName: ActivityRelativeDepthName
    __activityDepthHeightMeasure: MeasureCompact
    __activityTopDepthHeightMeasure: MeasureCompact
    __activityBottomDepthHeightMeasure: MeasureCompact
    __activityDepthAltitudeReferencePointText: DepthAltitudeReferencePointText
    __projectIdentifier: ProjectIdentifier
    __activityConductingOrganizationText: List[ActivityConductingOrganizationText]
    __monitoringLocationIdentifier: MonitoringLocationIdentifier
    __samplingComponentName: SamplingComponentName
    __activityCommentText: CommentText

    def __init__(
        self,
        o: dict = None,
        *,
        activityIdentifier: ActivityIdentifier = None,
        activityIdentifierUserSupplied: ActivityIdentifierUserSupplied = None,
        activityTypeCode: ActivityTypeCode = None,
        activityMediaName: ActivityMediaName = None,
        activityMediaSubdivisionName: ActivityMediaSubdivisionName = None,
        activityStartDate: ActivityStartDate = None,
        activityStartTime: WQXTime = None,
        activityEndDate: ActivityEndDate = None,
        activityEndTime: WQXTime = None,
        activityRelativeDepthName: ActivityRelativeDepthName = None,
        activityDepthHeightMeasure: MeasureCompact = None,
        activityTopDepthHeightMeasure: MeasureCompact = None,
        activityBottomDepthHeightMeasure: MeasureCompact = None,
        activityDepthAltitudeReferencePointText: DepthAltitudeReferencePointText = None,
        projectIdentifier: ProjectIdentifier = None,
        activityConductingOrganizationText: List[
            ActivityConductingOrganizationText
        ] = None,
        monitoringLocationIdentifier: MonitoringLocationIdentifier = None,
        samplingComponentName: SamplingComponentName = None,
        activityCommentText: CommentText = None
    ):
        if isinstance(o, ActivityDescription):
            # Assign attributes from object without typechecking
            self.__activityIdentifier = o.activityIdentifier
            self.__activityIdentifierUserSupplied = o.activityIdentifierUserSupplied
            self.__activityTypeCode = o.activityTypeCode
            self.__activityMediaName = o.activityMediaName
            self.__activityMediaSubdivisionName = o.activityMediaSubdivisionName
            self.__activityStartDate = o.activityStartDate
            self.__activityStartTime = o.activityStartTime
            self.__activityEndDate = o.activityEndDate
            self.__activityEndTime = o.activityEndTime
            self.__activityRelativeDepthName = o.activityRelativeDepthName
            self.__activityDepthHeightMeasure = o.activityDepthHeightMeasure
            self.__activityTopDepthHeightMeasure = o.activityTopDepthHeightMeasure
            self.__activityBottomDepthHeightMeasure = o.activityBottomDepthHeightMeasure
            self.__activityDepthAltitudeReferencePointText = (
                o.activityDepthAltitudeReferencePointText
            )
            self.__projectIdentifier = o.projectIdentifier
            self.__activityConductingOrganizationText = (
                o.activityConductingOrganizationText
            )
            self.__monitoringLocationIdentifier = o.monitoringLocationIdentifier
            self.__samplingComponentName = o.samplingComponentName
            self.__activityCommentText = o.activityCommentText
        elif isinstance(o, dict):
            # Assign attributes from other ActivityDescription with typechecking
            self.activityIdentifier = o.get("activityIdentifier")
            self.activityIdentifierUserSupplied = o.get("activityIdentifierUserSupplied")
            self.activityTypeCode = o.get("activityTypeCode")
            self.activityMediaName = o.get("activityMediaName")
            self.activityMediaSubdivisionName = o.get("activityMediaSubdivisionName")
            self.activityStartDate = o.get("activityStartDate")
            self.activityStartTime = o.get("activityStartTime")
            self.activityEndDate = o.get("activityEndDate")
            self.activityEndTime = o.get("activityEndTime")
            self.activityRelativeDepthName = o.get("activityRelativeDepthName")
            self.activityDepthHeightMeasure = o.get("activityDepthHeightMeasure")
            self.activityTopDepthHeightMeasure = o.get("activityTopDepthHeightMeasure")
            self.activityBottomDepthHeightMeasure = o.get(
                "activityBottomDepthHeightMeasure"
            )
            self.activityDepthAltitudeReferencePointText = o.get(
                "activityDepthAltitudeReferencePointText"
            )
            self.projectIdentifier = o.get("projectIdentifier")
            self.activityConductingOrganizationText = o.get(
                "activityConductingOrganizationText", []
            )
            self.monitoringLocationIdentifier = o.get("monitoringLocationIdentifier")
            self.samplingComponentName = o.get("samplingComponentName")
            self.activityCommentText = o.get("activityCommentText")
        else:
            # Assign attributes from named keywords with typechecking
            self.activityIdentifier = activityIdentifier
            self.activityIdentifierUserSupplied = activityIdentifierUserSupplied
            self.activityTypeCode = activityTypeCode
            self.activityMediaName = activityMediaName
            self.activityMediaSubdivisionName = activityMediaSubdivisionName
            self.activityStartDate = activityStartDate
            self.activityStartTime = activityStartTime
            self.activityEndDate = activityEndDate
            self.activityEndTime = activityEndTime
            self.activityRelativeDepthName = activityRelativeDepthName
            self.activityDepthHeightMeasure = activityDepthHeightMeasure
            self.activityTopDepthHeightMeasure = activityTopDepthHeightMeasure
            self.activityBottomDepthHeightMeasure = activityBottomDepthHeightMeasure
            self.activityDepthAltitudeReferencePointText = (
                activityDepthAltitudeReferencePointText
            )
            self.projectIdentifier = projectIdentifier
            self.activityConductingOrganizationText = activityConductingOrganizationText
            self.monitoringLocationIdentifier = monitoringLocationIdentifier
            self.samplingComponentName = samplingComponentName
            self.activityCommentText = activityCommentText

    @property
    def activityIdentifier(self) -> ActivityIdentifier:
        return self.__activityIdentifier

    @activityIdentifier.setter
    def activityIdentifier(self, val: ActivityIdentifier) -> None:
        self.__activityIdentifier = None if val is None else ActivityIdentifier(val)

    @property
    def activityIdentifierUserSupplied(self) -> ActivityIdentifierUserSupplied:
        return self.__activityIdentifierUserSupplied

    @activityIdentifierUserSupplied.setter
    def activityIdentifierUserSupplied(self, val: ActivityIdentifierUserSupplied) -> None:
        self.__activityIdentifierUserSupplied = (
            None if val is None else ActivityIdentifierUserSupplied(val)
        )

    @property
    def activityTypeCode(self) -> ActivityTypeCode:
        return self.__activityTypeCode

    @activityTypeCode.setter
    def activityTypeCode(self, val: ActivityTypeCode) -> None:
        self.__activityTypeCode = None if val is None else ActivityTypeCode(val)

    @property
    def activityMediaName(self) -> ActivityMediaName:
        return self.__activityMediaName

    @activityMediaName.setter
    def activityMediaName(self, val: ActivityMediaName) -> None:
        self.__activityMediaName = None if val is None else ActivityMediaName(val)

    @property
    def activityMediaSubdivisionName(self) -> ActivityMediaSubdivisionName:
        return self.__activityMediaSubdivisionName

    @activityMediaSubdivisionName.setter
    def activityMediaSubdivisionName(self, val: ActivityMediaSubdivisionName) -> None:
        self.__activityMediaSubdivisionName = (
            None if val is None else ActivityMediaSubdivisionName(val)
        )

    @property
    def activityStartDate(self) -> ActivityStartDate:
        return self.__activityStartDate

    @activityStartDate.setter
    def activityStartDate(self, val: ActivityStartDate) -> None:
        self.__activityStartDate = (
            None
            if val is None
            else ActivityStartDate(year=val.year, month=val.month, day=val.day)
        )

    @property
    def activityStartTime(self) -> WQXTime:
        """
        The measure of clock time when the field activity began.
        """
        return self.__activityStartTime

    @activityStartTime.setter
    def activityStartTime(self, val: WQXTime) -> None:
        """
        The measure of clock time when the field activity began.
        """
        self.__activityStartTime = None if val is None else WQXTime(val)

    @property
    def activityEndDate(self) -> ActivityEndDate:
        return self.__activityEndDate

    @activityEndDate.setter
    def activityEndDate(self, val: ActivityEndDate) -> None:
        self.__activityEndDate = (
            None
            if val is None
            else ActivityEndDate(year=val.year, month=val.month, day=val.day)
        )

    @property
    def activityEndTime(self) -> WQXTime:
        """
        The measure of clock time when the field activity ended.
        """
        return self.__activityEndTime

    @activityEndTime.setter
    def activityEndTime(self, val: WQXTime) -> None:
        """
        The measure of clock time when the field activity ended.
        """
        self.__activityEndTime = None if val is None else WQXTime(val)

    @property
    def activityRelativeDepthName(self) -> ActivityRelativeDepthName:
        return self.__activityRelativeDepthName

    @activityRelativeDepthName.setter
    def activityRelativeDepthName(self, val: ActivityRelativeDepthName) -> None:
        self.__activityRelativeDepthName = (
            None if val is None else ActivityRelativeDepthName(val)
        )

    @property
    def activityDepthHeightMeasure(self) -> MeasureCompact:
        """
        A measurement of the vertical location (measured from a reference point) at
        which an activity occurred.
        """
        return self.__activityDepthHeightMeasure

    @activityDepthHeightMeasure.setter
    def activityDepthHeightMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the vertical location (measured from a reference point) at
        which an activity occurred.
        """
        self.__activityDepthHeightMeasure = None if val is None else MeasureCompact(val)

    @property
    def activityTopDepthHeightMeasure(self) -> MeasureCompact:
        """
        A measurement of the upper vertical location of a vertical location range
        (measured from a reference point) at which an activity occurred.
        """
        return self.__activityTopDepthHeightMeasure

    @activityTopDepthHeightMeasure.setter
    def activityTopDepthHeightMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the upper vertical location of a vertical location range
        (measured from a reference point) at which an activity occurred.
        """
        self.__activityTopDepthHeightMeasure = (
            None if val is None else MeasureCompact(val)
        )

    @property
    def activityBottomDepthHeightMeasure(self) -> MeasureCompact:
        """
        A measurement of the lower vertical location of a vertical location range
        (measured from a reference point) at which an activity occurred.
        """
        return self.__activityBottomDepthHeightMeasure

    @activityBottomDepthHeightMeasure.setter
    def activityBottomDepthHeightMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the lower vertical location of a vertical location range
        (measured from a reference point) at which an activity occurred.
        """
        self.__activityBottomDepthHeightMeasure = (
            None if val is None else MeasureCompact(val)
        )

    @property
    def activityDepthAltitudeReferencePointText(self,) -> DepthAltitudeReferencePointText:
        """
        The reference used to indicate the datum or reference used to establish the
        depth/altitude of an activity.
        """
        return self.__activityDepthAltitudeReferencePointText

    @activityDepthAltitudeReferencePointText.setter
    def activityDepthAltitudeReferencePointText(
        self, val: DepthAltitudeReferencePointText
    ) -> None:
        """
        The reference used to indicate the datum or reference used to establish the
        depth/altitude of an activity.
        """
        self.__activityDepthAltitudeReferencePointText = (
            None if val is None else DepthAltitudeReferencePointText(val)
        )

    @property
    def projectIdentifier(self) -> ProjectIdentifier:
        return self.__projectIdentifier

    @projectIdentifier.setter
    def projectIdentifier(self, val: ProjectIdentifier) -> None:
        self.__projectIdentifier = None if val is None else ProjectIdentifier(val)

    @property
    def activityConductingOrganizationText(
        self,
    ) -> List[ActivityConductingOrganizationText]:
        return self.__activityConductingOrganizationText

    @activityConductingOrganizationText.setter
    def activityConductingOrganizationText(
        self,
        val: Union[
            ActivityConductingOrganizationText, List[ActivityConductingOrganizationText]
        ],
    ) -> None:
        if val is None:
            self.__activityConductingOrganizationText = []
        elif isinstance(val, list):
            r: List[ActivityConductingOrganizationText] = []
            for x in val:
                r.append(ActivityConductingOrganizationText(x))
            self.__activityConductingOrganizationText = r
        else:
            self.__activityConductingOrganizationText = [
                ActivityConductingOrganizationText(val)
            ]

    @property
    def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
        return self.__monitoringLocationIdentifier

    @monitoringLocationIdentifier.setter
    def monitoringLocationIdentifier(self, val: MonitoringLocationIdentifier) -> None:
        self.__monitoringLocationIdentifier = (
            None if val is None else MonitoringLocationIdentifier(val)
        )

    @property
    def samplingComponentName(self) -> SamplingComponentName:
        return self.__samplingComponentName

    @samplingComponentName.setter
    def samplingComponentName(self, val: SamplingComponentName) -> None:
        self.__samplingComponentName = None if val is None else SamplingComponentName(val)

    @property
    def activityCommentText(self) -> CommentText:
        """
        General comments concerning the activity.
        """
        return self.__activityCommentText

    @activityCommentText.setter
    def activityCommentText(self, val: CommentText) -> None:
        """
        General comments concerning the activity.
        """
        self.__activityCommentText = None if val is None else CommentText(val)

    def generateXML(self, name: str = "ActivityDescription") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__activityIdentifier is None:
                raise WQXException("Attribute 'activityIdentifier' is required.")
            line("ActivityIdentifier", self.__activityIdentifier)
            if self.__activityIdentifierUserSupplied is not None:
                line(
                    "ActivityIdentifierUserSupplied",
                    self.__activityIdentifierUserSupplied,
                )
            if self.__activityTypeCode is None:
                raise WQXException("Attribute 'activityTypeCode' is required.")
            line("ActivityTypeCode", self.__activityTypeCode)
            if self.__activityMediaName is None:
                raise WQXException("Attribute 'activityMediaName' is required.")
            line("ActivityMediaName", self.__activityMediaName)
            if self.__activityMediaSubdivisionName is not None:
                line("ActivityMediaSubdivisionName", self.__activityMediaSubdivisionName)
            if self.__activityStartDate is None:
                raise WQXException("Attribute 'activityStartDate' is required.")
            line("ActivityStartDate", str(self.__activityStartDate))
            if self.__activityStartTime is not None:
                asis(self.__activityStartTime.generateXML("ActivityStartTime"))
            if self.__activityEndDate is not None:
                line("ActivityEndDate", str(self.__activityEndDate))
            if self.__activityEndTime is not None:
                asis(self.__activityEndTime.generateXML("ActivityEndTime"))
            if self.__activityRelativeDepthName is not None:
                line("ActivityRelativeDepthName", self.__activityRelativeDepthName)
            if self.__activityDepthHeightMeasure is not None:
                asis(
                    self.__activityDepthHeightMeasure.generateXML(
                        "ActivityDepthHeightMeasure"
                    )
                )
            if self.__activityTopDepthHeightMeasure is not None:
                asis(
                    self.__activityTopDepthHeightMeasure.generateXML(
                        "ActivityTopDepthHeightMeasure"
                    )
                )
            if self.__activityBottomDepthHeightMeasure is not None:
                asis(
                    self.__activityBottomDepthHeightMeasure.generateXML(
                        "ActivityBottomDepthHeightMeasure"
                    )
                )
            if self.__activityDepthAltitudeReferencePointText is not None:
                line(
                    "ActivityDepthAltitudeReferencePointText",
                    self.__activityDepthAltitudeReferencePointText,
                )
            if self.__projectIdentifier is None or len(self.__projectIdentifier) < 1:
                raise WQXException(
                    "Attribute 'projectIdentifier' must be a list of 1 or more "
                    "ProjectIdentifier objects."
                )
            line("ProjectIdentifier", self.__projectIdentifier)
            for x in self.__activityConductingOrganizationText:
                line("ActivityConductingOrganizationText", x)
            if self.__monitoringLocationIdentifier is not None:
                line("MonitoringLocationIdentifier", self.__monitoringLocationIdentifier)
            if self.__samplingComponentName is not None:
                line("SamplingComponentName", self.__samplingComponentName)
            if self.__activityCommentText is not None:
                line("ActivityCommentText", self.__activityCommentText)

        return doc.getvalue()
