from yattag import Doc, indent
from .SimpleContent import (
  ResourceTitleName,
  ResourceCreatorName,
  ResourceSubjectText,
  ResourcePublisherName,
  ResourceDate,
  ResourceIdentifier
)
from ..common import WQXException

class BibliographicReference:
  """The descriptors used to identify and catalog an object."""

  __resourceTitleName: ResourceTitleName
  __resourceCreatorName: ResourceCreatorName
  __resourceSubjectText: ResourceSubjectText
  __resourcePublisherName: ResourcePublisherName
  __resourceDate: ResourceDate
  __resourceIdentifier: ResourceIdentifier

  def __init__(self, o=None, *,
    resourceTitleName:ResourceTitleName = None,
    resourceCreatorName:ResourceCreatorName = None,
    resourceSubjectText:ResourceSubjectText = None,
    resourcePublisherName:ResourcePublisherName = None,
    resourceDate:ResourceDate = None,
    resourceIdentifier:ResourceIdentifier = None
  ):
    if isinstance(o, BibliographicReference):
      # Assign attributes from object without typechecking
      self.__resourceTitleName = resourceTitleName
      self.__resourceCreatorName = resourceCreatorName
      self.__resourceSubjectText = resourceSubjectText
      self.__resourcePublisherName = resourcePublisherName
      self.__resourceDate = resourceDate
      self.__resourceIdentifier = resourceIdentifier
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.resourceTitleName = o.get('resourceTitleName', default = None)
      self.resourceCreatorName = o.get('resourceCreatorName', default = None)
      self.resourceSubjectText = o.get('resourceSubjectText', default = None)
      self.resourcePublisherName = o.get('resourcePublisherName', default = None)
      self.resourceDate = o.get('resourceDate', default = None)
      self.resourceIdentifier = o.get('resourceIdentifier', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.resourceTitleName = resourceTitleName
      self.resourceCreatorName = resourceCreatorName
      self.resourceSubjectText = resourceSubjectText
      self.resourcePublisherName = resourcePublisherName
      self.resourceDate = resourceDate
      self.resourceIdentifier = resourceIdentifier

  @property
  def ResourceTitleName(self) -> ResourceTitleName:
    return self.__ResourceTitleName
  @ResourceTitleName.setter
  def ResourceTitleName(self, val:ResourceTitleName) -> None:
    self.__ResourceTitleName = ResourceTitleName(val)

  @property
  def ResourceCreatorName(self) -> ResourceCreatorName:
    return self.__ResourceCreatorName
  @ResourceCreatorName.setter
  def ResourceCreatorName(self, val:ResourceCreatorName) -> None:
    self.__ResourceCreatorName = None if val is None else ResourceCreatorName(val)

  @property
  def ResourceSubjectText(self) -> ResourceSubjectText:
    return self.__ResourceSubjectText
  @ResourceSubjectText.setter
  def ResourceSubjectText(self, val:ResourceSubjectText) -> None:
    self.__ResourceSubjectText = None if val is None else ResourceSubjectText(val)

  @property
  def ResourcePublisherName(self) -> ResourcePublisherName:
    return self.__ResourcePublisherName
  @ResourcePublisherName.setter
  def ResourcePublisherName(self, val:ResourcePublisherName) -> None:
    self.__ResourcePublisherName = None if val is None else ResourcePublisherName(val)

  @property
  def ResourceDate(self) -> ResourceDate:
    return self.__ResourceDate
  @ResourceDate.setter
  def ResourceDate(self, val:ResourceDate) -> None:
    self.__ResourceDate = ResourceDate(val)

  @property
  def ResourceIdentifier(self) -> ResourceIdentifier:
    return self.__ResourceIdentifier
  @ResourceIdentifier.setter
  def ResourceIdentifier(self, val:ResourceIdentifier) -> None:
    self.__ResourceIdentifier = ResourceIdentifier(val)

  def generateXML(self):
    if self.__resourceTitleName is None:
      raise WQXException("Attribute 'ResourceTitleName' is required.")
    if self.__resourceDate is None:
      raise WQXException("Attribute 'ResourceDate' is required.")
    if self.__resourceIdentifier is None:
      raise WQXException("Attribute 'ResourceIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ResourceTitleName', self.__resourceTitleName)
    if self.__resourceCreatorName is not None:
      doc.asis(self.__resourceCreatorName.generateXML())
    if self.__resourceSubjectText is not None:
      doc.asis(self.__resourceSubjectText.generateXML())
    if self.__resourcePublisherName is not None:
      doc.asis(self.__resourcePublisherName.generateXML())
    line('ResourceDate', self.__resourceDate)
    line('ResourceIdentifier', self.__resourceIdentifier)

    return doc.getvalue()