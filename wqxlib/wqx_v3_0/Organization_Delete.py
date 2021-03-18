from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import (
    ActivityGroupIdentifier,
    ActivityIdentifier,
    IndexIdentifier,
    MonitoringLocationIdentifier,
    OrganizationIdentifier,
    ProjectIdentifier,
)


class OrganizationDelete:
    """
    Schema used to delete organization information
    """

    __organizationIdentifier: OrganizationIdentifier
    __projectIdentifier: List[ProjectIdentifier]
    __monitoringLocationIdentifier: List[MonitoringLocationIdentifier]
    __activityIdentifier: List[ActivityIdentifier]
    __activityGroupIdentifier: List[ActivityGroupIdentifier]
    __indexIdentifier: List[IndexIdentifier]

    def __init__(
        self,
        o: dict = None,
        *,
        organizationIdentifier: OrganizationIdentifier = None,
        projectIdentifier: List[ProjectIdentifier] = None,
        monitoringLocationIdentifier: List[MonitoringLocationIdentifier] = None,
        activityIdentifier: List[ActivityIdentifier] = None,
        activityGroupIdentifier: List[ActivityGroupIdentifier] = None,
        indexIdentifier: List[IndexIdentifier] = None
    ):
        if isinstance(o, OrganizationDelete):
            # Assign attributes from object without typechecking
            self.__organizationIdentifier = o.organizationIdentifier
            self.__projectIdentifier = o.projectIdentifier
            self.__monitoringLocationIdentifier = o.monitoringLocationIdentifier
            self.__activityIdentifier = o.activityIdentifier
            self.__activityGroupIdentifier = o.activityGroupIdentifier
            self.__indexIdentifier = o.indexIdentifier
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.organizationIdentifier = o.get("organizationIdentifier")
            self.projectIdentifier = o.get("projectIdentifier")
            self.monitoringLocationIdentifier = o.get("monitoringLocationIdentifier")
            self.activityIdentifier = o.get("activityIdentifier")
            self.activityGroupIdentifier = o.get("activityGroupIdentifier")
            self.indexIdentifier = o.get("indexIdentifier")
        else:
            # Assign attributes from named keywords with typechecking
            self.organizationIdentifier = organizationIdentifier
            self.projectIdentifier = projectIdentifier
            self.monitoringLocationIdentifier = monitoringLocationIdentifier
            self.activityIdentifier = activityIdentifier
            self.activityGroupIdentifier = activityGroupIdentifier
            self.indexIdentifier = indexIdentifier

    @property
    def organizationIdentifier(self) -> OrganizationIdentifier:
        return self.__organizationIdentifier

    @organizationIdentifier.setter
    def organizationIdentifier(self, val: OrganizationIdentifier) -> None:
        self.__organizationIdentifier = (
            None if val is None else OrganizationIdentifier(val)
        )

    @property
    def projectIdentifier(self) -> List[ProjectIdentifier]:
        return self.__projectIdentifier

    @projectIdentifier.setter
    def projectIdentifier(
        self, val: Union[ProjectIdentifier, List[ProjectIdentifier]]
    ) -> None:
        if val is None:
            self.__projectIdentifier = []
        elif isinstance(val, list):
            r: List[ProjectIdentifier] = []
            for x in val:
                r.append(ProjectIdentifier(x))
            self.__projectIdentifier = r
        else:
            self.__projectIdentifier = [ProjectIdentifier(val)]

    @property
    def monitoringLocationIdentifier(self) -> List[MonitoringLocationIdentifier]:
        return self.__monitoringLocationIdentifier

    @monitoringLocationIdentifier.setter
    def monitoringLocationIdentifier(
        self,
        val: Union[MonitoringLocationIdentifier, List[MonitoringLocationIdentifier]],
    ) -> None:
        if val is None:
            self.__monitoringLocationIdentifier = []
        elif isinstance(val, list):
            r: List[MonitoringLocationIdentifier] = []
            for x in val:
                r.append(MonitoringLocationIdentifier(x))
            self.__monitoringLocationIdentifier = r
        else:
            self.__monitoringLocationIdentifier = [MonitoringLocationIdentifier(val)]

    @property
    def activityIdentifier(self) -> List[ActivityIdentifier]:
        return self.__activityIdentifier

    @activityIdentifier.setter
    def activityIdentifier(
        self, val: Union[ActivityIdentifier, List[ActivityIdentifier]]
    ) -> None:
        if val is None:
            self.__activityIdentifier = []
        elif isinstance(val, list):
            r: List[ActivityIdentifier] = []
            for x in val:
                r.append(ActivityIdentifier(x))
            self.__activityIdentifier = r
        else:
            self.__activityIdentifier = [ActivityIdentifier(val)]

    @property
    def activityGroupIdentifier(self) -> List[ActivityGroupIdentifier]:
        return self.__activityGroupIdentifier

    @activityGroupIdentifier.setter
    def activityGroupIdentifier(
        self, val: Union[ActivityGroupIdentifier, List[ActivityGroupIdentifier]]
    ) -> None:
        if val is None:
            self.__activityGroupIdentifier = []
        elif isinstance(val, list):
            r: List[ActivityGroupIdentifier] = []
            for x in val:
                r.append(ActivityGroupIdentifier(x))
            self.__activityGroupIdentifier = r
        else:
            self.__activityGroupIdentifier = [ActivityGroupIdentifier(val)]

    @property
    def indexIdentifier(self) -> List[IndexIdentifier]:
        return self.__indexIdentifier

    @indexIdentifier.setter
    def indexIdentifier(self, val: Union[IndexIdentifier, List[IndexIdentifier]]) -> None:
        if val is None:
            self.__indexIdentifier = []
        elif isinstance(val, list):
            r: List[IndexIdentifier] = []
            for x in val:
                r.append(IndexIdentifier(x))
            self.__indexIdentifier = r
        else:
            self.__indexIdentifier = [IndexIdentifier(val)]

    def generateXML(self, name="OrganizationDelete"):
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__organizationIdentifier is None:
                raise WQXException("Attribute 'organizationIdentifier' is required.")
            line("OrganizationIdentifier", self.__organizationIdentifier)
            for x in self.__projectIdentifier:
                line("ProjectIdentifier", x)
            for x in self.__monitoringLocationIdentifier:
                line("MonitoringLocationIdentifier", x)
            for x in self.__activityIdentifier:
                line("ActivityIdentifier", x)
            for x in self.__activityGroupIdentifier:
                line("ActivityGroupIdentifier", x)
            for x in self.__indexIdentifier:
                line("IndexIdentifier", x)

        return doc.getvalue()
