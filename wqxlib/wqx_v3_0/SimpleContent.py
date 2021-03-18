from datetime import date, time
from decimal import Decimal
from typing import Union


class ActivityConductingOrganizationText(str):
    """
    A name of the Organization conducting an activity.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError(
                "ActivityConductingOrganizationText must be between 0 and 120 "
                "characters."
            )


class ActivityEndDate(date):
    """
    The calendar date when the field activity was completed.
    """

    pass


class ActivityGroupIdentifier(str):
    """
    Designator that uniquely identifies a grouping of activities within an organization.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError(
                "ActivityGroupIdentifier must be between 1 and 55 characters."
            )


class ActivityGroupName(str):
    """
    A name of an activity group.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError("ActivityGroupName must be between 0 and 120 characters.")


class ActivityGroupTypeCode(str):
    """
    Identifies the type of grouping of a set of activities.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 50:
            raise ValueError(
                "ActivityGroupTypeCode must be between 1 and 50 " "characters."
            )


class ActivityIdentifier(str):
    """
    Designator that uniquely identifies an activity within an organization.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError("ActivityIdentifier must be between 1 and 55 characters.")


class ActivityIdentifierUserSupplied(str):
    """
    User Supplied Sample ID that uniquely identifies an activity within an organization.
    """

    def __init__(self, o=""):
        if len(o) > 55:
            raise ValueError(
                "ActivityIdentifierUserSupplied must be between 0 and 55 characters."
            )


class ActivityLocationDescriptionText(str):
    """
    Text description of the activity location.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "ActivityLocationDescriptionText must be between 0 and 4000 characters."
            )


class ActivityMediaName(str):
    """
    Name or code indicating the environmental medium where the sample was taken.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 20:
            raise ValueError("ActivityMediaName must be between 1 and 20 characters.")


class ActivityMediaSubdivisionName(str):
    """
    Name or code indicating the environmental matrix as a subdivision of the sample
    media.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "ActivityMediaSubdivisionName must be between 0 and 60 characters."
            )


class ActivityRelativeDepthName(str):
    """
    The name that indicates the approximate location within the water column at which
    the activity occurred.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError(
                "ActivityRelativeDepthName must be between 0 and 30 characters."
            )


class ActivityStartDate(date):
    """
    The calendar date on which the field activity was started.
    """

    pass


class ActivityTypeCode(str):
    """
    The text describing the type of activity.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 70:
            raise ValueError("ActivityTypeCode must be between 1 and 70 characters.")


class AddressText(str):
    """
    The address that describes the physical (geographic), shipping, or mailing location
    of an organization.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("AddressText must be between 0 and 50 characters.")


class AddressTypeName(str):
    """
    Categorizes an address as either location, shipping, or mailing address.
    """

    def __init__(self, o=""):
        if len(o) > 8:
            raise ValueError("AddressTypeName must be between 0 and 8 characters.")


class AnalysisEndDate(date):
    """
    The calendar date on which the analysis was finished.
    """

    pass


class AnalysisStartDate(date):
    """
    The calendar date on which the analysis began.
    """

    pass


class LocalAquiferCode(str):
    """
    The identification number or code assigned by the aquifer publisher.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError("LocalAquiferCode must be between 0 and 120 characters.")


class LocalAquiferCodeContext(str):
    """
    The code that Identifies the source or data system that created or defined the
    identifier.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError(
                "LocalAquiferCodeContext must be between 0 and 35 characters."
            )


class LocalAquiferDescriptionText(str):
    """
    Information that further describes an aquifer.
    """

    def __init__(self, o=""):
        if len(o) > 512:
            raise ValueError(
                "LocalAquiferDescriptionText must be between 0 and 512 characters."
            )


class LocalAquiferName(str):
    """
    The name associated with the aquifer from the aquifer publisher.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError("LocalAquiferName must be between 0 and 255 characters.")


class AquiferTypeName(str):
    """
    The type of aquifer, such as confined or unconfined.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError("AquiferTypeName must be between 0 and 255 characters.")


class AssemblageSampledName(str):
    """
    An association of interacting populations of organisms in a given waterbody.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "AssemblageSampledName must be between 0 and 50 " "characters."
            )


class BiasValue(str):
    """
    The systematic or persistent distortion of a measurement process which causes error
    in one direction.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("BiasValue must be between 0 and 60 characters.")


class BiologicalIntentName(str):
    """
    The primary reason the biological monitoring has occurred.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError("BiologicalIntentName must be between 0 and 35 characters.")


class BiologicalIndividualIdentifier(str):
    """
    A number uniquely identifying the individual in accordance with the total number of
    individuals reported by the user.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "BiologicalIndividualIdentifier must be between 0 and 60 characters."
            )


class BinaryObjectFileName(str):
    """
    The text describing the descriptive name used to represent the file, including file
    extension.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
            raise ValueError(
                "BinaryObjectFileName must be between 1 and 255 " "characters."
            )


