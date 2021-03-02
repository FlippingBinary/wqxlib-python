from datetime import date, time
from decimal import Decimal
from typing import Union

# TODO: Add docstrings from XSD annotations.

class ActivityConductingOrganizationText(str):
  """A name of the Organization conducting an activity."""
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("ActivityConductingOrganizationText must be between 0 and 120 characters.")

class ActivityEndDate(date):
  pass

class ActivityGroupIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("ActivityGroupIdentifier must be between 1 and 55 characters.")

class ActivityGroupName(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("ActivityGroupName must be between 0 and 120 characters.")

class ActivityGroupTypeCode(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 50:
      raise ValueError("ActivityGroupTypeCode must be between 1 and 50 characters.")

class ActivityIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("ActivityIdentifier must be between 1 and 55 characters.")

class ActivityIdentifierUserSupplied(str):
  def __init__(self, o=''):
    if len(o) > 55:
      raise ValueError("ActivityIdentifierUserSupplied must be between 0 and 55 characters.")

class ActivityLocationDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("ActivityLocationDescriptionText must be between 0 and 4000 characters.")

class ActivityMediaName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 20:
      raise ValueError("ActivityMediaName must be between 1 and 20 characters.")

class ActivityMediaSubdivisionName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ActivityMediaSubdivisionName must be between 0 and 60 characters.")

class ActivityRelativeDepthName(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("ActivityRelativeDepthName must be between 0 and 30 characters.")

class ActivityStartDate(date):
  pass

class ActivityTypeCode(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 70:
      raise ValueError("ActivityTypeCode must be between 1 and 70 characters.")

class AddressTypeName(str):
  def __init__(self, o=''):
    if len(o) > 8:
      raise ValueError("AddressTypeName must be between 0 and 8 characters.")

class AddressText(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("AddressText must be between 0 and 50 characters.")

class AnalysisEndDate(date):
  pass

class AnalysisStartDate(date):
  pass

class LocalAquiferCode(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("LocalAquiferCode must be between 0 and 120 characters.")

class LocalAquiferCodeContext(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("LocalAquiferCodeContext must be between 0 and 35 characters.")

class LocalAquiferDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 512:
      raise ValueError("LocalAquiferDescriptionText must be between 0 and 512 characters.")

class LocalAquiferName(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("LocalAquiferName must be between 0 and 255 characters.")

class AquiferTypeName(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("AquiferTypeName must be between 0 and 255 characters.")

class AssemblageSampledName(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("AssemblageSampledName must be between 0 and 50 characters.")

class BiasValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("BiasValue must be between 0 and 60 characters.")

class BiologicalIntentName(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("BiologicalIntentName must be between 0 and 35 characters.")

class BiologicalIndividualIdentifier(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("BiologicalIndividualIdentifier must be between 0 and 60 characters.")

class BinaryObjectFileName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
      raise ValueError("BinaryObjectFileName must be between 1 and 255 characters.")

class BinaryObjectFileTypeCode(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 6:
      raise ValueError("BinaryObjectFileTypeCode must be between 1 and 6 characters.")

class CellFormName(str):
  def __init__(self, o=''):
    if len(o) > 11:
      raise ValueError("CellFormName must be between 0 and 11 characters.")

class CellShapeName(str):
  def __init__(self, o=''):
    if len(o) > 18:
      raise ValueError("CellShapeName must be between 0 and 18 characters.")

class CharacteristicName(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("CharacteristicName must be between 0 and 255 characters.")

class CharacteristicNameUserSupplied(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("CharacteristicNameUserSupplied must be between 0 and 255 characters.")

class ChemicalPreservativeUsedName(str):
  def __init__(self, o=''):
    if len(o) > 250:
      raise ValueError("ChemicalPreservativeUsedName must be between 0 and 250 characters.")

class CollectionDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("CollectionDescriptionText must be between 0 and 4000 characters.")

class CommentText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("CommentText must be between 0 and 4000 characters.")

class ConfidenceIntervalValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ConfidenceIntervalValue must be between 0 and 60 characters.")

class ConstructionDate(date):
  pass

class CountryCode(str):
  def __init__(self, o=''):
    if len(o) > 2:
      raise ValueError("CountryCode must be between 0 and 2 characters.")

class CountyCode(str):
  def __init__(self, o=''):
    if len(o) > 3:
      raise ValueError("CountyCode must be between 0 and 3 characters.")

class DataLoggerLineName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("DataLoggerLineName must be between 0 and 60 characters.")

class DepthAltitudeReferencePointText(str):
  def __init__(self, o=''):
    if len(o) > 125:
      raise ValueError("DepthAltitudeReferencePointText must be between 0 and 125 characters.")

class DetectionQuantitationLimitTypeName(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("DetectionQuantitationLimitTypeName must be between 0 and 35 characters.")

class DetectionQuantitationLimitCommentText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("DetectionQuantitationLimitCommentText must be between 0 and 4000 characters.")

class ElectronicAddressText(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("ElectronicAddressText must be between 0 and 120 characters.")

class ElectronicAddressTypeName(str):
  def __init__(self, o=''):
    if len(o) > 8:
      raise ValueError("ElectronicAddressTypeName must be between 0 and 8 characters.")

class RecordIdentifierUserSupplied(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("RecordIdentifierUserSupplied must be between 0 and 60 characters.")

class FormulaDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("FormulaDescriptionText must be between 0 and 4000 characters.")

class FormationTypeText(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("FormationTypeText must be between 0 and 50 characters.")

class FrequencyClassDescriptorCode(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("FrequencyClassDescriptorCode must be between 0 and 50 characters.")

class FrequencyClassDescriptorUnitCode(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("FrequencyClassDescriptorUnitCode must be between 0 and 12 characters.")

class FunctionalFeedingGroupName(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("FunctionalFeedingGroupName must be between 0 and 30 characters.")

class GearProcedureUnitCode(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("GearProcedureUnitCode must be between 0 and 35 characters.")

class GroupSummaryCount(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("GroupSummaryCount must be between 0 and 60 characters.")

class HabitName(str):
  def __init__(self, o=''):
    if len(o) > 15:
      raise ValueError("HabitName must be between 0 and 15 characters.")

class HabitatSelectionMethod(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("HabitatSelectionMethod must be between 0 and 35 characters.")

class HorizontalCollectionMethodName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 150:
      raise ValueError("HorizontalCollectionMethodName must be between 1 and 150 characters.")

class HorizontalCoordinateReferenceSystemDatumName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 6:
      raise ValueError("HorizontalCoordinateReferenceSystemDatumName must be between 1 and 6 characters.")

class HUCEightDigitCode(str):
  def __init__(self, o=''):
    if len(o) > 8:
      raise ValueError("HUCEightDigitCode must be between 0 and 8 characters.")

class HUCTwelveDigitCode(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("HUCTwelveDigitCode must be between 0 and 12 characters.")

class HydrologicCondition(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("HydrologicCondition must be between 0 and 60 characters.")

class HydrologicEvent(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("HydrologicEvent must be between 0 and 60 characters.")

class IndexCalculatedDate(date):
  pass

class IndexIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("IndexIdentifier must be between 1 and 55 characters.")

class IndexQualifierCode(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("IndexQualifierCode must be between 0 and 35 characters.")

class IndexScore(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("IndexScore must be between 0 and 60 characters.")

class IndexTypeIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 50:
      raise ValueError("IndexTypeIdentifier must be between 1 and 50 characters.")

class IndexTypeIdentifierContext(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("IndexTypeIdentifierContext must be between 0 and 50 characters.")

class IndexTypeName(str):
  def __init__(self, o=''):
    if len(o) > 100:
      raise ValueError("IndexTypeName must be between 0 and 100 characters.")

class IndexTypeScaleText(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("IndexTypeScaleText must be between 0 and 50 characters.")

class LaboratorySampleSplitRatio(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("LaboratorySampleSplitRatio must be between 0 and 60 characters.")

class LaboratoryAccreditationIndicator(object):
  __o: bool
  def __init__(self, o=False):
    self.__o = bool(o)
  def __str__(self):
    return "True" if self.__o else "False"
  def __bool__(self):
    return self.__o

class LaboratoryAccreditationAuthorityName(str):
  def __init__(self, o=''):
    if len(o) > 20:
      raise ValueError("LaboratoryAccreditationAuthorityName must be between 0 and 20 characters.")

class LaboratoryName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("LaboratoryName must be between 0 and 60 characters.")

class LatitudeMeasure(Decimal):
  def __new__(self, o):
    s = str(o).split('.')
    totalDigits = 12
    fractionDigits = 10
    s[1] = s[1][0:min(len(s[1]),fractionDigits,max(totalDigits-len(s[0]),0))]
    return super().__new__(self,'.'.join(s))

class LocalityName(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("LocalityName must be between 0 and 30 characters.")

class LocationCategoryName(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("LocationCategoryName must be between 0 and 50 characters.")

class LocationStatusName(str):
  def __init__(self, o=''):
    if len(o) > 15:
      raise ValueError("LocationStatusName must be between 0 and 15 characters.")

class LongitudeMeasure(float):
  def __new__(self,o):
    s = str(o).split('.')
    totalDigits = 14
    fractionDigits = 11
    s[1] = s[1][0:min(len(s[1]),fractionDigits,max(totalDigits-len(s[0]),0))]
    return super().__new__(self,'.'.join(s))

class LowerConfidenceLimitValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("LowerConfidenceLimitValue must be between 0 and 60 characters.")

class LowerClassBoundValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("LowerClassBoundValue must be between 0 and 60 characters.")

class MeasureQualifierCode(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("MeasureQualifierCode must be between 0 and 35 characters.")

class MeasureUnitCode(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("MeasureUnitCode must be between 0 and 12 characters.")

class MeasureValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("MeasureValue must be between 0 and 60 characters.")

class MeasureValueTargeted(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("MeasureValueTargeted must be between 0 and 60 characters.")

class MeasureUnitCodeTargeted(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("MeasureUnitCodeTargeted must be between 0 and 12 characters.")

class MethodDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("MethodDescriptionText must be between 0 and 4000 characters.")

class MethodIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 35:
      raise ValueError("MethodIdentifier must be between 1 and 35 characters.")

class MethodIdentifierContext(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
      raise ValueError("MethodIdentifierContext must be between 1 and 120 characters.")
  
class MethodModificationText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("MethodModificationText must be between 0 and 4000 characters.")

class MethodName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 250:
      raise ValueError("MethodName must be between 1 and 250 characters.")

class MethodQualifierTypeName(str):
  def __init__(self, o=''):
    if len(o) > 25:
      raise ValueError("MethodQualifierTypeName must be between 0 and 25 characters.")

class MethodSpeciationName(str):
  def __init__(self, o=''):
    if len(o) > 20:
      raise ValueError("MethodSpeciationName must be between 0 and 20 characters.")

class MetricTypeIdentifier(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("MetricTypeIdentifier must be between 0 and 50 characters.")

class MetricTypeIdentifierContext(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("MetricTypeIdentifierContext must be between 0 and 50 characters.")

class MetricTypeName(str):
  def __init__(self, o=''):
    if len(o) > 100:
      raise ValueError("MetricTypeName must be between 0 and 100 characters.")

class MetricSamplingPointPlaceInSeries(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("MetricSamplingPointPlaceInSeries must be between 0 and 60 characters.")

class MetricScore(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("MetricScore must be between 0 and 60 characters.")

class MetricTypeScaleText(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("MetricTypeScaleText must be between 0 and 50 characters.")

class MonitoringLocationDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("MonitoringLocationDescriptionText must be between 0 and 4000 characters.")

class MonitoringLocationIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("MonitoringLocationIdentifier must be between 1 and 55 characters.")

class MonitoringLocationIdentifierContext(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
      raise ValueError("MonitoringLocationIdentifierContext must be between 1 and 120 characters.")

class MonitoringLocationName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
      raise ValueError("MonitoringLocationName must be between 1 and 255 characters.")

class MonitoringLocationTypeName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 45:
      raise ValueError("MonitoringLocationTypeName must be between 1 and 45 characters.")

class NationalAquiferCode(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("NationalAquiferCode must be between 0 and 120 characters.")

class NetTypeName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 60:
      raise ValueError("NetTypeName must be between 1 and 60 characters.")

class NewIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("NewIdentifier must be between 1 and 55 characters.")

class OldIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("OldIdentifier must be between 1 and 55 characters.")

class OrganizationDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 500:
      raise ValueError("OrganizationDescriptionText must be between 0 and 500 characters.")

class OrganizationFormalName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
      raise ValueError("OrganizationFormalName must be between 1 and 255 characters.")

class OrganizationIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 35:
      print("OrganizationIdentifier:")
      print(o)
      raise ValueError("OrganizationIdentifier must be between 1 and 35 characters.")

class PassCount(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("PassCount must be between 0 and 60 characters.")

class ProportionSampleProcessedNumeric(float):
  pass

class PostalCode(str):
  def __init__(self, o=''):
    if len(o) > 10:
      raise ValueError("PostalCode must be between 0 and 10 characters.")

class PrecisionValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("PrecisionValue must be between 0 and 60 characters.")

class PreparationEndDate(date):
  pass

class PreparationStartDate(date):
  pass

class ProjectDescriptionText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("ProjectDescriptionText must be between 0 and 4000 characters.")

class ProjectIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
      raise ValueError("ProjectIdentifier must be between 1 and 55 characters.")

class ProjectName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 512:
      raise ValueError("ProjectName must be between 1 and 512 characters.")

class QAPPApprovedIndicator(object):
  __o: bool
  def __init__(self, o=False):
    self.__o = bool(o)
  def __str__(self):
    return "True" if self.__o else "False"
  def __bool__(self):
    return self.__o

class QAPPApprovalAgencyName(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("QAPPApprovalAgencyName must be between 0 and 50 characters.")

class ReferenceLocationEndDate(date):
  pass

class ReferenceLocationStartDate(date):
  pass

class ReferenceLocationTypeCode(str):
  def __init__(self, o=''):
    if len(o) > 20:
      raise ValueError("ReferenceLocationTypeCode must be between 0 and 20 characters.")

class ResourceCreatorName(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("ResourceCreatorName must be between 0 and 120 characters.")

class ResourceDate(date):
  pass

class ResourceIdentifier(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
      raise ValueError("ResourceIdentifier must be between 1 and 255 characters.")

class ResourcePublisherName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ResourcePublisherName must be between 0 and 60 characters.")

class ResourceSubjectText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("ResourceSubjectText must be between 0 and 4000 characters.")

class ResourceTitleName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
      raise ValueError("ResourceTitleName must be between 1 and 120 characters.")

class ResultDetectionConditionText(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("ResultDetectionConditionText must be between 0 and 35 characters.")

class LaboratoryCommentText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("LaboratoryCommentText must be between 0 and 4000 characters.")

class ResultMeasureValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ResultMeasureValue must be between 0 and 60 characters.")

class ResultParticleSizeBasisText(str):
  def __init__(self, o=''):
    if len(o) > 40:
      raise ValueError("ResultParticleSizeBasisText must be between 0 and 40 characters.")

class ResultSampleFractionText(str):
  def __init__(self, o=''):
    if len(o) > 25:
      raise ValueError("ResultSampleFractionText must be between 0 and 25 characters.")

class ResultSamplingPointName(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("ResultSamplingPointName must be between 0 and 120 characters.")

class ResultSamplingPointCommentText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("ResultSamplingPointCommentText must be between 0 and 4000 characters.")

class ResultSamplingPointType(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ResultSamplingPointType must be between 0 and 60 characters.")

class ResultSamplingPointPlaceInSeries(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ResultSamplingPointPlaceInSeries must be between 0 and 60 characters.")
  
class ResultStatusIdentifier(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("ResultStatusIdentifier must be between 0 and 12 characters.")

class ResultTemperatureBasisText(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("ResultTemperatureBasisText must be between 0 and 12 characters.")

class ResultTimeBasisText(str):
  def __init__(self, o=''):
    if len(o) > 12:
      raise ValueError("ResultTimeBasisText must be between 0 and 12 characters.")

class ResultValueTypeName(str):
  def __init__(self, o=''):
    if len(o) > 20:
      raise ValueError("ResultValueTypeName must be between 0 and 20 characters.")

class ResultWeightBasisText(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("ResultWeightBasisText must be between 0 and 60 characters.")

class SampleCollectionEquipmentName(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 60:
      raise ValueError("SampleCollectionEquipmentName must be between 1 and 60 characters.")

class SampleCollectionEquipmentCommentText(str):
  def __init__(self, o=''):
    if len(o) > 4000:
      raise ValueError("SampleCollectionEquipmentCommentText must be between 0 and 4000 characters.")

class SampleContainerColorName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("SampleContainerColorName must be between 0 and 60 characters.")

class SampleContainerLabelName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("SampleContainerLabelName must be between 0 and 60 characters.")

class SampleContainerTypeName(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("SampleContainerTypeName must be between 0 and 60 characters.")

class SampleTissueAnatomyName(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("SampleTissueAnatomyName must be between 0 and 50 characters.")

class SampleTransportStorageDescription(str):
  def __init__(self, o=''):
    if len(o) > 1999:
      raise ValueError("SampleTransportStorageDescription must be between 0 and 1999 characters.")

class SamplingComponentName(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("SamplingComponentName must be between 0 and 120 characters.")

class SamplingDesignTypeCode(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 20:
      raise ValueError("SamplingDesignTypeCode must be between 1 and 20 characters.")

class SourceMapScale(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("SourceMapScale must be between 0 and 60 characters.")

class StateCode(str):
  def __init__(self, o=''):
    if len(o) > 2:
      raise ValueError("StateCode must be between 0 and 2 characters.")

class StatisticalBaseCode(str):
  def __init__(self, o=''):
    if len(o) > 25:
      raise ValueError("StatisticalBaseCode must be between 0 and 25 characters.")

class StatisticalNValueNumeric(int):
  def __init__(self, o=0):
    if o < 0:
      raise ValueError("StatisticalNValueNumeric must be a positive integer.")

class StatisticalStratumText(str):
  def __init__(self, o=''):
    if len(o) > 15:
      raise ValueError("StatisticalStratumText must be between 0 and 15 characters.")

class SubjectTaxonomicName(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("SubjectTaxonomicName must be between 0 and 255 characters.")

class SubjectTaxonomicNameUserSupplied(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("SubjectTaxonomicNameUserSupplied must be between 0 and 255 characters.")

class SubjectTaxonomicNameUserSuppliedReferenceText(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("SubjectTaxonomicNameUserSuppliedReferenceText must be between 0 and 255 characters.")

class SubstanceDilutionFactor(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("SubstanceDilutionFactor must be between 0 and 60 characters.")

class SupplementalAddressText(str):
  def __init__(self, o=''):
    if len(o) > 120:
      raise ValueError("SupplementalAddressText must be between 0 and 120 characters.")

class TargetCount(str):
  def __init__(self, o=''):
    if len(o) > 35:
      raise ValueError("TargetCount must be between 0 and 35 characters.")

class TaxonomicPollutionTolerance(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("TaxonomicPollutionTolerance must be between 0 and 30 characters.")

class TaxonomistAccreditationIndicator(object):
  __o: bool
  def __init__(self, o=False):
    self.__o = bool(o)
  def __str__(self):
    return "True" if self.__o else "False"
  def __bool__(self):
    return self.__o

class TaxonomistAccreditationAuthorityName(str):
  def __init__(self, o=''):
    if len(o) > 20:
      raise ValueError("TaxonomistAccreditationAuthorityName must be between 0 and 20 characters.")

class TaxonomicPollutionToleranceScaleText(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("TaxonomicPollutionToleranceScaleText must be between 0 and 50 characters.")

class TelephoneExtensionNumberText(str):
  def __init__(self, o=''):
    if len(o) > 6:
      raise ValueError("TelephoneExtensionNumberText must be between 0 and 6 characters.")

class TelephoneNumberText(str):
  def __init__(self, o=''):
    if len(o) > 15:
      raise ValueError("TelephoneNumberText must be between 0 and 15 characters.")

class TelephoneNumberTypeName(str):
  def __init__(self, o=''):
    if len(o) > 6:
      raise ValueError("TelephoneNumberTypeName must be between 0 and 6 characters.")

class ThermalPreservativeUsedName(str):
  def __init__(self, o=''):
    if len(o) > 250:
      raise ValueError("ThermalPreservativeUsedName must be between 0 and 250 characters.")

class Time(time):
  pass

class TimeZoneCode(str):
  def __init__(self, o=None):
    if not isinstance(o, str) or len(o) < 1 or len(o) > 4:
      raise ValueError("TimeZoneCode must be between 1 and 4 characters.")

class ToxicityTestType(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("ToxicityTestType must be between 0 and 30 characters.")

class TribalCode(str):
  def __init__(self, o=''):
    if len(o) > 3:
      raise ValueError("TribalCode must be between 0 and 3 characters.")

class TribalLandIndicator(str):
  def __new__(self, o:Union[str,bool]):
    if isinstance(o, str):
      if o.lower() in ['true', 't', 'yes', 'y', '1']:
        return super().__new__(self, 'true')
      else:
        return super().__new__(self, 'false')
    else:
      return super().__new__(self, 'true' if bool(o) else 'false')
  def __bool__(self):
    if self == 'true':
      return True
    else:
      return False

class TribalLandName(str):
  def __init__(self, o=''):
    if len(o) > 512:
      raise ValueError("TribalLandName must be between 0 and 512 characters.")

class TrophicLevelName(str):
  def __init__(self, o=''):
    if len(o) > 30:
      raise ValueError("TrophicLevelName must be between 0 and 30 characters.")

class UnidentifiedSpeciesIdentifier(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("UnidentifiedSpeciesIdentifier must be between 0 and 255 characters.")

class UpperConfidenceLimitValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("UpperConfidenceLimitValue must be between 0 and 60 characters.")

class UpperClassBoundValue(str):
  def __init__(self, o=''):
    if len(o) > 60:
      raise ValueError("UpperClassBoundValue must be between 0 and 60 characters.")

class VerticalCollectionMethodName(str):
  def __init__(self, o=''):
    if len(o) > 50:
      raise ValueError("VerticalCollectionMethodName must be between 0 and 50 characters.")

class VerticalCoordinateReferenceSystemDatumName(str):
  def __init__(self, o=''):
    if len(o) > 10:
      raise ValueError("VerticalCoordinateReferenceSystemDatumName must be between 0 and 10 characters.")

class VoltinismName(str):
  def __init__(self, o=''):
    if len(o) > 25:
      raise ValueError("VoltinismName must be between 0 and 25 characters.")

class WellTypeText(str):
  def __init__(self, o=''):
    if len(o) > 255:
      raise ValueError("WellTypeText must be between 0 and 255 characters.")

