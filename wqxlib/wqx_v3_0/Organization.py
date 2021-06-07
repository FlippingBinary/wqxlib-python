from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .Activity import Activity
from .ActivityGroup import ActivityGroup
from .BiologicalHabitatIndex import BiologicalHabitatIndex
from .ElectronicAddress import ElectronicAddress
from .MonitoringLocation import MonitoringLocation
from .OrganizationAddress import OrganizationAddress
from .OrganizationDescription import OrganizationDescription
from .Project import Project
from .Telephonic import Telephonic


class Organization:
    """
    Schema used to transfer organization information.
    """

    __organizationDescription: OrganizationDescription
    __electronicAddress: List[ElectronicAddress]
    __telephonic: List[Telephonic]
    __organizationAddress: List[OrganizationAddress]
    __project: List[Project]
    __monitoringLocation: List[MonitoringLocation]
    __biologicalHabitatIndex: List[BiologicalHabitatIndex]
    __activity: List[Activity]
    __activityGroup: List[ActivityGroup]

    def __init__(
        self,
        o: dict = None,
        *,
        organizationDescription: OrganizationDescription = None,
        electronicAddress: List[ElectronicAddress] = None,
        telephonic: List[Telephonic] = None,
        organizationAddress: List[OrganizationAddress] = None,
        project: List[Project] = None,
        monitoringLocation: List[MonitoringLocation] = None,
        biologicalHabitatIndex: List[BiologicalHabitatIndex] = None,
        activity: List[Activity] = None,
        activityGroup: List[ActivityGroup] = None
    ):
        if isinstance(o, Organization):
            # Assign attributes from object without typechecking
            self.__organizationDescription = o.organizationDescription
            self.__electronicAddress = o.electronicAddress
            self.__telephonic = o.telephonic
            self.__organizationAddress = o.organizationAddress
            self.__project = o.project
            self.__monitoringLocation = o.monitoringLocation
            self.__biologicalHabitatIndex = o.biologicalHabitatIndex
            self.__activity = o.activity
            self.__activityGroup = o.activityGroup
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.organizationDescription = o.get("organizationDescription")
            self.electronicAddress = o.get("electronicAddress")
            self.telephonic = o.get("telephonic")
            self.organizationAddress = o.get("organizationAddress")
            self.project = o.get("project")
            self.monitoringLocation = o.get("monitoringLocation")
            self.biologicalHabitatIndex = o.get("biologicalHabitatIndex")
            self.activity = o.get("activity")
            self.activityGroup = o.get("activityGroup")
        else:
            # Assign attributes from named keywords with typechecking
            self.organizationDescription = organizationDescription
            self.electronicAddress = electronicAddress
            self.telephonic = telephonic
            self.organizationAddress = organizationAddress
            self.project = project
            self.monitoringLocation = monitoringLocation
            self.biologicalHabitatIndex = biologicalHabitatIndex
            self.activity = activity
            self.activityGroup = activityGroup

    @property
    def organizationDescription(self) -> OrganizationDescription:
        return self.__organizationDescription

    @organizationDescription.setter
    def organizationDescription(self, val: OrganizationDescription) -> None:
        if val is not None and not isinstance(val, OrganizationDescription):
            raise WQXException(
                "Property 'organizationDescription' must be an OrganizationDescription "
                "object."
            )
        self.__organizationDescription = (
            None if val is None else OrganizationDescription(val)
        )

    @property
    def electronicAddress(self) -> List[ElectronicAddress]:
        return self.__electronicAddress

    @electronicAddress.setter
    def electronicAddress(
        self, val: Union[ElectronicAddress, List[ElectronicAddress]]
    ) -> None:
        if val is None:
            self.__electronicAddress = []
        elif isinstance(val, list):
            r: List[ElectronicAddress] = []
            for x in val:
                r.append(ElectronicAddress(x))
            self.__electronicAddress = r
        else:
            self.__electronicAddress = [ElectronicAddress(val)]

    @property
    def telephonic(self) -> List[Telephonic]:
        return self.__telephonic

    @telephonic.setter
    def telephonic(self, val: Union[Telephonic, List[Telephonic]]) -> None:
        if val is None:
            self.__telephonic = []
        elif isinstance(val, list):
            r: List[Telephonic] = []
            for x in val:
                r.append(Telephonic(x))
            self.__telephonic = r
        else:
            self.__telephonic = [Telephonic(val)]

    @property
    def organizationAddress(self) -> List[OrganizationAddress]:
        return self.__organizationAddress

    @organizationAddress.setter
    def organizationAddress(
        self, val: Union[OrganizationAddress, List[OrganizationAddress]]
    ) -> None:
        if val is None:
            self.__organizationAddress = []
        elif isinstance(val, list):
            r: List[OrganizationAddress] = []
            for x in val:
                r.append(OrganizationAddress(x))
            self.__organizationAddress = r
        else:
            self.__organizationAddress = [OrganizationAddress(val)]

    @property
    def project(self) -> List[Project]:
        return self.__project

    @project.setter
    def project(self, val: Union[Project, List[Project]]) -> None:
        if val is None:
            self.__project = []
        elif isinstance(val, list):
            r: List[Project] = []
            for x in val:
                r.append(Project(x))
            self.__project = r
        else:
            self.__project = [Project(val)]

    @property
    def monitoringLocation(self) -> List[MonitoringLocation]:
        return self.__monitoringLocation

    @monitoringLocation.setter
    def monitoringLocation(
        self, val: Union[MonitoringLocation, List[MonitoringLocation]]
    ) -> None:
        if val is None:
            self.__monitoringLocation = []
        elif isinstance(val, list):
            r: List[MonitoringLocation] = []
            for x in val:
                r.append(MonitoringLocation(x))
            self.__monitoringLocation = r
        else:
            self.__monitoringLocation = [MonitoringLocation(val)]

    @property
    def biologicalHabitatIndex(self) -> List[BiologicalHabitatIndex]:
        return self.__biologicalHabitatIndex

    @biologicalHabitatIndex.setter
    def biologicalHabitatIndex(
        self, val: Union[BiologicalHabitatIndex, List[BiologicalHabitatIndex]]
    ) -> None:
        if val is None:
            self.__biologicalHabitatIndex = []
        elif isinstance(val, list):
            r: List[BiologicalHabitatIndex] = []
            for x in val:
                r.append(BiologicalHabitatIndex(x))
            self.__biologicalHabitatIndex = r
        else:
            self.__biologicalHabitatIndex = [BiologicalHabitatIndex(val)]

    @property
    def activity(self) -> List[Activity]:
        return self.__activity

    @activity.setter
    def activity(self, val: Union[Activity, List[Activity]]) -> None:
        if val is None:
            self.__activity = []
        elif isinstance(val, list):
            r: List[Activity] = []
            for x in val:
                r.append(Activity(x))
            self.__activity = r
        else:
            self.__activity = [Activity(val)]

    @property
    def activityGroup(self) -> List[ActivityGroup]:
        return self.__activityGroup

    @activityGroup.setter
    def activityGroup(self, val: Union[ActivityGroup, List[ActivityGroup]]) -> None:
        if val is None:
            self.__activityGroup = []
        elif isinstance(val, list):
            r: List[ActivityGroup] = []
            for x in val:
                r.append(ActivityGroup(x))
            self.__activityGroup = r
        else:
            self.__activityGroup = [ActivityGroup(val)]

    def generateXML(self, name: str = "Organization") -> str:  # noqa: C901
        doc = Doc()
        asis = doc.asis
        tag = doc.tag

        with tag(name):
            if self.__organizationDescription is None:
                raise WQXException("Attribute 'organizationDescription' is required.")
            asis(self.__organizationDescription.generateXML("OrganizationDescription"))
            for x in self.__electronicAddress:
                asis(x.generateXML("ElectronicAddress"))
            for x in self.__telephonic:
                asis(x.generateXML("Telephonic"))
            if len(self.__organizationAddress) > 3:
                raise WQXException(
                    "Attribute 'organizationAddress' must contain 0 to 3 "
                    "OrganizationAddress objects."
                )
            for x in self.__organizationAddress:
                asis(x.generateXML("OrganizationAddress"))
            for x in self.__project:
                asis(x.generateXML("Project"))
            for x in self.__monitoringLocation:
                asis(x.generateXML("MonitoringLocation"))
            for x in self.__biologicalHabitatIndex:
                asis(x.generateXML("BiologicalHabitatIndex"))
            for x in self.__activity:
                asis(x.generateXML("Activity"))
            for x in self.__activityGroup:
                asis(x.generateXML("ActivityGroup"))

        return doc.getvalue()