class BinaryObjectFileTypeCode(str):
    """
    The text or acronym describing the binary content type of a file.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 6:
            raise ValueError(
                "BinaryObjectFileTypeCode must be between 1 and 6 characters."
            )


class CellFormName(str):
    """
    The name of the cell form for phytoplankton organisms expressed as a result. A single
    phytoplankton species may have a result value for any or all of these cell forms.
    """

    def __init__(self, o=""):
        if len(o) > 11:
            raise ValueError("CellFormName must be between 0 and 11 characters.")


class CellShapeName(str):
    """
    The cell shape of the phytoplankton organism.
    """

    def __init__(self, o=""):
        if len(o) > 18:
            raise ValueError("CellShapeName must be between 0 and 18 characters.")


class CharacteristicName(str):
    """
    The object, property, or substance which is evaluated or enumerated by either a
    direct field measurement, a direct field observation, or by laboratory analysis of
    material collected in the field.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError("CharacteristicName must be between 0 and 255 characters.")


class CharacteristicNameUserSupplied(str):
    """
    The object, property, or substance which is evaluated or enumerated by either a
    direct field measurement, a direct field observation, or by laboratory analysis of
    material collected in the field.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError(
                "CharacteristicNameUserSupplied must be between 0 and 255 characters."
            )


class ChemicalPreservativeUsedName(str):
    """
    Information describing the chemical means to preserve the sample.
    """

    def __init__(self, o=""):
        if len(o) > 250:
            raise ValueError(
                "ChemicalPreservativeUsedName must be between 0 and 250 characters."
            )


class CollectionDescriptionText(str):
    """
    Remark / Text description of the reach length.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "CollectionDescriptionText must be between 0 and 4000 characters."
            )


class CommentText(str):
    """
    Free text with general comments.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError("CommentText must be between 0 and 4000 characters.")


class ConfidenceIntervalValue(str):
    """
    A range of values constructed so that this range has a specified probability of
    including the true population mean.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "ConfidenceIntervalValue must be between 0 and 60 characters."
            )


class ConstructionDate(date):
    """
    Date of construction when well was completed.
    """

    pass


class CountryCode(str):
    """
    A code designator used to identify a primary geopolitical unit of the world.
    """

    def __init__(self, o=""):
        if len(o) > 2:
            raise ValueError("CountryCode must be between 0 and 2 characters.")


class CountyCode(str):
    """
    A code designator used to identify a U.S. county or county equivalent.
    """

    def __init__(self, o=""):
        if len(o) > 3:
            raise ValueError("CountyCode must be between 0 and 3 characters.")


class DataLoggerLineName(str):
    """
    The unique line identifier from a data logger result text file, normally a date/time
    format but could be any user defined name, e.g. "surface", "midwinter", and or
    "bottom".
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("DataLoggerLineName must be between 0 and 60 characters.")


class DepthAltitudeReferencePointText(str):
    """
    The reference used to indicate the datum or reference used to establish a
    depth/altitude measurement.
    """

    def __init__(self, o=""):
        if len(o) > 125:
            raise ValueError(
                "DepthAltitudeReferencePointText must be between 0 and 125 characters."
            )


class DetectionQuantitationLimitTypeName(str):
    """
    Text describing the type of detection or quantitation level used in the analysis of
    a characteristic.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError(
                "DetectionQuantitationLimitTypeName must be between 0 and 35 characters."
            )


class DetectionQuantitationLimitCommentText(str):
    """
    Text providing further description and comment on the detection and/or quantitation
    limits.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "DetectionQuantitationLimitCommentText must be between 0 and 4000 "
                "characters."
            )


class ElectronicAddressText(str):
    """
    A resource address, usually consisting of the access protocol, the domain name, and
    optionally, the path to a file or location.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError(
                "ElectronicAddressText must be between 0 and 120 characters."
            )


class ElectronicAddressTypeName(str):
    """
    The name that describes the electronic address type.
    """

    def __init__(self, o=""):
        if len(o) > 8:
            raise ValueError(
                "ElectronicAddressTypeName must be between 0 and 8 characters."
            )


class RecordIdentifierUserSupplied(str):
    """
    The user supplied record identifier associated with data entered.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "RecordIdentifierUserSupplied must be between 0 and 60 characters."
            )


class FormulaDescriptionText(str):
    """
    Provides a description of the formula used to calculate the activity metric score.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "FormulaDescriptionText must be between 0 and 4000 characters."
            )


class FormationTypeText(str):
    """
    Name of the primary formation or soils unit, in which the well is completed.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("FormationTypeText must be between 0 and 50 characters.")


class FrequencyClassDescriptorCode(str):
    """
    A code that describes the frequency class, either as a life stage, abnormality,
    gender, or measurable characteristic (i.e. length, weight) used to categorize a
    biological population count.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "FrequencyClassDescriptorCode must be between 0 and 50 characters."
            )


