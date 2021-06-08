from typing import List

from .wqx_v3_0 import (
    MonitoringLocation,
    MonitoringLocationGeospatial,
    MonitoringLocationIdentity,
    WellInformation,
)
from .WQXAttachedBinaryObject import WQXAttachedBinaryObject


class WQXMonitoringLocation(
    MonitoringLocation,
    MonitoringLocationGeospatial,
    MonitoringLocationIdentity,
    WellInformation,
):
    __attachedBinaryObjects: List[WQXAttachedBinaryObject] = []

    def __init__(self,):
        MonitoringLocation.__init__(self)
        MonitoringLocationGeospatial.__init__(self)
        MonitoringLocationIdentity.__init__(self)
        WellInformation.__init__(self)
        self.__attachedBinaryObjects = []

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.normalize()

    def attachedBinaryObject(self) -> WQXAttachedBinaryObject:
        tmp = WQXAttachedBinaryObject()
        self.__attachedBinaryObjects.append(tmp)
        return tmp

    def normalize(self) -> None:
        self.monitoringLocationGeospatial = MonitoringLocationGeospatial(self)
        self.monitoringLocationIdentity = MonitoringLocationIdentity(self)
        if self.wellTypeText is not None:
            self.wellInformation = WellInformation(self)
        self.attachedBinaryObject = self.__attachedBinaryObjects
