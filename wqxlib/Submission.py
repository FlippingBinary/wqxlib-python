from io import BytesIO
from zipfile import ZipFile
from .Document import Document

class Submission:
  __document: Document

  def __init__(self, o=None, *,
    document:Document = None
  ):
    if isinstance(o, Document):
      # Assign attributes from object without typechecking
      self.__document = o.document
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.document = o.get('document', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.document = document
  
  @property
  def document(self) -> Document:
    return self.__document
  @document.setter
  def document(self, val:Document) -> None:
    if val is not None and not isinstance(val, Document):
      raise TypeError("Attribute 'document' must be a Document object.")
    self.__document = None if val is None else Document(val)

  def generateZIP(self, fileName:str=None):
    if not isinstance(fileName, str):
      raise TypeError("Parameter 'fileName' must be a string.")

    mem = BytesIO()
    zip = ZipFile(mem, mode='w')

    results = self.__document.generateXML()
    zip.writestr('results.xml', results)

    # TODO: Add attachment files, if necessary. Example:
    #   zip.writestr('rawdata.csv', self.data)

    zip.close()
    mem.seek(0)

    with open(fileName, 'wb') as out:
      out.write(mem.read())