class FrequencyClassDescriptorUnitCode(str):
    """
    The code that represents the unit for measuring the item.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError(
                "FrequencyClassDescriptorUnitCode must be between 0 and 12 characters."
            )


class FunctionalFeedingGroupName(str):
    """
    For entries representing taxa, a code representing the functional feeding group with
    which the reported taxon is typically associated.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError(
                "FunctionalFeedingGroupName must be between 0 and 30 characters."
            )


class GearProcedureUnitCode(str):
    """
    The procedural code or equipment that represents the unit for measuring the effort.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError(
                "GearProcedureUnitCode must be between 0 and 35 " "characters."
            )


class GroupSummaryCount(str):
    """
    Captures the total count for a Group Summary.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("GroupSummaryCount must be between 0 and 60 characters.")


class HabitName(str):
    """
    The position that the characteristic occupies in a food chain.
    """

    def __init__(self, o=""):
        if len(o) > 15:
            raise ValueError("HabitName must be between 0 and 15 characters.")


class HabitatSelectionMethod(str):
    """
    The monitoring approach by which each habitat was chosen to sample. (e.g. random).
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError(
                "HabitatSelectionMethod must be between 0 and 35 characters."
            )


class HorizontalCollectionMethodName(str):
    """
    The name that identifies the method used to determine the latitude and longitude
    coordinates for a point on the earth.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 150:
            raise ValueError(
                "HorizontalCollectionMethodName must be between 1 and 150 characters."
            )


class HorizontalCoordinateReferenceSystemDatumName(str):
    """
    The name that describes the reference datum used in determining latitude and
    longitude coordinates.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 6:
            raise ValueError(
                "HorizontalCoordinateReferenceSystemDatumName must be between 1 and 6 "
                "characters."
            )


class HUCEightDigitCode(str):
    """
    The 8 digit federal code used to identify the hydrologic unit of the monitoring
    location to the cataloging unit level of precision.
    """

    def __init__(self, o=""):
        if len(o) > 8:
            raise ValueError("HUCEightDigitCode must be between 0 and 8 characters.")


class HUCTwelveDigitCode(str):
    """
    The 12 digit federal code used to identify the hydrologic unit of the monitoring
    location to the subwatershed level of precision.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError("HUCTwelveDigitCode must be between 0 and 12 characters.")


class HydrologicCondition(str):
    """
    Hydrologic condition is the hydrologic condition that is represented by the sample
    collected (i.e. ? normal, falling, rising, peak stage).
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("HydrologicCondition must be between 0 and 60 characters.")


class HydrologicEvent(str):
    """
    A hydrologic event that is represented by the sample collected (i.e. - storm,
    drought, snowmelt).
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("HydrologicEvent must be between 0 and 60 characters.")


class IndexCalculatedDate(date):
    """
    Date on which the index was calcualted.
    """

    pass


class IndexIdentifier(str):
    """
    A unique designator used to identify a unique index record that the activity metric
    is associated with.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError("IndexIdentifier must be between 1 and 55 characters.")


class IndexQualifierCode(str):
    """
    A code used to identify any qualifying issues that affect the index.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError("IndexQualifierCode must be between 0 and 35 characters.")


class IndexScore(str):
    """
    Provides the score for the index.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("IndexScore must be between 0 and 60 characters.")


class IndexTypeIdentifier(str):
    """
    A designator used to describe the unique name, number, or code assigned to identify
    the index (Organization specific).
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 50:
            raise ValueError("IndexTypeIdentifier must be between 1 and 50 characters.")


class IndexTypeIdentifierContext(str):
    """
    Identifies the source or data system that created or defined the index.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "IndexTypeIdentifierContext must be between 0 and 50 characters."
            )


class IndexTypeName(str):
    """
    Name of the habitat or biotic integrity index.
    """

    def __init__(self, o=""):
        if len(o) > 100:
            raise ValueError("IndexTypeName must be between 0 and 100 characters.")


class IndexTypeScaleText(str):
    """
    Provides a description of the scale used for the index.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("IndexTypeScaleText must be between 0 and 50 characters.")


class LaboratoryAccreditationIndicator(object):
    """
    Indicates whether the laboratory is accredited.
    """

    __o: bool

    def __init__(self, o=False):
        self.__o = bool(o)

    def __str__(self):
        return "True" if self.__o else "False"

    def __bool__(self):
        return self.__o


class LaboratoryAccreditationAuthorityName(str):
    """
    An outside accreditation authority identifier.
    """

    def __init__(self, o=""):
        if len(o) > 20:
            raise ValueError(
                "LaboratoryAccreditationAuthorityName must be between 0 and 20 "
                "characters."
            )


class LaboratoryName(str):
    """
    The name of Lab responsible for the result.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("LaboratoryName must be between 0 and 60 characters.")


class LaboratorySampleSplitRatio(str):
    """
    The proportion of all of the material collected that was sent to lab for analysis.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "LaboratorySampleSplitRatio must be between 0 and 60 characters."
            )


