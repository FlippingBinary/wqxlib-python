from yattag import Doc, indent
from .ReferenceMethod import ReferenceMethod
from .SamplePreparation import SamplePreparation
from .SimpleContent import *
from ..WQXException import WQXException

class SampleDescription:
  """Basic identification information for the sample collected as part of a monitoring activity."""

  __sampleCollectionMethod: ReferenceMethod
  __sampleCollectionEquipmentName: SampleCollectionEquipmentName
  __sampleCollectionEquipmentCommentText: SampleCollectionEquipmentCommentText
  __samplePreparation: SamplePreparation
  __hydrologicCondition: HydrologicCondition
  __hydrologicEvent: HydrologicEvent

  def __init__(self):
    self.__sampleCollectionMethod = None
    self.__sampleCollectionEquipmentName = None
    self.__sampleCollectionEquipmentCommentText = None
    self.__samplePreparation = None
    self.__hydrologicCondition = None
    self.__hydrologicEvent = None

  @property
  def sampleCollectionMethod(self) -> ReferenceMethod:
    """Identifies sample collection or measurement method procedures. Where a documented sample collection method has been employed, this enables the data provider to indicate the documented method that was employed during the field sample collection. Otherwise, the sample collection procedure will best be described in a freeform text."""
    return self.__sampleCollectionMethod
  @property
  def sampleCollectionMethod(self, val:ReferenceMethod) -> None:
    """Identifies sample collection or measurement method procedures. Where a documented sample collection method has been employed, this enables the data provider to indicate the documented method that was employed during the field sample collection. Otherwise, the sample collection procedure will best be described in a freeform text."""
    self.__sampleCollectionMethod = val

  @property
  def sampleCollectionEquipmentName(self) -> SampleCollectionEquipmentName:
    return self.__sampleCollectionEquipmentName
  @sampleCollectionEquipmentName.setter
  def sampleCollectionEquipmentName(self, val:SampleCollectionEquipmentName) -> None:
    self.__sampleCollectionEquipmentName = SampleCollectionEquipmentName(val)

  @property
  def sampleCollectionEquipmentCommentText(self) -> SampleCollectionEquipmentCommentText:
    return self.__sampleCollectionEquipmentCommentText
  @sampleCollectionEquipmentCommentText.setter
  def sampleCollectionEquipmentCommentText(self, val:SampleCollectionEquipmentCommentText) -> None:
    self.__sampleCollectionEquipmentCommentText = None if val is None else SampleCollectionEquipmentCommentText(val)

  @property
  def samplePreparation(self) -> SamplePreparation:
    return self.__samplePreparation
  @property
  def samplePreparation(self, val:SamplePreparation) -> None:
    self.__samplePreparation = val

  @property
  def hydrologicCondition(self) -> HydrologicCondition:
    return self.__hydrologicCondition
  @hydrologicCondition.setter
  def hydrologicCondition(self, val:HydrologicCondition) -> None:
    self.__hydrologicCondition = None if val is None else HydrologicCondition(val)

  @property
  def hydrologicEvent(self) -> HydrologicEvent:
    return self.__hydrologicEvent
  @hydrologicEvent.setter
  def hydrologicEvent(self, val:HydrologicEvent) -> None:
    self.__hydrologicEvent = None if val is None else HydrologicEvent(val)

  def generateXML(self):
    if self.__sampleCollectionEquipmentName is None:
      WQXException("Attribute 'sampleCollectionEquipmentName' is required.")

    doc, tag, text, line = Doc().ttl()

    if self.__sampleCollectionMethod is not None:
      with tag('SampleCollectionMethod'):
        doc.asis(self.__sampleCollectionMethod.generateXML())
    line('SampleCollectionEquipmentName', self.__sampleCollectionEquipmentName)
    if self.__sampleCollectionEquipmentCommentText is not None:
      line('SampleCollectionEquipmentCommentText', self.__sampleCollectionEquipmentCommentText)
    if self.__samplePreparation is not None:
      with tag('SamplePreparation'):
        doc.asis(self.__samplePreparation.generateXML())
    if self.__hydrologicCondition is not None:
      line('HydrologicCondition', self.__hydrologicCondition)
    if self.__hydrologicEvent is not None:
      line('HydrologicEvent', self.__hydrologicEvent)

    return indent(doc.getvalue(), indentation = ' '*2)
