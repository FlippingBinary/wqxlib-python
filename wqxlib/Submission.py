from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile

from .Document import Document
from .ImportConfiguration import ImportConfiguration


class Submission:
    __document: Document
    __importConfiguration: ImportConfiguration

    def __init__(
        self,
        o: dict = None,
        *,
        document: Document = None,
        importConfiguration: ImportConfiguration = None,
    ):
        if isinstance(o, Document):
            # Assign attributes from object without typechecking
            self.__document = o.document
            self.__importConfiguration = o.importConfiguration
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.document = o.get("document")
            self.importConfiguration = o.get("importConfiguration")
        else:
            # Assign attributes from named keywords with typechecking
            self.document = document
            self.importConfiguration = importConfiguration

    @property
    def document(self) -> Document:
        return self.__document

    @document.setter
    def document(self, val: Document) -> None:
        if val is not None and not isinstance(val, Document):
            raise TypeError("Attribute 'document' must be a Document object.")
        self.__document = None if val is None else Document(val)

    @property
    def importConfiguration(self) -> ImportConfiguration:
        return self.__importConfiguration

    @importConfiguration.setter
    def importConfiguration(self, val: ImportConfiguration) -> None:
        if val is not None and not isinstance(val, ImportConfiguration):
            raise TypeError(
                "Attribute 'importConfiguration' must be a ImportConfiguration object."
            )
        self.__importConfiguration = None if val is None else ImportConfiguration(val)

    #  def importData(self, data:List, *, importConfiguration:ImportConfiguration=None):
    #    ic = self.__importConfiguration if importConfiguration is None else importConfiguration
    #    for row in data:
    #      pass

    #  def importResult(self, result: dict):
    #      pass

    def generateZIP(self, fileName: str = None):
        if not isinstance(fileName, str):
            raise TypeError("Parameter 'fileName' must be a string.")

        mem = BytesIO()
        zip = ZipFile(mem, mode="w", compression=ZIP_DEFLATED)

        results = self.__document.generateXML()
        zip.writestr("results.xml", results)

        # TODO: Add attachment files, if necessary. Example:
        #   zip.writestr('rawdata.csv', self.data)

        zip.close()
        mem.seek(0)

        with open(fileName, "wb") as out:
            out.write(mem.read())