class LatitudeMeasure(Decimal):
    """
    The measure of the angular distance on a meridian north or south of the equator.
    """

    def __new__(cls, o):
        s = str(o).split(".")
        totalDigits = 12
        fractionDigits = 10
        s[1] = s[1][0 : min(len(s[1]), fractionDigits, max(totalDigits - len(s[0]), 0))]
        return super().__new__(cls, ".".join(s))


class LocalityName(str):
    """
    The name of a city, town, village or other locality.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError("LocalityName must be between 0 and 30 characters.")


class LocationCategoryName(str):
    """
    Free text describing a category of naturally similar site types, such as
    high-gradient.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("LocationCategoryName must be between 0 and 50 characters.")


class LocationStatusName(str):
    """
    Indicates whether this site is active and available for sampling.
    """

    def __init__(self, o=""):
        if len(o) > 15:
            raise ValueError("LocationStatusName must be between 0 and 15 characters.")


class LongitudeMeasure(float):
    """
    The measure of the angular distance on a meridian east or west of the prime meridian.
    """

    def __new__(cls, o):
        s = str(o).split(".")
        totalDigits = 14
        fractionDigits = 11
        s[1] = s[1][0 : min(len(s[1]), fractionDigits, max(totalDigits - len(s[0]), 0))]
        return super().__new__(cls, ".".join(s))


class LowerConfidenceLimitValue(str):
    """
    Value of the lower end of the confidence interval.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "LowerConfidenceLimitValue must be between 0 and 60 characters."
            )


class LowerClassBoundValue(str):
    """
    This described the lower bound for a frequency class descriptor.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("LowerClassBoundValue must be between 0 and 60 characters.")


class MeasureQualifierCode(str):
    """
    A code used to identify any qualifying issues that affect the results.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError("MeasureQualifierCode must be between 0 and 35 characters.")


class MeasureUnitCode(str):
    """
    The code that represents the unit for measuring the item.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError("MeasureUnitCode must be between 0 and 12 characters.")


class MeasureValue(str):
    """
    The recorded dimension, capacity, quality, or amount of something ascertained by
    measuring or observing.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("MeasureValue must be between 0 and 60 characters.")


class MeasureValueTargeted(str):
    """
    The targeted value of the recorded dimension, capacity, quality, or amount of
    something ascertained by measuring or observing.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("MeasureValueTargeted must be between 0 and 60 characters.")


class MeasureUnitCodeTargeted(str):
    """
    The code that represents the unit for measuring the item.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError(
                "MeasureUnitCodeTargeted must be between 0 and 12 characters."
            )


class MethodDescriptionText(str):
    """
    A brief summary that provides general information about the method.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "MethodDescriptionText must be between 0 and 4000 characters."
            )


class MethodIdentifier(str):
    """
    The identification number or code assigned by the method publisher.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 35:
            raise ValueError("MethodIdentifier must be between 1 and 35 characters.")


class MethodIdentifierContext(str):
    """
    Identifies the source or data system that created or defined the identifier.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
            raise ValueError(
                "MethodIdentifierContext must be between 1 and 120 characters."
            )


class MethodModificationText(str):
    """
    A brief summary that provides general information about the modification of the
    method.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "MethodModificationText must be between 0 and 4000 characters."
            )


class MethodName(str):
    """
    The title that appears on the method from the method publisher.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 250:
            raise ValueError("MethodName must be between 1 and 250 characters.")


class MethodQualifierTypeName(str):
    """
    Identifier of type of method that identifies it as reference, equivalent, or other.
    """

    def __init__(self, o=""):
        if len(o) > 25:
            raise ValueError(
                "MethodQualifierTypeName must be between 0 and 25 characters."
            )


class MethodSpeciationName(str):
    """
    Identifies the chemical speciation in which the measured result is expressed.
    """

    def __init__(self, o=""):
        if len(o) > 20:
            raise ValueError("MethodSpeciationName must be between 0 and 20 characters.")


class MetricTypeIdentifier(str):
    """
    A designator used to describe the unique name, number, or code assigned to identify
    the metric (Organization specific).
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("MetricTypeIdentifier must be between 0 and 50 characters.")


class MetricTypeIdentifierContext(str):
    """
    Identifies the source or data system that created or defined the metric.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "MetricTypeIdentifierContext must be between 0 and 50 characters."
            )


class MetricTypeName(str):
    """
    Name of the activity metric.
    """

    def __init__(self, o=""):
        if len(o) > 100:
            raise ValueError("MetricTypeName must be between 0 and 100 characters.")


class MetricSamplingPointPlaceInSeries(str):
    """
    The order in which a single point within a sampling frame was visited in relation to
    other components.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "MetricSamplingPointPlaceInSeries must be between 0 and 60 characters."
            )


class MetricScore(str):
    """
    Provides the scaled or calculated score for the activity metric.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("MetricScore must be between 0 and 60 characters.")


