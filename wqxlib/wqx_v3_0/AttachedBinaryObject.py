from yattag import Doc

from ..exceptions import WQXException
from .SimpleContent import BinaryObjectFileName, BinaryObjectFileTypeCode


class AttachedBinaryObject:
    """
    Reference document, image, photo, GIS data layer, laboratory material or other
    electronic object attached within a data exchange, as well as information used to
    describe the object.
    """

    __binaryObjectFileName: BinaryObjectFileName
    __binaryObjectFileTypeCode: BinaryObjectFileTypeCode

    def __init__(
        self,
        o: dict = None,
        *,
        binaryObjectFileName: BinaryObjectFileName = None,
        binaryObjectFileTypeCode: BinaryObjectFileTypeCode = None
    ):
        if isinstance(o, AttachedBinaryObject):
            # Assign attributes from object without typechecking
            self.__binaryObjectFileName = o.binaryObjectFileName
            self.__binaryObjectFileTypeCode = o.binaryObjectFileTypeCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.binaryObjectFileName = o.get("binaryObjectFileName")
            self.binaryObjectFileTypeCode = o.get("binaryObjectFileTypeCode")
        else:
            # Assign attributes from named keywords with typechecking
            self.binaryObjectFileName = binaryObjectFileName
            self.binaryObjectFileTypeCode = binaryObjectFileTypeCode

    @property
    def binaryObjectFileName(self) -> BinaryObjectFileName:
        return self.__binaryObjectFileName

    @binaryObjectFileName.setter
    def binaryObjectFileName(self, val: BinaryObjectFileName) -> None:
        self.__binaryObjectFileName = BinaryObjectFileName(val)

    @property
    def binaryObjectFileTypeCode(self) -> BinaryObjectFileTypeCode:
        return self.__binaryObjectFileTypeCode

    @binaryObjectFileTypeCode.setter
    def binaryObjectFileTypeCode(self, val: BinaryObjectFileTypeCode) -> None:
        self.__binaryObjectFileTypeCode = BinaryObjectFileTypeCode(val)

    def generateXML(self, name: str = "AttachedBinaryObject") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__binaryObjectFileName is None:
                raise WQXException("Attribute 'binaryObjectFileName' is required.")
            line("BinaryObjectFileName", self.__binaryObjectFileName)
            if self.__binaryObjectFileTypeCode is None:
                raise WQXException("Attribute 'binaryObjectFileTypeCode' is required.")
            line("BinaryObjectFileTypeCode", self.__binaryObjectFileTypeCode)

        return doc.getvalue()
