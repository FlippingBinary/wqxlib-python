from io import BytesIO
from typing import List, NewType
from zipfile import ZipFile

from .Document import Document
from .Header import Header
from .Payload import Payload
from .wqx_v3_0 import WQX, Organization, OrganizationDescription
from .WQXActivity import WQXActivity
from .WQXElectronicAddress import WQXElectronicAddress
from .WQXMonitoringLocation import WQXMonitoringLocation
from .WQXOrganizationAddress import WQXOrganizationAddress
from .WQXTelephonic import WQXTelephonic

WQXActivityType = NewType("WQXActivity", WQXActivity)
# WQXActivityGroupType = NewType("WQXActivityGroup", WQXActivityGroup)
# WQXBiologicalHabitatIndex = NewType("WQXBiologicalHabitatIndex", WQXBiologicalHabitatIndex)
WQXElectronicAddressType = NewType("WQXElectronicAddress", WQXElectronicAddress)
WQXMonitoringLocationType = NewType("WQXMonitoringLocation", WQXMonitoringLocation)
WQXOrganizationAddressType = NewType("WQXOrganizationAddress", WQXOrganizationAddress)
# WQXProjectType = NewType("WQXProject", WQXProject)
WQXTelephonicType = NewType("WQXTelephonic", WQXTelephonic)


class WQXSubmission(Document, Header, OrganizationDescription):
    __filename: str = None
    __activities: List[WQXActivityType] = []
    # __activityGroups: List[WQXActivityGroupType] = []
    # __biologicalHabitatIndices: List[WQXBiologicalHabitatIndex] = []
    __electronicAddresses: List[WQXElectronicAddressType] = []
    __monitoringLocations: List[WQXMonitoringLocation] = []
    __organizationAddresses: List[WQXOrganizationAddressType] = []
    # __projects: List[WQXProjectType] = []
    __telephonics: List[WQXTelephonicType] = []

    def __init__(self, filename: str = None):
        OrganizationDescription.__init__(self)
        Header.__init__(self)
        Document.__init__(self)
        self.__filename = filename
        self.title = "WQX"
        self.__activities = []
        # self.__activityGroups = []
        # self.__biologicalHabitatIndices = []
        self.__electronicAddresses = []
        self.__monitoringLocations = []
        self.__organizationAddresses = []
        # self.__projects = []
        self.__telephonics = []

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            print("WQX Document creation failed due to exceptions")
            print(exception_value)
            print(exception_traceback)
            return
        if self.__filename is not None:
            filetype = self.__filename[-4:].upper()
            if filetype.upper() == ".ZIP":
                self.generateZIP(fileName=self.__filename)
            elif filetype.upper() == ".XML":
                self.generateXML(fileName=self.__filename)
        # else do nothing because we assume it was handled inside the 'with'.

    def activity(self) -> WQXActivity:
        tmp = WQXActivity()
        self.__activities.append(tmp)
        return tmp

    # def activityGroup(self) -> WQXActivityGroup:
    #    tmp = WQXActivityGroup()
    #    self.__activityGroups.append(tmp)
    #    return tmp

    # def biologicalHabitatIndex(self) -> WQXBiologicalHabitatIndex:
    #    tmp = WQXBiologicalHabitatIndex()
    #    self.__biologicalHabitatIndices.append(tmp)
    #    return tmp

    def electronicAddress(self) -> WQXElectronicAddress:
        tmp = WQXElectronicAddress()
        self.__electronicAddresses.append(tmp)
        return tmp

    def monitoringLocation(self) -> WQXMonitoringLocation:
        tmp = WQXMonitoringLocation()
        self.__monitoringLocations.append(tmp)
        return tmp

    def organizationAddress(self) -> WQXOrganizationAddress:
        tmp = WQXOrganizationAddress()
        self.__organizationAddresses.append(tmp)
        return tmp

    # def project(self) -> WQXProject:
    #    tmp = WQXProject()
    #    self.__projects.append(tmp)
    #    return tmp

    def telephonic(self) -> WQXTelephonic:
        tmp = WQXTelephonic()
        self.__telephonics.append(tmp)
        return tmp

    def normalize(self) -> None:
        self.header = Header(self)
        self.payload = [
            Payload(
                operation="Update-Insert",
                wqx=WQX(
                    organization=Organization(
                        organizationDescription=OrganizationDescription(self),
                        electronicAddress=self.__electronicAddresses,
                        telephonic=self.__telephonics,
                        organizationAddress=self.__organizationAddresses,
                        # project=self.__projects,
                        monitoringLocation=self.__monitoringLocations,
                        # biologicalHabitatIndex=self.__biologicalHabitatIndex,
                        activity=self.__activities,
                        # activityGroup=self.__activityGroups,
                    )
                ),
            )
        ]

    def list_rule_violations(self) -> List[str]:
        self.normalize()
        return self.list_rule_violations()

    def generateXML(self, fileName: str = None) -> str:
        self.normalize()
        if fileName is None:
            return super().generateXML()
        else:
            with open(fileName, "w") as out:
                out.write(super().generateXML())

    def generateZIP(self, fileName: str = None):
        if not isinstance(fileName, str):
            raise TypeError("Parameter 'fileName' must be a string.")

        mem = BytesIO()
        zip = ZipFile(mem, mode="w")

        zip.writestr("submission.xml", self.generateXML())

        # TODO: Add attachment files, if necessary. Example:
        #   zip.writestr('rawdata.csv', self.data)

        zip.close()
        mem.seek(0)

        with open(fileName, "wb") as out:
            out.write(mem.read())