class MetricTypeScaleText(str):
    """
    Provides a description of the scale used for the activity metric.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError("MetricTypeScaleText must be between 0 and 50 characters.")


class MonitoringLocationDescriptionText(str):
    """
    Text description of the monitoring location.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "MonitoringLocationDescriptionText must be between 0 and 4000 characters."
            )


class MonitoringLocationIdentifier(str):
    """
    A designator used to describe the unique name, number, or code assigned to identify
    the monitoring location.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError(
                "MonitoringLocationIdentifier must be between 1 and 55 characters."
            )


class MonitoringLocationIdentifierContext(str):
    """
    Identifies the source or data system that created or defined the monitoring location
    identifier.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
            raise ValueError(
                "MonitoringLocationIdentifierContext must be between 1 and 120 "
                "characters."
            )


class MonitoringLocationName(str):
    """
    The designator specified by the sampling organization for the site at which sampling
    or other activities are conducted.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
            raise ValueError(
                "MonitoringLocationName must be between 1 and 255 characters."
            )


class MonitoringLocationTypeName(str):
    """
    The descriptive name for a type of monitoring location.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 45:
            raise ValueError(
                "MonitoringLocationTypeName must be between 1 and 45 characters."
            )


class NationalAquiferCode(str):
    """
    Code of the aquifer in which the well is completed.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError("NationalAquiferCode must be between 0 and 120 characters.")


class NetTypeName(str):
    """
    The text describing the type of net.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 60:
            raise ValueError("NetTypeName must be between 1 and 60 characters.")


class NewIdentifier(str):
    """
    The new identifier which replaces an older one.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError("NewIdentifier must be between 1 and 55 characters.")


class OldIdentifier(str):
    """
    The old identifier which will be replaced.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError("OldIdentifier must be between 1 and 55 characters.")


class OrganizationDescriptionText(str):
    """
    Information that further describes an organization.
    """

    def __init__(self, o=""):
        if len(o) > 500:
            raise ValueError(
                "OrganizationDescriptionText must be between 0 and 500 characters."
            )


class OrganizationFormalName(str):
    """
    The legal designator (i.e. formal name) of an organization.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
            raise ValueError(
                "OrganizationFormalName must be between 1 and 255 characters."
            )


class OrganizationIdentifier(str):
    """
    A designator used to uniquely identify a unique business establishment within a
    context.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 35:
            print("OrganizationIdentifier:")
            print(o)
            raise ValueError(
                "OrganizationIdentifier must be between 1 and 35 characters."
            )


class PassCount(str):
    """
    The number of passes through the water from which the sample was collected.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("PassCount must be between 0 and 60 characters.")


class ProportionSampleProcessedNumeric(float):
    """
    This field captures the proportion of the sample processed. Proportion is stored as a
    number between 0 and 1. Large/rare count would be documented as 1 (100%).
    """

    pass


class PostalCode(str):
    """
    The combination of the 5-digit Zone Improvement Plan (ZIP) code and the four-digit
    extension code (if available) that represents the geographic segment that is a
    subunit of the ZIP Code, assigned by the U.S. Postal Service to a geographic location
    to facilitate mail delivery; or the postal zone specific to the country, other than
    the U.S., where the mail is delivered.
    """

    def __init__(self, o=""):
        if len(o) > 10:
            raise ValueError("PostalCode must be between 0 and 10 characters.")


class PrecisionValue(str):
    """
    A measure of mutual agreement among individual measurements of the same property
    usually under prescribed similar conditions.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("PrecisionValue must be between 0 and 60 characters.")


class PreparationEndDate(date):
    """
    The calendar date when the preparation/extraction of the sample for analysis was
    finished.
    """

    pass


class PreparationStartDate(date):
    """
    The calendar date when the preparation/extraction of the sample for analysis began.
    """

    pass


class ProjectDescriptionText(str):
    """
    Project description, which may include a description of the project purpose, summary
    of the objectives, or brief summary of the results of the project.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "ProjectDescriptionText must be between 0 and 4000 characters."
            )


class ProjectIdentifier(str):
    """
    A designator used to uniquely identify a data collection project within a context of
    an organization.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 55:
            raise ValueError("ProjectIdentifier must be between 1 and 55 characters.")


class ProjectName(str):
    """
    The name assigned by the Organization (project leader or principal investigator) to
    the project.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 512:
            raise ValueError("ProjectName must be between 1 and 512 characters.")


class QAPPApprovedIndicator(object):
    """
    Indicates whether a Quality Assurance Project Plan (QAPP) has been approved for the
    submitted project.
    """

    __o: bool

    def __init__(self, o=False):
        self.__o = bool(o)

    def __str__(self):
        return "True" if self.__o else "False"

    def __bool__(self):
        return self.__o


class QAPPApprovalAgencyName(str):
    """
    An outside approval authority identifier for the QAPP (e.g. EPA or State
    Organization).
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "QAPPApprovalAgencyName must be between 0 and 50 characters."
            )


class ReferenceLocationEndDate(date):
    """
    The calendar date on which the monitoring location stopped being used as a reference
    site.
    """

    pass


