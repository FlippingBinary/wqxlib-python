from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .AttachedBinaryObject import AttachedBinaryObject
from .ProjectMonitoringLocationWeighting import ProjectMonitoringLocationWeighting
from .SimpleContent import (
    ProjectDescriptionText,
    ProjectIdentifier,
    ProjectName,
    QAPPApprovalAgencyName,
    QAPPApprovedIndicator,
    SamplingDesignTypeCode,
)


class Project:
    """
    An environmental data collection effort that has a stated purpose and puts a series
    of samples and results into a meaningful context.
    """

    __projectIdentifier: ProjectIdentifier
    __projectName: ProjectName
    __projectDescriptionText: ProjectDescriptionText
    __samplingDesignTypeCode: SamplingDesignTypeCode
    __qAPPApprovedIndicator: QAPPApprovedIndicator
    __qAPPApprovalAgencyName: QAPPApprovalAgencyName
    __attachedBinaryObject: List[AttachedBinaryObject]
    __projectMonitoringLocationWeighting: List[ProjectMonitoringLocationWeighting]

    def __init__(
        self,
        o: dict = None,
        *,
        projectIdentifier: ProjectIdentifier = None,
        projectName: ProjectName = None,
        projectDescriptionText: ProjectDescriptionText = None,
        samplingDesignTypeCode: SamplingDesignTypeCode = None,
        qAPPApprovedIndicator: QAPPApprovedIndicator = None,
        qAPPApprovalAgencyName: QAPPApprovalAgencyName = None,
        attachedBinaryObject: List[AttachedBinaryObject] = None,
        projectMonitoringLocationWeighting: List[
            ProjectMonitoringLocationWeighting
        ] = None
    ):
        if isinstance(o, Project):
            # Assign attributes from object without typechecking
            self.__projectIdentifier = o.projectIdentifier
            self.__projectName = o.projectName
            self.__projectDescriptionText = o.projectDescriptionText
            self.__samplingDesignTypeCode = o.samplingDesignTypeCode
            self.__qAPPApprovedIndicator = o.qAPPApprovedIndicator
            self.__qAPPApprovalAgencyName = o.qAPPApprovalAgencyName
            self.__attachedBinaryObject = o.attachedBinaryObject
            self.__projectMonitoringLocationWeighting = (
                o.projectMonitoringLocationWeighting
            )
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.projectIdentifier = o.get("projectIdentifier")
            self.projectName = o.get("projectName")
            self.projectDescriptionText = o.get("projectDescriptionText")
            self.samplingDesignTypeCode = o.get("samplingDesignTypeCode")
            self.qAPPApprovedIndicator = o.get("qAPPApprovedIndicator")
            self.qAPPApprovalAgencyName = o.get("qAPPApprovalAgencyName")
            self.attachedBinaryObject = o.get("attachedBinaryObject")
            self.projectMonitoringLocationWeighting = o.get(
                "projectMonitoringLocationWeighting"
            )
        else:
            # Assign attributes from named keywords with typechecking
            self.projectIdentifier = projectIdentifier
            self.projectName = projectName
            self.projectDescriptionText = projectDescriptionText
            self.samplingDesignTypeCode = samplingDesignTypeCode
            self.qAPPApprovedIndicator = qAPPApprovedIndicator
            self.qAPPApprovalAgencyName = qAPPApprovalAgencyName
            self.attachedBinaryObject = attachedBinaryObject
            self.projectMonitoringLocationWeighting = projectMonitoringLocationWeighting

    @property
    def projectIdentifier(self) -> ProjectIdentifier:
        return self.__projectIdentifier

    @projectIdentifier.setter
    def projectIdentifier(self, val: ProjectIdentifier) -> None:
        self.__projectIdentifier = ProjectIdentifier(val)

    @property
    def projectName(self) -> ProjectName:
        return self.__projectName

    @projectName.setter
    def projectName(self, val: ProjectName) -> None:
        self.__projectName = ProjectName(val)

    @property
    def projectDescriptionText(self) -> ProjectDescriptionText:
        return self.__projectDescriptionText

    @projectDescriptionText.setter
    def projectDescriptionText(self, val: ProjectDescriptionText) -> None:
        self.__projectDescriptionText = (
            None if val is None else ProjectDescriptionText(val)
        )

    @property
    def samplingDesignTypeCode(self) -> SamplingDesignTypeCode:
        return self.__samplingDesignTypeCode

    @samplingDesignTypeCode.setter
    def samplingDesignTypeCode(self, val: SamplingDesignTypeCode) -> None:
        self.__samplingDesignTypeCode = (
            None if val is None else SamplingDesignTypeCode(val)
        )

    @property
    def qAPPApprovedIndicator(self) -> QAPPApprovedIndicator:
        return self.__qAPPApprovedIndicator

    @qAPPApprovedIndicator.setter
    def qAPPApprovedIndicator(self, val: QAPPApprovedIndicator) -> None:
        self.__qAPPApprovedIndicator = None if val is None else QAPPApprovedIndicator(val)

    @property
    def qAPPApprovalAgencyName(self) -> QAPPApprovalAgencyName:
        return self.__qAPPApprovalAgencyName

    @qAPPApprovalAgencyName.setter
    def qAPPApprovalAgencyName(self, val: QAPPApprovalAgencyName) -> None:
        self.__qAPPApprovalAgencyName = (
            None if val is None else QAPPApprovalAgencyName(val)
        )

    @property
    def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
        return self.__attachedBinaryObject

    @attachedBinaryObject.setter
    def attachedBinaryObject(
        self, val: Union[AttachedBinaryObject, List[AttachedBinaryObject]]
    ) -> None:
        if val is None:
            self.__attachedBinaryObject = []
        elif isinstance(val, list):
            r: List[AttachedBinaryObject] = []
            for x in val:
                r.append(AttachedBinaryObject(x))
            self.__attachedBinaryObject = r
        else:
            self.__attachedBinaryObject = [AttachedBinaryObject(val)]

    @property
    def projectMonitoringLocationWeighting(
        self,
    ) -> List[ProjectMonitoringLocationWeighting]:
        return self.__projectMonitoringLocationWeighting

    @projectMonitoringLocationWeighting.setter
    def projectMonitoringLocationWeighting(
        self,
        val: Union[
            ProjectMonitoringLocationWeighting, List[ProjectMonitoringLocationWeighting]
        ],
    ) -> None:
        if val is None:
            self.__projectMonitoringLocationWeighting = []
        elif isinstance(val, list):
            r: List[ProjectMonitoringLocationWeighting] = []
            for x in val:
                r.append(ProjectMonitoringLocationWeighting(x))
            self.__projectMonitoringLocationWeighting = r
        else:
            self.__projectMonitoringLocationWeighting = [
                ProjectMonitoringLocationWeighting(val)
            ]

    def generateXML(self, name: str = "Project") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__projectIdentifier is None:
                raise WQXException("Attribute 'projectIdentifier' is required.")
            line("ProjectIdentifier", self.__projectIdentifier)
            if self.__projectName is None:
                raise WQXException("Attribute 'projectName' is required.")
            line("ProjectName", self.__projectName)
            if self.__projectDescriptionText is not None:
                line("ProjectDescriptionText", self.__projectDescriptionText)
            if self.__samplingDesignTypeCode is not None:
                line("SamplingDesignTypeCode", self.__samplingDesignTypeCode)
            if self.__qAPPApprovedIndicator is not None:
                line("QAPPApprovedIndicator", self.__qAPPApprovedIndicator)
            if self.__qAPPApprovalAgencyName is not None:
                line("QAPPApprovalAgencyName", self.__qAPPApprovalAgencyName)
            for x in self.__attachedBinaryObject:
                asis(x.generateXML("AttachedBinaryObject"))
            for x in self.__projectMonitoringLocationWeighting:
                asis(x.generateXML("ProjectMonitoringLocationWeighting"))

        return doc.getvalue()
