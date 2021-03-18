from yattag import Doc

from ..exceptions import WQXException
from .MeasureCompact import MeasureCompact
from .SimpleContent import NetTypeName


class NetInformation:
    """
    Allows for the reporting of net sample collection information.
    """

    __netTypeName: NetTypeName
    __netSurfaceAreaMeasure: MeasureCompact
    __netMeshSizeMeasure: MeasureCompact
    __boatSpeedMeasure: MeasureCompact
    __currentSpeedMeasure: MeasureCompact

    def __init__(
        self,
        o: dict = None,
        *,
        netTypeName: NetTypeName = None,
        netSurfaceAreaMeasure: MeasureCompact = None,
        netMeshSizeMeasure: MeasureCompact = None,
        boatSpeedMeasure: MeasureCompact = None,
        currentSpeedMeasure: MeasureCompact = None
    ):
        if isinstance(o, NetInformation):
            # Assign attributes from object without typechecking
            self.__netTypeName = o.netTypeName
            self.__netSurfaceAreaMeasure = o.netSurfaceAreaMeasure
            self.__netMeshSizeMeasure = o.netMeshSizeMeasure
            self.__boatSpeedMeasure = o.boatSpeedMeasure
            self.__currentSpeedMeasure = o.currentSpeedMeasure
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.netTypeName = o.get("netTypeName")
            self.netSurfaceAreaMeasure = o.get("netSurfaceAreaMeasure")
            self.netMeshSizeMeasure = o.get("netMeshSizeMeasure")
            self.boatSpeedMeasure = o.get("boatSpeedMeasure")
            self.currentSpeedMeasure = o.get("currentSpeedMeasure")
        else:
            # Assign attributes from named keywords with typechecking
            self.netTypeName = netTypeName
            self.netSurfaceAreaMeasure = netSurfaceAreaMeasure
            self.netMeshSizeMeasure = netMeshSizeMeasure
            self.boatSpeedMeasure = boatSpeedMeasure
            self.currentSpeedMeasure = currentSpeedMeasure

    @property
    def netTypeName(self) -> NetTypeName:
        return self.__netTypeName

    @netTypeName.setter
    def netTypeName(self, val: NetTypeName) -> None:
        self.__netTypeName = NetTypeName(val)

    @property
    def netSurfaceAreaMeasure(self) -> MeasureCompact:
        """
        A measurement of the effective surface area of the net used during biological
        monitoring sample collection.
        """
        return self.netSurfaceAreaMeasure

    @netSurfaceAreaMeasure.setter
    def netSurfaceAreaMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the effective surface area of the net used during biological
        monitoring sample collection.
        """
        self.__netSurfaceAreaMeasure = None if val is None else MeasureCompact(val)

    @property
    def netMeshSizeMeasure(self) -> MeasureCompact:
        """
        A measurement of the mesh size of the net used during biological monitoring
        sample collection.
        """
        return self.netMeshSizeMeasure

    @netMeshSizeMeasure.setter
    def netMeshSizeMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the mesh size of the net used during biological monitoring
        sample collection.
        """
        self.__netMeshSizeMeasure = None if val is None else MeasureCompact(val)

    @property
    def boatSpeedMeasure(self) -> MeasureCompact:
        """
        A measurement of the boat speed during biological monitoring sample collection.
        """
        return self.boatSpeedMeasure

    @boatSpeedMeasure.setter
    def boatSpeedMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the boat speed during biological monitoring sample collection.
        """
        self.__boatSpeedMeasure = None if val is None else MeasureCompact(val)

    @property
    def currentSpeedMeasure(self) -> MeasureCompact:
        """
        A measurement of the current during biological monitoring sample collection.
        """
        return self.currentSpeedMeasure

    @currentSpeedMeasure.setter
    def currentSpeedMeasure(self, val: MeasureCompact) -> None:
        """
        A measurement of the current during biological monitoring sample collection.
        """
        self.__currentSpeedMeasure = None if val is None else MeasureCompact(val)

    def generateXML(self, name: str = "NetInformation") -> str:
        doc = Doc()
        asis = doc.asis
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__netTypeName is None:
                raise WQXException("Attribute 'netTypeName' is required.")
            line("NetTypeName", self.__netTypeName)
            if self.__netSurfaceAreaMeasure is not None:
                asis(self.__netSurfaceAreaMeasure.generateXML("NetSurfaceAreaMeasure"))
            if self.__netMeshSizeMeasure is not None:
                asis(self.__netMeshSizeMeasure.generateXML("NetMeshSizeMeasure"))
            if self.__boatSpeedMeasure is not None:
                asis(self.__boatSpeedMeasure.generateXML("BoatSpeedMeasure"))
            if self.__currentSpeedMeasure is not None:
                asis(self.__currentSpeedMeasure.generateXML("CurrentSpeedMeasure"))

        return doc.getvalue()
