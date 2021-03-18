from typing import List, Union

from yattag import Doc

from ..exceptions import WQXException
from .AttachedBinaryObject import AttachedBinaryObject
from .MonitoringLocationGeospatial import MonitoringLocationGeospatial
from .MonitoringLocationIdentity import MonitoringLocationIdentity
from .WellInformation import WellInformation


class MonitoringLocation:
    """
    An identifiable location where an environmental sample, onsite measurement, and/or
    observation is determined.
    """

    __monitoringLocationIdentity: MonitoringLocationIdentity
    __monitoringLocationGeospatial: MonitoringLocationGeospatial
    __wellInformation: WellInformation
    __attachedBinaryObject: List[AttachedBinaryObject]

    def __init__(
        self,
        o: dict = None,
        *,
        monitoringLocationIdentity: MonitoringLocationIdentity = None,
        monitoringLocationGeospatial: MonitoringLocationGeospatial = None,
        wellInformation: WellInformation = None,
        attachedBinaryObject: List[AttachedBinaryObject] = None
    ):
        if isinstance(o, MonitoringLocation):
            # Assign attributes from object without typechecking
            self.__monitoringLocationIdentity = o.monitoringLocationIdentity
            self.__monitoringLocationGeospatial = o.monitoringLocationGeospatial
            self.__wellInformation = o.wellInformation
            self.__attachedBinaryObject = o.attachedBinaryObject
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.monitoringLocationIdentity = o.get("monitoringLocationIdentity")
            self.monitoringLocationGeospatial = o.get("monitoringLocationGeospatial")
            self.wellInformation = o.get("wellInformation")
            self.attachedBinaryObject = o.get("attachedBinaryObject")
        else:
            # Assign attributes from named keywords with typechecking
            self.monitoringLocationIdentity = monitoringLocationIdentity
            self.monitoringLocationGeospatial = monitoringLocationGeospatial
            self.wellInformation = wellInformation
            self.attachedBinaryObject = attachedBinaryObject

    @property
    def monitoringLocationIdentity(self) -> MonitoringLocationIdentity:
        return self.__monitoringLocationIdentity

    @monitoringLocationIdentity.setter
    def monitoringLocationIdentity(self, val: MonitoringLocationIdentity) -> None:
        self.__monitoringLocationIdentity = (
            None if val is None else MonitoringLocationIdentity(val)
        )

    @property
    def monitoringLocationGeospatial(self) -> MonitoringLocationGeospatial:
        return self.__monitoringLocationGeospatial

    @monitoringLocationGeospatial.setter
    def monitoringLocationGeospatial(self, val: MonitoringLocationGeospatial) -> None:
        self.__monitoringLocationGeospatial = (
            None if val is None else MonitoringLocationGeospatial(val)
        )

    @property
    def wellInformation(self) -> WellInformation:
        return self.__wellInformation

    @wellInformation.setter
    def wellInformation(self, val: WellInformation) -> None:
        self.__wellInformation = None if val is None else WellInformation(val)

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

    def generateXML(self, name: str = "MonitoringLocation") -> str:
        doc = Doc()
        asis = doc.asis
        tag = doc.tag

        with tag(name):
            if self.__monitoringLocationIdentity is None:
                raise WQXException("Attribute 'MonitoringLocationIdentity' is required.")
            asis(
                self.__monitoringLocationIdentity.generateXML(
                    "MonitoringLocationIdentity"
                )
            )
            if self.__monitoringLocationGeospatial is None:
                raise WQXException(
                    "Attribute 'MonitoringLocationGeospatial' is required."
                )
            asis(
                self.__monitoringLocationGeospatial.generateXML(
                    "MonitoringLocationGeospatial"
                )
            )
            if self.__wellInformation is not None:
                asis(self.__wellInformation.generateXML("WellInformation"))
            for x in self.__attachedBinaryObject:
                asis(x.generateXML("AttachedBinaryObject"))

        return doc.getvalue()