class ReferenceLocationStartDate(date):
    """
    The calendar date on which the monitoring location started being used as a reference
    site.
    """

    pass


class ReferenceLocationTypeCode(str):
    """
    Identifies whether this site is a reference or control site by specifying the
    reference location type.
    """

    def __init__(self, o=""):
        if len(o) > 20:
            raise ValueError(
                "ReferenceLocationTypeCode must be between 0 and 20 characters."
            )


class ResourceCreatorName(str):
    """
    An entity primarily responible for making the content of the resource.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError("ResourceCreatorName must be between 0 and 120 characters.")


class ResourceDate(date):
    """
    A date of an event in the lifecycle of the resource.
    """

    pass


class ResourceIdentifier(str):
    """
    An unambiguous reference to the resource within a given context.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 255:
            raise ValueError("ResourceIdentifier must be between 1 and 255 characters.")


class ResourcePublisherName(str):
    """
    An entity responsible for making the resource available.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("ResourcePublisherName must be between 0 and 60 characters.")


class ResourceSubjectText(str):
    """
    A topic of the content of the resource.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError("ResourceSubjectText must be between 0 and 4000 characters.")


class ResourceTitleName(str):
    """
    A name given to the resource.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 120:
            raise ValueError("ResourceTitleName must be between 1 and 120 characters.")


class ResultDetectionConditionText(str):
    """
    The textual descriptor of a result.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError(
                "ResultDetectionConditionText must be between 0 and 35 characters."
            )


class LaboratoryCommentText(str):
    """
    Remarks which further describe the laboratory procedures which produced the result.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "LaboratoryCommentText must be between 0 and 4000 characters."
            )


class ResultMeasureValue(str):
    """
    The reportable measure of the result for the chemical, microbiological or other
    characteristic being analyzed.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("ResultMeasureValue must be between 0 and 60 characters.")


class ResultParticleSizeBasisText(str):
    """
    User defined free text describing the particle size class for which the associated
    result is defined.
    """

    def __init__(self, o=""):
        if len(o) > 40:
            raise ValueError(
                "ResultParticleSizeBasisText must be between 0 and 40 characters."
            )


class ResultSampleFractionText(str):
    """
    The text name of the portion of the sample associated with results obtained from a
    physically-partitioned sample.
    """

    def __init__(self, o=""):
        if len(o) > 25:
            raise ValueError(
                "ResultSampleFractionText must be between 0 and 25 characters."
            )


class ResultSamplingPointName(str):
    """
    Single point name within a sampling frame or protocol that is associated with the
    reported result.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError(
                "ResultSamplingPointName must be between 0 and 120 characters."
            )


class ResultSamplingPointCommentText(str):
    """
    Text description of a single point within a sampling frame for the result.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "ResultSamplingPointCommentText must be between 0 and 4000 characters."
            )


class ResultSamplingPointType(str):
    """
    Location of a Single point within a sampling frame or position that is associated
    with the reported result.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "ResultSamplingPointType must be between 0 and 60 characters."
            )


class ResultSamplingPointPlaceInSeries(str):
    """
    The order in which a single point within a sampling frame was visited in relation to
    other components.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "ResultSamplingPointPlaceInSeries must be between 0 and 60 characters."
            )


class ResultStatusIdentifier(str):
    """
    Indicates the acceptability of the result with respect to QA/QC criteria.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError(
                "ResultStatusIdentifier must be between 0 and 12 characters."
            )


class ResultTemperatureBasisText(str):
    """
    The name that represents the controlled temperature at which the sample was
    maintained during analysis, e.g. 25 deg BOD analysis.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError(
                "ResultTemperatureBasisText must be between 0 and 12 characters."
            )


class ResultTimeBasisText(str):
    """
    The period of time (in days) over which a measurement was made. For example, BOD can
    be measured as 5 day or 20 day BOD.
    """

    def __init__(self, o=""):
        if len(o) > 12:
            raise ValueError("ResultTimeBasisText must be between 0 and 12 characters.")


class ResultValueTypeName(str):
    """
    A name that qualifies the process which was used in the determination of the result
    value (e.g., actual, estimated, calculated).
    """

    def __init__(self, o=""):
        if len(o) > 20:
            raise ValueError("ResultValueTypeName must be between 0 and 20 characters.")


class ResultWeightBasisText(str):
    """
    The name that represents the form of the sample or portion of the sample which is
    associated with the result value (e.g., wet weight, dry weight, ash-free dry weight).
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("ResultWeightBasisText must be between 0 and 60 characters.")


class SampleCollectionEquipmentCommentText(str):
    """
    Free text with general comments further describing the sample collection equipment.
    """

    def __init__(self, o=""):
        if len(o) > 4000:
            raise ValueError(
                "SampleCollectionEquipmentCommentText must be between 0 and 4000 "
                "characters."
            )


class SampleCollectionEquipmentName(str):
    """
    The name for the equipment used in collecting the sample.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 60:
            raise ValueError(
                "SampleCollectionEquipmentName must be between 1 and 60 characters."
            )


