from typing import List, Union
from yattag import Doc, indent
from .Entity_Update_Identifiers import UpdateIdentifiers
from ..common import WQXException

class WQXUpdateIdentifiers:
  """Main Schema used to update identifiers for major entities (projects, monitoring locations, activity, activity groups, and indexes)."""

  __updateIdentifiers: List[UpdateIdentifiers]

  def __init__(self, o=None, *,
    updateIdentifiers:List[UpdateIdentifiers] = None
  ):
    if isinstance(o, WQXUpdateIdentifiers):
      # Assign attributes from object without typechecking
      self.__updateIdentifiers = o.updateIdentifiers
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.updateIdentifiers = o.get('updateIdentifiers', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.updateIdentifiers = updateIdentifiers

  @property
  def updateIdentifiers(self) -> List[UpdateIdentifiers]:
    return self.__updateIdentifiers
  @updateIdentifiers.setter
  def updateIdentifiers(self, val:Union[UpdateIdentifiers,List[UpdateIdentifiers]]) -> None:
    if val is None:
      self.__updateIdentifiers = []
    elif isinstance(val, list):
      r:List[UpdateIdentifiers] = []
      for x in val:
        r.append(UpdateIdentifiers(x))
      self.__updateIdentifiers = r
    else:
      self.__updateIdentifiers = [UpdateIdentifiers(val)]

  def generateXML(self, name = 'UpdateIdentifiers') -> str:
    if self.__updateIdentifiers is None:
      raise WQXException("Attribute 'updateIdentifiers' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(
      name,
      ('xmlns','http://www.exchangenetwork.net/schema/wqx/3'),
      ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance'),
      ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')
    ):
      for x in self.__updateIdentifiers:
        doc.asis(x.generateXML('UpdateIdentifiers'))

    return doc.getvalue()