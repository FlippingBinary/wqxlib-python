from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .AlternateMonitoringLocationIdentity import AlternateMonitoringLocationIdentity
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
    HUCEightDigitCode,
    HUCTwelveDigitCode,
    MonitoringLocationDescriptionText,
    MonitoringLocationIdentifier,
    MonitoringLocationName,
    MonitoringLocationTypeName,
    TribalLandIndicator,
    TribalLandName,
)


class MonitoringLocationIdentity:
    """
    Basic identification information for the location/site that is monitored or used
    for sampling.
    """

    __monitoringLocationIdentifier: MonitoringLocationIdentifier
    __monitoringLocationName: MonitoringLocationName
    __monitoringLocationTypeName: MonitoringLocationTypeName
    __monitoringLocationDescriptionText: MonitoringLocationDescriptionText
    __hucEightDigitCode: HUCEightDigitCode
    __hucTwelveDigitCode: HUCTwelveDigitCode
    __tribalLandIndicator: TribalLandIndicator
    __tribalLandName: TribalLandName
    __alternateMonitoringLocationIdentity: List[AlternateMonitoringLocationIdentity]
    __drainageAreaMeasure: MeasureCompact
    __contributingDrainageAreaMeasure: MeasureCompact

    def __init__(
        self,
        o: dict = None,
        *,
        monitoringLocationIdentifier: MonitoringLocationIdentifier = None,
        monitoringLocationName: MonitoringLocationName = None,
        monitoringLocationTypeName: MonitoringLocationTypeName = None,
        monitoringLocationDescriptionText: MonitoringLocationDescriptionText = None,
        hucEightDigitCode: HUCEightDigitCode = None,
        hucTwelveDigitCode: HUCTwelveDigitCode = None,
        tribalLandIndicator: TribalLandIndicator = None,
        tribalLandName: TribalLandName = None,
        alternateMonitoringLocationIdentity: List[
            AlternateMonitoringLocationIdentity
        ] = None,
        drainageAreaMeasure: MeasureCompact = None,
        contributingDrainageAreaMeasure: MeasureCompact = None
    ):
        if isinstance(o, MonitoringLocationIdentity):
            # Assign attributes from object without typechecking
            self.__monitoringLocationIdentifier = o.monitoringLocationIdentifier
            self.__monitoringLocationName = o.monitoringLocationName
            self.__monitoringLocationTypeName = o.monitoringLocationTypeName
            self.__monitoringLocationDescriptionText = o.monitoringLocationDescriptionText
            self.__hucEightDigitCode = o.hucEightDigitCode
            self.__hucTwelveDigitCode = o.hucTwelveDigitCode
            self.__tribalLandIndicator = o.tribalLandIndicator
            self.__tribalLandName = o.tribalLandName
            self.__alternateMonitoringLocationIdentity = (
                o.alternateMonitoringLocationIdentity
            )
            self.__drainageAreaMeasure = o.drainageAreaMeasure
            self.__contributingDrainageAreaMeasure = o.contributingDrainageAreaMeasure
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.monitoringLocationIdentifier = o.get("monitoringLocationIdentifier")
            self.monitoringLocationName = o.get("monitoringLocationName")
            self.monitoringLocationTypeName = o.get("monitoringLocationTypeName")
            self.monitoringLocationDescriptionText = o.get(
                "monitoringLocationDescriptionText"
            )
            self.hucEightDigitCode = o.get("hucEightDigitCode")
            self.hucTwelveDigitCode = o.get("hucTwelveDigitCode")
            self.tribalLandIndicator = o.get("tribalLandIndicator")
            self.tribalLandName = o.get("tribalLandName")
            self.alternateMonitoringLocationIdentity = o.get(
                "alternateMonitoringLocationIdentity"
            )
            self.drainageAreaMeasure = o.get("drainageAreaMeasure")
            self.contributingDrainageAreaMeasure = o.get(
                "contributingDrainageAreaMeasure"
            )
        else:
            # Assign attributes from named keywords with typechecking
            self.monitoringLocationIdentifier = monitoringLocationIdentifier
            self.monitoringLocationName = monitoringLocationName
            self.monitoringLocationTypeName = monitoringLocationTypeName
            self.monitoringLocationDescriptionText = monitoringLocationDescriptionText
            self.hucEightDigitCode = hucEightDigitCode
            self.hucTwelveDigitCode = hucTwelveDigitCode
            self.tribalLandIndicator = tribalLandIndicator
            self.tribalLandName = tribalLandName
            self.alternateMonitoringLocationIdentity = alternateMonitoringLocationIdentity
            self.drainageAreaMeasure = drainageAreaMeasure
            self.contributingDrainageAreaMeasure = contributingDrainageAreaMeasure

    @property
    def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
        return self.__monitoringLocationIdentifier

    @monitoringLocationIdentifier.setter
    def monitoringLocationIdentifier(self, val: MonitoringLocationIdentifier) -> None:
        self.__monitoringLocationIdentifier = (
            None if val is None else MonitoringLocationIdentifier(val)
        )

    @property
    def monitoringLocationName(self) -> MonitoringLocationName:
        return self.__monitoringLocationName

    @monitoringLocationName.setter
    def monitoringLocationName(self, val: MonitoringLocationName) -> None:
        self.__monitoringLocationName = (
            None if val is None else MonitoringLocationName(val)
        )

    @property
    def monitoringLocationTypeName(self) -> MonitoringLocationTypeName:
        return self.__monitoringLocationTypeName

    @monitoringLocationTypeName.setter
    def monitoringLocationTypeName(self, val: MonitoringLocationTypeName) -> None:
        self.__monitoringLocationTypeName = (
            None if val is None else MonitoringLocationTypeName(val)
        )

    @property
    def monitoringLocationDescriptionText(self) -> MonitoringLocationDescriptionText:
        return self.__monitoringLocationDescriptionText

    @monitoringLocationDescriptionText.setter
    def monitoringLocationDescriptionText(
        self, val: MonitoringLocationDescriptionText
    ) -> None:
        self.__monitoringLocationDescriptionText = (
            None if val is None else MonitoringLocationDescriptionText(val)
        )

    @property
    def hucEightDigitCode(self) -> HUCEightDigitCode:
        return self.__hucEightDigitCode

    @hucEightDigitCode.setter
    def hucEightDigitCode(self, val: HUCEightDigitCode) -> None:
        self.__hucEightDigitCode = None if val is None else HUCEightDigitCode(val)

    @property
    def hucTwelveDigitCode(self) -> HUCTwelveDigitCode:
        return self.__hucTwelveDigitCode

    @hucTwelveDigitCode.setter
    def hucTwelveDigitCode(self, val: HUCTwelveDigitCode) -> None:
        self.__hucTwelveDigitCode = None if val is None else HUCTwelveDigitCode(val)

    @property
    def tribalLandIndicator(self) -> TribalLandIndicator:
        return self.__tribalLandIndicator

    @tribalLandIndicator.setter
    def tribalLandIndicator(self, val: TribalLandIndicator) -> None:
        self.__tribalLandIndicator = TribalLandIndicator(val)

    @property
    def tribalLandName(self) -> TribalLandName:
        return self.__tribalLandName

    @tribalLandName.setter
    def tribalLandName(self, val: TribalLandName) -> None:
        self.__tribalLandName = None if val is None else TribalLandName(val)

    @property
    def alternateMonitoringLocationIdentity(
        self,
    ) -> List[AlternateMonitoringLocationIdentity]:
        return self.__alternateMonitoringLocationIdentity

    @alternateMonitoringLocationIdentity.setter
    def alternateMonitoringLocationIdentity(
        self,
        val: Union[
            AlternateMonitoringLocationIdentity,
            List[AlternateMonitoringLocationIdentity],
        ],
    ) -> None:
        if val is None:
            self.__alternateMonitoringLocationIdentity = []
        elif isinstance(val, list):
            r: List[AlternateMonitoringLocationIdentity] = []
            for x in val:
                r.append(AlternateMonitoringLocationIdentity(x))
            self.__alternateMonitoringLocationIdentity = r
        else:
            self.__alternateMonitoringLocationIdentity = [
                AlternateMonitoringLocationIdentity(val)
            ]

    @property
    def drainageAreaMeasure(self) -> MeasureCompact:
        """
        The drainage basin of a lake, stream, wetland, or estuary site.
        """
        return self.__drainageAreaMeasure

    @drainageAreaMeasure.setter
    def drainageAreaMeasure(self, val: MeasureCompact) -> None:
        """
        The drainage basin of a lake, stream, wetland, or estuary site.
        """
        self.__drainageAreaMeasure = None if val is None else MeasureCompact(val)

    @property
    def contributingDrainageAreaMeasure(self) -> MeasureCompact:
        """
        The contributing drainage area of a lake, stream, wetland, or estuary site.
        """
        return self.__contributingDrainageAreaMeasure

    @contributingDrainageAreaMeasure.setter
    def contributingDrainageAreaMeasure(self, val: MeasureCompact) -> None:
        """
        The contributing drainage area of a lake, stream, wetland, or estuary site.
        """
        self.__contributingDrainageAreaMeasure = (
            None if val is None else MeasureCompact(val)
        )

    def generateXML(self, name: str = "MonitoringLocationIdentity") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__monitoringLocationIdentifier is None:
                raise WQXException(
                    "Attribute 'MonitoringLocationIdentifier' is required."
                )
            line("MonitoringLocationIdentifier", self.__monitoringLocationIdentifier)
            if self.__monitoringLocationName is None:
                raise WQXException("Attribute 'MonitoringLocationName' is required.")
            line("MonitoringLocationName", self.__monitoringLocationName)
            if self.__monitoringLocationTypeName is None:
                raise WQXException("Attribute 'MonitoringLocationTypeName' is required.")
            line("MonitoringLocationTypeName", self.__monitoringLocationTypeName)
            if self.__monitoringLocationDescriptionText is not None:
                line(
                    "MonitoringLocationDescriptionText",
                    self.__monitoringLocationDescriptionText,
                )
            if self.__hucEightDigitCode is not None:
                line("HUCEightDigitCode", self.__hucEightDigitCode)
            if self.__hucTwelveDigitCode is not None:
                line("HUCTwelveDigitCode", self.__hucTwelveDigitCode)
            line("TribalLandIndicator", str(self.__tribalLandIndicator))
            if self.__tribalLandName is not None:
                line("TribalLandName", self.__tribalLandName)
            for x in self.__alternateMonitoringLocationIdentity:
                asis(x.generateXML("AlternateMonitoringLocationIdentity"))
            if self.__drainageAreaMeasure is not None:
                asis(self.__drainageAreaMeasure.generateXML("DrainageAreaMeasure"))
            if self.__contributingDrainageAreaMeasure is not None:
                asis(
                    self.__contributingDrainageAreaMeasure.generateXML(
                        "ContributingDrainageAreaMeasure"
                    )
                )

        return doc.getvalue()