class SampleContainerColorName(str):
    """
    The text describing the sample container color.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "SampleContainerColorName must be between 0 and 60 characters."
            )


class SampleContainerLabelName(str):
    """
    The identification number or code assigned by the LAB or data collector. Sample
    Identification Codes and Labeling.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "SampleContainerLabelName must be between 0 and 60 characters."
            )


class SampleContainerTypeName(str):
    """
    The text describing the sample container type.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "SampleContainerTypeName must be between 0 and 60 characters."
            )


class SampleTissueAnatomyName(str):
    """
    The name of the anatomy from which a tissue sample was taken.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "SampleTissueAnatomyName must be between 0 and 50 characters."
            )


class SampleTransportStorageDescription(str):
    """
    The text describing sample handling and transport procedures used.
    """

    def __init__(self, o=""):
        if len(o) > 1999:
            raise ValueError(
                "SampleTransportStorageDescription must be between 0 and 1999 "
                "characters."
            )


class SamplingComponentName(str):
    """
    Single entity within a sampling frame at which a collection procedure or protocol
    was performed (e.g. transect, plot point).
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError(
                "SamplingComponentName must be between 0 and 120 characters."
            )


class SamplingDesignTypeCode(str):
    """
    A code used to identify the type of sampling design employed for this project to
    ensure that sampling activities can support project objectives.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 20:
            raise ValueError(
                "SamplingDesignTypeCode must be between 1 and 20 characters."
            )


class SourceMapScale(str):
    """
    The number that represents the proportional distance on the ground for one unit of
    measure on the map or photo.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("SourceMapScale must be between 0 and 60 characters.")


class StateCode(str):
    """
    A code designator used to identify a principal administrative subdivision of the
    United States, Canada, or Mexico.
    """

    def __init__(self, o=""):
        if len(o) > 2:
            raise ValueError("StateCode must be between 0 and 2 characters.")


class StatisticalBaseCode(str):
    """
    The code for the method used to calculate derived results.
    """

    def __init__(self, o=""):
        if len(o) > 25:
            raise ValueError("StatisticalBaseCode must be between 0 and 25 characters.")


class StatisticalNValueNumeric(int):
    """
    The number of repeated measurements taken to calculate the result value as an
    average.
    """

    def __init__(self, o=0):
        if o < 0:
            raise ValueError("StatisticalNValueNumeric must be a positive integer.")


class StatisticalStratumText(str):
    """
    Identifies the statistical stratum applied to this site.
    """

    def __init__(self, o=""):
        if len(o) > 15:
            raise ValueError(
                "StatisticalStratumText must be between 0 and 15 characters."
            )


class SubjectTaxonomicName(str):
    """
    The name of the organism sampled as part of a biological sample.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError("SubjectTaxonomicName must be between 0 and 255 characters.")


class SubjectTaxonomicNameUserSupplied(str):
    """
    The user supplied name of the organism sampled as part of a biological sample.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError(
                "SubjectTaxonomicNameUserSupplied must be between 0 and 255 characters."
            )


class SubjectTaxonomicNameUserSuppliedReferenceText(str):
    """
    Identifies the source or data system that created or defined the identifier.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError(
                "SubjectTaxonomicNameUserSuppliedReferenceText must be between 0 and 255"
                "characters."
            )


class SubstanceDilutionFactor(str):
    """
    The overall dilution of the substance subjected to this analysis.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "SubstanceDilutionFactor must be between 0 and 60 characters."
            )


class SupplementalAddressText(str):
    """
    The text that provides additional information about an address, including a building
    name with its secondary unit and number, an industrial park name, an installation
    name or descriptive text where no formal address is available.
    """

    def __init__(self, o=""):
        if len(o) > 120:
            raise ValueError(
                "SupplementalAddressText must be between 0 and 120 characters."
            )


class TargetCount(str):
    """
    A code used to identify the intended count that the sorter was aiming for.
    """

    def __init__(self, o=""):
        if len(o) > 35:
            raise ValueError("TargetCount must be between 0 and 35 characters.")


class TaxonomicPollutionTolerance(str):
    """
    For entries representing taxa, a code representing the ability of the reported taxon
    to tolerate pollution.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError(
                "TaxonomicPollutionTolerance must be between 0 and 30 characters."
            )


class TaxonomistAccreditationIndicator(object):
    """
    Indicates whether the taxonomist is accredited.
    """

    __o: bool

    def __init__(self, o=False):
        self.__o = bool(o)

    def __str__(self):
        return "True" if self.__o else "False"

    def __bool__(self):
        return self.__o


class TaxonomistAccreditationAuthorityName(str):
    """
    An outside accreditation authority identifier for the taxonomist.
    """

    def __init__(self, o=""):
        if len(o) > 20:
            raise ValueError(
                "TaxonomistAccreditationAuthorityName must be between 0 and 20 "
                "characters."
            )


class TaxonomicPollutionToleranceScaleText(str):
    """
    Provides a description of the scale used for the taxonomic pollution tolerance value.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "TaxonomicPollutionToleranceScaleText must be between 0 and 50 "
                "characters."
            )


class TelephoneExtensionNumberText(str):
    """
    The number assigned within an organization to an individual telephone that extends
    the external telephone number.
    """

    def __init__(self, o=""):
        if len(o) > 6:
            raise ValueError(
                "TelephoneExtensionNumberText must be between 0 and 6 characters."
            )


class TelephoneNumberText(str):
    """
    The number that identifies a particular telephone connection.
    """

    def __init__(self, o=""):
        if len(o) > 15:
            raise ValueError("TelephoneNumberText must be between 0 and 15 characters.")


class TelephoneNumberTypeName(str):
    """
    The name that describes a telephone number type.
    """

    def __init__(self, o=""):
        if len(o) > 6:
            raise ValueError(
                "TelephoneNumberTypeName must be between 0 and 6 characters."
            )


class ThermalPreservativeUsedName(str):
    """
    Information describing the temperature means used to preserve the sample.
    """

    def __init__(self, o=""):
        if len(o) > 250:
            raise ValueError(
                "ThermalPreservativeUsedName must be between 0 and 250 characters."
            )


class Time(time):
    """
    The time of day that is reported.
    """

    pass


class TimeZoneCode(str):
    """
    The time zone for which the time of day is reported. Any of the longitudinal
    divisions of the earth's surface in which a standard time is kept.
    """

    def __init__(self, o=None):
        if not isinstance(o, str) or len(o) < 1 or len(o) > 4:
            raise ValueError("TimeZoneCode must be between 1 and 4 characters.")


class ToxicityTestType(str):
    """
    Identifies the type of toxicity as either Acute or Chronic.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError("ToxicityTestType must be between 0 and 30 characters.")


class TribalCode(str):
    """
    The code that represents the American Indian tribe or Alaskan Native entity.
    """

    def __init__(self, o=""):
        if len(o) > 3:
            raise ValueError("TribalCode must be between 0 and 3 characters.")


class TribalLandIndicator(str):
    """
    An indicator denoting whether the location is on a tribal land.
    """

    def __new__(cls, o: Union[str, bool]):
        if isinstance(o, str):
            if o.lower() in ["true", "t", "yes", "y", "1"]:
                return super().__new__(cls, "true")
            else:
                return super().__new__(cls, "false")
        else:
            return super().__new__(cls, "true" if bool(o) else "false")

    def __bool__(self):
        if self == "true":
            return True
        else:
            return False


class TribalLandName(str):
    """
    The name of an American Indian or Alaskan native area where the location exists.
    """

    def __init__(self, o=""):
        if len(o) > 512:
            raise ValueError("TribalLandName must be between 0 and 512 characters.")


class TrophicLevelName(str):
    """
    For entries representing taxa, a code representing the trophic level with which the
    reported taxon is typically assigned.
    """

    def __init__(self, o=""):
        if len(o) > 30:
            raise ValueError("TrophicLevelName must be between 0 and 30 characters.")


class UnidentifiedSpeciesIdentifier(str):
    """
    A number or name assigned as a part of a taxonomic identification. Used with a valid
    genus name to indicate a unique species has been observed but not taxonomically
    identified.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError(
                "UnidentifiedSpeciesIdentifier must be between 0 and 255 characters."
            )


class UpperConfidenceLimitValue(str):
    """
    Value of the upper end of the confidence interval.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError(
                "UpperConfidenceLimitValue must be between 0 and 60 characters."
            )


class UpperClassBoundValue(str):
    """
    This described the upper bound for a frequency class descriptor.
    """

    def __init__(self, o=""):
        if len(o) > 60:
            raise ValueError("UpperClassBoundValue must be between 0 and 60 characters.")


class VerticalCollectionMethodName(str):
    """
    The name that identifies the method used to collect the vertical measure (i.e. the
    altitude) of a reference point.
    """

    def __init__(self, o=""):
        if len(o) > 50:
            raise ValueError(
                "VerticalCollectionMethodName must be between 0 and 50 characters."
            )


class VerticalCoordinateReferenceSystemDatumName(str):
    """
    The name of the reference datum used to determine the vertical measure (i.e., the
    altitude).
    """

    def __init__(self, o=""):
        if len(o) > 10:
            raise ValueError(
                "VerticalCoordinateReferenceSystemDatumName must be between 0 and 10 "
                "characters."
            )


class VoltinismName(str):
    """
    The number of broods or generations of the characteristic in a year.
    """

    def __init__(self, o=""):
        if len(o) > 25:
            raise ValueError("VoltinismName must be between 0 and 25 characters.")


class WellTypeText(str):
    """
    Identifies the primary well type.
    """

    def __init__(self, o=""):
        if len(o) > 255:
            raise ValueError("WellTypeText must be between 0 and 255 characters.")
