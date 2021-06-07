# Python library for WQX (wqxlib)

This is a Python library for creating XML documents for direct submission to WQX Web without using an import configuration file. If your use-case is complex, this feature may save you the hassle of uploading incremental changes to an import configuration file as you detect more edge cases or struggle to make an import configuration file which is flexible enough for your purposes. Just modify your code to produce the proper XML file and use the `WQXWeb` class from the sister project [`wqxweblib`](https://github.com/FlippingBinary/wqxweblib-python) to upload it. It's also useful for submitting new monitoring locations or other types of data which are one-off situations. Sometimes it's easier to just build the XML file directly than it is to first create an import configuration file (or copy one) and specify the parameters in a CSV or XSL file. If you find a bug, please submit a pull request on [Github](https://github.com/FlippingBinary/wqxlib-python) or open an issue there. I'm also open to suggestions for how to improve the creation of XML files. Currently, it's quite complex due to its flexibility.

This code is supported by the National Science Foundation under Award No. OIA-1458952. Any opinions, findings and conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## Contents

- [Python library for WQX (wqxlib)](#python-library-for-wqx-wqxlib)
  - [Contents](#contents)
  - [Getting Started](#getting-started)
  - [Package Versioning](#package-versioning)
  - [Import WQX Module](#import-wqx-module)
- [WQXLib XML API Reference](#wqxlib-xml-api-reference)
  - [Document](#document)
  - [Header](#header)
  - [Payload](#payload)
  - [Submission](#submission)
- [WQXLib's WQX v3.0 XML API Reference](#wqxlibs-wqx-v30-xml-api-reference)
  - [Activity](#activity)
  - [ActivityDescription](#activitydescription)
  - [ActivityGroup](#activitygroup)
  - [ActivityLocation](#activitylocation)
  - [ActivityMetric](#activitymetric)
  - [ActivityMetricType](#activitymetrictype)
  - [AlternateMonitoringLocationIdentity](#alternatemonitoringlocationidentity)
  - [AquiferInformation](#aquiferinformation)
  - [AttachedBinaryObject](#attachedbinaryobject)
  - [BibliographicReference](#bibliographicreference)
  - [BiologicalActivityDescription](#biologicalactivitydescription)
  - [BiologicalHabitatCollectionInformation](#biologicalhabitatcollectioninformation)
  - [BiologicalHabitatIndex](#biologicalhabitatindex)
  - [BiologicalResultDescription](#biologicalresultdescription)
  - [CollectionEffort](#collectioneffort)
  - [ComparableAnalyticalMethod](#comparableanalyticalmethod)
  - [DataQualityIndicator](#dataqualityindicator)
  - [DetectionQuantitationLimit](#detectionquantitationlimit)
  - [ElectronicAddress](#electronicaddress)
  - [Entity_Update_Identifiers](#entity_update_identifiers)
  - [FrequencyClassInformation](#frequencyclassinformation)
  - [HorizontalAccuracyMeasure](#horizontalaccuracymeasure)
  - [IndexType](#indextype)
  - [LabSamplePreparation](#labsamplepreparation)
  - [Measure](#measure)
  - [MeasureCompact](#measurecompact)
  - [MonitoringLocation](#monitoringlocation)
  - [MonitoringLocationGeospatial](#monitoringlocationgeospatial)
  - [MonitoringLocationIdentity](#monitoringlocationidentity)
  - [NetInformation](#netinformation)
  - [Organization](#organization)
  - [OrganizationAddress](#organizationaddress)
  - [OrganizationDescription](#organizationdescription)
  - [Organization_Delete](#organization_delete)
  - [Project](#project)
  - [ProjectMonitoringLocationWeighting](#projectmonitoringlocationweighting)
  - [ReferenceMethod](#referencemethod)
  - [Result](#result)
  - [ResultAnalyticalMethod](#resultanalyticalmethod)
  - [ResultDescription](#resultdescription)
  - [ResultLabInformation](#resultlabinformation)
  - [SampleDescription](#sampledescription)
  - [SamplePreparation](#samplepreparation)
  - [SimpleContent](#simplecontent)
  - [TaxonomicDetails](#taxonomicdetails)
  - [Telephonic](#telephonic)
  - [WellInformation](#wellinformation)
  - [WQX](#wqx)
  - [WQXTime](#wqxtime)
  - [WQXDelete](#wqxdelete)
  - [WQXUpdateIdentifiers](#wqxupdateidentifiers)

## Getting Started

Look in the `examples` directory for a more complete example with sample data.

1. Install this package using `pip`

        pip install wqxlib

2. Import the `WQXSubmission` class

        from wqxlib import WQXSubmission

3. Use the `with ... as` syntax to create the submission

        with WQXSubmission(filename='example.xml') as submission:
            # Manipulate submission object properties

4. After creating the submission, submit it using the `wqxweblib` package or manually in WQX Web.

## Package Versioning

This package uses a five-segment version number. The first two segments of the version number indicate the version of WQX it supports. The last three segments follow the [Semantic Versioning](https://semver.org/) standard and are specific to only this package, not any WQX release. They are in the format `x.y.z` where `x` is the major version number, `y` is the minor version number, and `z` is the patch version number.

The major version number increments when incompatible API changes are made. The minor version number increments when functionality is added in a backward compatible manner. The patch version number increments when there are backward compatible bug fixes. 

It is a good practice to lock the first three digits of the version in your `requirements.txt` file, if you are using one. That allow you to safely rebuild your environment without accidentally introducing breaking changes. For the current version, that would mean adding a line to your `requirements.txt` file like this:

    wqxlib<3.0.1

# WQXLib XML API Reference

The following low-level classes describe the larger structure of a valid XML document for WQXWeb submission. These classes contain the building blocks provided by WQX v3.0. You are not required to interact with these directly. Use of the `with ... as` syntax is highly recommended.

## Document

The base document type used for submission to WQXWeb.

**Parameters:**

- `id` (ID)
- `header` (Header)
- `payload` (List[Payload])

## Header

**Parameters:**

- `author` (str)
- `organization` (str)
- `title` (str)
- `creationTime` (datetime)
- `comment` (str)
- `dataService` (str)
- `contactInfo` (str)
- `notification` (List[str])
- `sensitivity` (str)
- `property` (dict)

## Payload

The Payload section of the document contains the WQX data.

- `operation` (OperationType) - either "UPDATE_INSERT" or "DELETE".
- `wqx` (WQX) - this must be a v3.0 `WQX` object as described in the next section, if provided.
- `wqxUpdateIdentifiers` (WQXUpdateIdentifiers) - this must be a v3.0 `WQXUpdateIdentifiers` object as described in the next section, if provided.
- `wqxDelete` (WQXDelete) - this must be a v3.0 `WQXDelete` object as described in the next section, if provided.

## Submission

This is the container of the entire submission.

**Parameters:**

- `document` (Document)

# WQXLib's WQX v3.0 XML API Reference

The following classes describe the building blocks of a v3.0 XML document for WQXWeb submission. This is the current version of the standard and there are no plans to create an API for the older versions. If you want to, please use the pattern of the v3.0 code and submit a pull request so others can benefit from your code too.

All of the described classes come directly from the XSD files which are used by WQX to validate input.

To import any of the following types, pull them from `wqxlib` like this:

    from wqxlib import (
      MonitoringLocation,
      MonitoringLocationGeospatial,
      MonitoringLocationIdentity,
      Organization,
      OrganizationDescription,
      WQX
    )

## Activity

Allows for the reporting of monitoring activities conducted at a Monitoring Location.

**Parameters:**

- `activityDescription` (ActivityDescription)
- `activityLocation` (ActivityLocation)
- `biologicalActivityDescription` (BiologicalActivityDescription)
- `sampleDescription` (SampleDescription)
- `activityMetric` (List of ActivityMetric)
- `attachedBinaryObject` (List of AttachedBinaryObject)
- `result` (List of Result)

## ActivityDescription

Basic identification information for an activity conducted within a project.

**Parameters:**

- `activityIdentifier` (ActivityIdentifier)
- `activityIdentifierUserSupplied` (ActivityIdentifierUserSupplied)
- `activityTypeCode` (ActivityTypeCode)
- `activityMediaName` (ActivityMediaName)
- `activityMediaSubdivisionName` (ActivityMediaSubdivisionName)
- `activityStartDate` (ActivityStartDate)
- `activityStartTime` (WQXTime)
- `activityEndDate` (ActivityEndDate)
- `activityEndTime` (WQXTime)
- `activityRelativeDepthName` (ActivityRelativeDepthName)
- `activityDepthHeightMeasure` (MeasureCompact)
- `activityTopDepthHeightMeasure` (MeasureCompact)
- `activityBottomDepthHeightMeasure` (MeasureCompact)
- `activityDepthAltitudeReferencePointText` (DepthAltitudeReferencePointText)
- `projectIdentifier` (ProjectIdentifier)
- `activityConductingOrganizationText` (List of ActivityConductingOrganizationText)
- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `samplingComponentName` (SamplingComponentName)
- `activityCommentText` (CommentText)

## ActivityGroup

Allows for the grouping of activities.

**Parameters:**

- `activityGroupIdentifier` (ActivityGroupIdentifier)
- `activityGroupName` (ActivityGroupName)
- `activityGroupTypeCode` (ActivityGroupTypeCode)
- `activityIdentifier` (ActivityIdentifier)
- `replaceActivities` (bool)

## ActivityLocation

Geospatial description of monitoring site, if it is different from that described in the station description.

**Parameters:**

- `latitudeMeasure` (LatitudeMeasure)
- `longitudeMeasure` (LongitudeMeasure)
- `sourceMapScale` (SourceMapScale)
- `horizontalAccuracyMeasure` (MeasureCompact)
- `horizontalCollectionMethodName` (HorizontalCollectionMethodName)
- `horizontalCoordinateReferenceSystemDatumName` (HorizontalCoordinateReferenceSystemDatumName)
- `activityLocationDescriptionText` (ActivityLocationDescriptionText)

## ActivityMetric

This section allows for the reporting of metrics to support habitat or biotic integrity indices.

**Parameters:**

- `activityMetricType` (ActivityMetricType)
- `metricValueMeasure` (MeasureCompact)
- `metricScore` (MetricScore)
- `metricSamplingPointPlaceInSeries` (MetricSamplingPointPlaceInSeries)
- `metricCommentText` (CommentText)
- `indexIdentifier` (IndexIdentifier)

## ActivityMetricType

This section identifies the metric type reported as part of an activity metric.

**Parameters:**

- `metricTypeIdentifier` (MetricTypeIdentifier),
- `metricTypeIdentifierContext` (MetricTypeIdentifierContext),
- `metricTypeName` (MetricTypeName),
- `metricTypeCitation` (BibliographicReference),
- `metricTypeScaleText` (MetricTypeScaleText),
- `formulaDescriptionText` (FormulaDescriptionText)

## AlternateMonitoringLocationIdentity

Alternate identifications of a monitoring location.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `monitoringLocationIdentifierContext` (MonitoringLocationIdentifierContext)

## AquiferInformation

Identifies the procedures, processes, and references required to determine the methods used to obtain a result.

**Parameters:**

- `localAquiferCode` (LocalAquiferCode)
- `localAquiferCodeContext` (LocalAquiferCodeContext)
- `localAquiferName` (LocalAquiferName)
- `localAquiferDescriptionText` (LocalAquiferDescriptionText)

## AttachedBinaryObject

Reference document, image, photo, GIS data layer, laboratory material or other electronic object attached within a data exchange, as well as information used to describe the object.

**Parameters:**

- `binaryObjectFileName` (BinaryObjectFileName)
- `binaryObjectFileTypeCode` (BinaryObjectFileTypeCode)

## BibliographicReference

The descriptors used to identify and catalog an object.

**Parameters:**

- `resourceTitleName` (ResourceTitleName)
- `resourceCreatorName` (ResourceCreatorName)
- `resourceSubjectText` (ResourceSubjectText)
- `resourcePublisherName` (ResourcePublisherName)
- `resourceDate` (ResourceDate)
- `resourceIdentifier` (ResourceIdentifier)

## BiologicalActivityDescription

Allows for the reporting of biological monitoring activities conducted at a Monitoring Location.

**Parameters:**

- `assemblageSampledName` (AssemblageSampledName)
- `biologicalHabitatCollectionInformation` (BiologicalHabitatCollectionInformation)
- `toxicityTestType` (ToxicityTestType)
- `habitatSelectionMethod` (HabitatSelectionMethod)

## BiologicalHabitatCollectionInformation

Allows for the reporting of biological habitat sample collection information.

**Parameters:**

- `collectionDuration` (MeasureCompact)
- `collectionArea` (MeasureCompact)
- `collectionEffort` (CollectionEffort)
- `reachLengthMeasure` (MeasureCompact)
- `reachWidthMeasure` (MeasureCompact)
- `collectionDescriptionText` (CollectionDescriptionText)
- `passCount` (PassCount)
- `netInformation` (NetInformation)

## BiologicalHabitatIndex

This section allows for the reporting of habitat and biotic integrity indices as a representation of water quality conditions.

**Parameters:**

- `indexIdentifier` (IndexIdentifier)
- `indexType` (IndexType)
- `indexScore` (IndexScore)
- `indexQualifierCode` (IndexQualifierCode)
- `indexCommentText` (CommentText)
- `indexCalculatedDate` (IndexCalculatedDate)
- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)

## BiologicalResultDescription

Allows for the reporting of biological result information.

**Parameters:**

- `biologicalIntentName` (BiologicalIntentName)
- `biologicalIndividualIdentifier` (BiologicalIndividualIdentifier)
- `subjectTaxonomicName` (SubjectTaxonomicName)
- `subjectTaxonomicNameUserSupplied` (SubjectTaxonomicNameUserSupplied)
- `subjectTaxonomicNameUserSuppliedReferenceText` (SubjectTaxonomicNameUserSuppliedReferenceText)
- `unidentifiedSpeciesIdentifier` (UnidentifiedSpeciesIdentifier)
- `sampleTissueAnatomyName` (SampleTissueAnatomyName)
- `groupSummaryCount` (GroupSummaryCount)
- `groupSummaryWeightMeasure` (MeasureCompact)
- `taxonomicDetails` (TaxonomicDetails)
- `frequencyClassInformation` (FrequencyClassInformation)

## CollectionEffort

The fields to describe the effort used a collection.

**Parameters:**

- `measureValue` (MeasureValue)
- `gearProcedureUnitCode` (GearProcedureUnitCode)

## ComparableAnalyticalMethod

Identifies the procedures, processes, and references required to determine the analytical methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodModificationText` (MethodModificationText)

## DataQualityIndicator

The quantitative statistics and qualitative descriptors that are used to interpret the degree of acceptability or utility of data to the user.

**Parameters:**

- `precisionValue` (PrecisionValue)
- `biasValue` (BiasValue)
- `confidenceIntervalValue` (ConfidenceIntervalValue)
- `upperConfidenceLimitValue` (UpperConfidenceLimitValue)
- `lowerConfidenceLimitValue` (LowerConfidenceLimitValue)

## DetectionQuantitationLimit

Information that describes one of a variety of detection or quantitation limits determined in a laboratory.

**Parameters:**

- `detectionQuantitationLimitTypeName` (DetectionQuantitationLimitTypeName)
- `detectionQuantitationLimitMeasure` (MeasureCompact)
- `detectionQuantitationLimitCommentText` (DetectionQuantitationLimitCommentText)

## ElectronicAddress

A location within a system of worldwide electronic communication where a computer user can access information or receive electronic mail.

**Parameters:**

- `electronicAddressText` (ElectronicAddressText)
- `electronicAddressTypeName` (ElectronicAddressTypeName)

## Entity_Update_Identifiers

Allows a Project Identifier to be changed.

**Parameters:**

- `oldIdentifier` (OldIdentifier)
- `newIdentifier` (NewIdentifier)

## FrequencyClassInformation

This section allows for the definition of a subgroup of biological communities by life stage, physical attribute, or abnormality to support frequency class studies.

**Parameters:**

- `frequencyClassDescriptorCode` (FrequencyClassDescriptorCode)
- `frequencyClassDescriptorUnitCode` (FrequencyClassDescriptorUnitCode)
- `lowerClassBoundValue` (LowerClassBoundValue)
- `upperClassBoundValue` (UpperClassBoundValue)

## HorizontalAccuracyMeasure

This file was not converted from XSD because it is does not define a complex type. It only creates an element called "HorizontalAccuracyMeasure" of type "MeasureCompact".

## IndexType

This section identifies the index type reported as part of a biological or habitat index.

**Parameters:**

- `indexTypeIdentifier` (IndexTypeIdentifier)
- `indexTypeIdentifierContext` (IndexTypeIdentifierContext)
- `indexTypeName` (IndexTypeName)
- `indexTypeCitation` (BibliographicReference)
- `indexTypeScaleText` (IndexTypeScaleText)

## LabSamplePreparation

Describes Lab Sample Preparation procedures which may alter the original state of the Sample and produce Lab subsamples.  These Lab Subsamples are analyized and reported by the Lab as Sample results.

**Parameters:**

- `labSamplePreparationMethod` (ReferenceMethod)
- `preparationStartDate` (PreparationStartDate)
- `preparationStartTime` (WQXTime)
- `preparationEndDate` (PreparationEndDate)
- `preparationEndTime` (WQXTime)
- `substanceDilutionFactor` (SubstanceDilutionFactor)

## Measure

Identifies the value, associated units of measure, and qualifier for measuring the observation or analytical result value.

**Parameters:**

- `resultMeasureValue` (ResultMeasureValue)
- `measureUnitCode` (MeasureUnitCode)
- `measureQualifierCode` (List[MeasureQualifierCode])

## MeasureCompact

Identifies only the value and the associated units of measure for measuring the observation or analytical result value.

**Parameters:**

- `measureValue` (MeasureValue)
- `measureUnitCode` (MeasureUnitCode)

## MonitoringLocation

An identifiable location where an environmental sample, onsite measurement, and/or observation is determined.

**Parameters:**

- `monitoringLocationIdentity` (MonitoringLocationIdentity)
- `monitoringLocationGeospatial` (MonitoringLocationGeospatial)
- `wellInformation` (WellInformation)
- `attachedBinaryObject` (List[AttachedBinaryObject])

## MonitoringLocationGeospatial

Monitoring location geographic location.

**Parameters:**

- `latitudeMeasure` (LatitudeMeasure)
- `longitudeMeasure` (LongitudeMeasure)
- `sourceMapScale` (SourceMapScale)
- `horizontalAccuracyMeasure` (MeasureCompact)
- `verticalAccuracyMeasure` (MeasureCompact)
- `horizontalCollectionMethodName` (HorizontalCollectionMethodName)
- `horizontalCoordinateReferenceSystemDatumName` (HorizontalCoordinateReferenceSystemDatumName)
- `verticalMeasure` (MeasureCompact)
- `verticalCollectionMethodName` (VerticalCollectionMethodName)
- `verticalCoordinateReferenceSystemDatumName` (VerticalCoordinateReferenceSystemDatumName)
- `countryCode` (CountryCode)
- `stateCode` (StateCode)
- `countyCode` (CountyCode)

## MonitoringLocationIdentity

Basic identification information for the location/site that is monitored or used for sampling.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `monitoringLocationName` (MonitoringLocationName)
- `monitoringLocationTypeName` (MonitoringLocationTypeName)
- `monitoringLocationDescriptionText` (MonitoringLocationDescriptionText)
- `hucEightDigitCode` (HUCEightDigitCode)
- `hucTwelveDigitCode` (HUCTwelveDigitCode)
- `tribalLandIndicator` (TribalLandIndicator)
- `tribalLandName` (TribalLandName)
- `alternateMonitoringLocationIdentity` (List[AlternateMonitoringLocationIdentity])
- `drainageAreaMeasure` (MeasureCompact)
- `contributingDrainageAreaMeasure` (MeasureCompact)

## NetInformation

Allows for the reporting of net sample collection information.

**Parameters:**

- `netTypeName` (NetTypeName)
- `netSurfaceAreaMeasure` (MeasureCompact)
- `netMeshSizeMeasure` (MeasureCompact)
- `boatSpeedMeasure` (MeasureCompact)
- `currentSpeedMeasure` (MeasureCompact)

## Organization

Schema used to transfer organization information.

**Parameters:**

- `organizationDescription` (OrganizationDescription)
- `electronicAddress` (List[ElectronicAddress])
- `telephonic` (List[Telephonic])
- `organizationAddress` (List[OrganizationAddress])
- `project` (List[Project])
- `monitoringLocation` (List[MonitoringLocation])
- `biologicalHabitatIndex` (List[BiologicalHabitatIndex])
- `activity` (List[Activity])
- `activityGroup` (List[ActivityGroup])

## OrganizationAddress

The physical address of an organization.

**Parameters:**

- `addressTypeName` (AddressTypeName)
- `addressText` (AddressText)
- `supplementalAddressText` (SupplementalAddressText)
- `localityName` (LocalityName)
- `stateCode` (StateCode)
- `postalCode` (PostalCode)
- `countryCode` (CountryCode)
- `countyCode` (CountyCode)

## OrganizationDescription

The particular word(s) regularly connected with a unique framework of authority within which a person or persons act, or are designated to act, towards some purpose.

**Parameters:**

- `organizationIdentifier` (OrganizationIdentifier)
- `organizationFormalName` (OrganizationFormalName)
- `organizationDescriptionText` (OrganizationDescriptionText)
- `tribalCode` (TribalCode)

## Organization_Delete

Schema used to delete organization information.

**Parameters:**

- `organizationIdentifier` (OrganizationIdentifier)
- `projectIdentifier` (List[ProjectIdentifier])
- `monitoringLocationIdentifier` (List[MonitoringLocationIdentifier])
- `activityIdentifier` (List[ActivityIdentifier])
- `activityGroupIdentifier` (List[ActivityGroupIdentifier])
- `indexIdentifier` (List[IndexIdentifier])

## Project

An environmental data collection effort that has a stated purpose and puts a series of samples and results into a meaningful context.

**Parameters:**

- `projectIdentifier` (ProjectIdentifier)
- `projectName` (ProjectName)
- `projectDescriptionText` (ProjectDescriptionText)
- `samplingDesignTypeCode` (SamplingDesignTypeCode)
- `qAPPApprovedIndicator` (QAPPApprovedIndicator)
- `qAPPApprovalAgencyName` (QAPPApprovalAgencyName)
- `attachedBinaryObject` (List[AttachedBinaryObject])
- `projectMonitoringLocationWeighting` (List[ProjectMonitoringLocationWeighting])

## ProjectMonitoringLocationWeighting

Describes the probability weighting information for a given Project / Monitoring Location Assignment.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `locationWeightingFactorMeasure` (MeasureCompact)
- `statisticalStratumText` (StatisticalStratumText)
- `locationCategoryName` (LocationCategoryName)
- `locationStatusName` (LocationStatusName)
- `referenceLocationTypeCode` (ReferenceLocationTypeCode)
- `referenceLocationStartDate` (ReferenceLocationStartDate)
- `referenceLocationEndDate` (ReferenceLocationEndDate)
- `referenceLocationCitation` (BibliographicReference)
- `commentText` (CommentText)

## ReferenceMethod

Identifies the procedures, processes, and references required to determine the methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodName` (MethodName)
- `methodQualifierTypeName` (MethodQualifierTypeName)
- `methodDescriptionText` (MethodDescriptionText)

## Result

Describes the results of a field measurement, observation, or laboratory analysis.

**Parameters:**

- `resultDescription` (ResultDescription)
- `biologicalResultDescription` (BiologicalResultDescription)
- `attachedBinaryObject` (List[AttachedBinaryObject])
- `resultAnalyticalMethod` (ResultAnalyticalMethod)
- `comparableAnalyticalMethod` (ComparableAnalyticalMethod)
- `resultLabInformation` (ResultLabInformation)
- `labSamplePreparation` (List[LabSamplePreparation])

## ResultAnalyticalMethod

Identifies the procedures, processes, and references required to determine the analytical methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodName` (MethodName)
- `methodQualifierTypeName` (MethodQualifierTypeName)
- `methodDescriptionText` (MethodDescriptionText)

## ResultDescription

Describes the results of a field measurement, observation, or laboratory analysis.

**Parameters:**

- `dataLoggerLineName` (DataLoggerLineName)
- `resultDetectionConditionText` (ResultDetectionConditionText)
- `characteristicName` (CharacteristicName)
- `characteristicNameUserSupplied` (CharacteristicNameUserSupplied)
- `methodSpeciationName` (MethodSpeciationName)
- `resultSampleFractionText` (ResultSampleFractionText)
- `resultMeasure` (Measure)
- `targetCount` (TargetCount)
- `proportionSampleProcessedNumeric` (ProportionSampleProcessedNumeric)
- `resultStatusIdentifier` (ResultStatusIdentifier)
- `statisticalBaseCode` (StatisticalBaseCode)
- `statisticalNValueNumeric` (StatisticalNValueNumeric)
- `resultValueTypeName` (ResultValueTypeName)
- `resultWeightBasisText` (ResultWeightBasisText)
- `resultTimeBasisText` (ResultTimeBasisText)
- `resultTemperatureBasisText` (ResultTemperatureBasisText)
- `resultParticleSizeBasisText` (ResultParticleSizeBasisText)
- `dataQuality` (DataQuality)
- `resultCommentText` (CommentText)
- `resultDepthHeightMeasure` (MeasureCompact)
- `resultDepthAltitudeReferencePointText` (DepthAltitudeReferencePointText)
- `resultSamplingPointName` (ResultSamplingPointName)
- `resultSamplingPointType` (ResultSamplingPointType)
- `resultSamplingPointPlaceInSeries` (ResultSamplingPointPlaceInSeries)
- `resultSamplingPointCommentText` (ResultSamplingPointCommentText)
- `recordIdentifierUserSupplied` (RecordIdentifierUserSupplied)

## ResultLabInformation

Describes information obtained by a laboratory related to a specific laboratory analysis.

**Parameters:**

- `laboratoryName` (LaboratoryName)
- `analysisStartDate` (AnalysisStartDate)
- `analysisStartTime` (WQXTime)
- `analysisEndDate` (AnalysisEndDate)
- `analysisEndTime` (WQXTime)
- `laboratoryCommentText` (LaboratoryCommentText)
- `resultDetectionQuantitationLimit` (DetectionQuantitationLimit)
- `laboratorySampleSplitRatio` (LaboratorySampleSplitRatio)
- `laboratoryAccreditationIndicator` (LaboratoryAccreditationIndicator)
- `laboratoryAccreditationAuthorityName` (LaboratoryAccreditationAuthorityName)
- `taxonomistAccreditationIndicator` (TaxonomistAccreditationIndicator)
- `taxonomistAccreditationAuthorityName` (TaxonomistAccreditationAuthorityName)

## SampleDescription

Basic identification information for the sample collected as part of a monitoring activity.

**Parameters:**

- `sampleCollectionMethod` (ReferenceMethod)
- `sampleCollectionEquipmentName` (SampleCollectionEquipmentName)
- `sampleCollectionEquipmentCommentText` (SampleCollectionEquipmentCommentText)
- `samplePreparation` (SamplePreparation)
- `hydrologicCondition` (HydrologicCondition)
- `hydrologicEvent` (HydrologicEvent)

## SamplePreparation

Describes a sample preparation procedure which may be conducted on an initial Sample or on subsequent subsamples.

**Parameters:**

- `samplePreparationMethod` (ReferenceMethod)
- `sampleContainerLabelName` (SampleContainerLabelName)
- `sampleContainerTypeName` (SampleContainerTypeName)
- `sampleContainerColorName` (SampleContainerColorName)
- `chemicalPreservativeUsedName` (ChemicalPreservativeUsedName)
- `thermalPreservativeUsedName` (ThermalPreservativeUsedName)
- `sampleTransportStorageDescription` (SampleTransportStorageDescription)

## SimpleContent

There are several data types which are strings or other basic data types with rules added. `SimpleContent` is the name of an `XSD` file and also the name of the Python file which defines those same types. They do not need to be used directly in your code. Just use regular Python types and they will be converted when possible.

## TaxonomicDetails

This section allows for the further definition of user-defined details for taxa.

**Parameters:**

- `cellFormName` (CellFormName)
- `cellShapeName` (CellShapeName)
- `habitName` (HabitName)
- `voltinismName` (VoltinismName)
- `taxonomicPollutionTolerance` (TaxonomicPollutionTolerance)
- `taxonomicPollutionToleranceScaleText` (TaxonomicPollutionToleranceScaleText)
- `trophicLevelName` (TrophicLevelName)
- `functionalFeedingGroupName` (FunctionalFeedingGroupName)
- `taxonomicDetailsCitation` (BibliographicReference)

## Telephonic

An identification of a telephone connection.

**Parameters:**

- `telephoneNumberText` (TelephoneNumberText)
- `telephoneNumberTypeName` (TelephoneNumberTypeName)
- `telephoneExtensionNumberText` (TelephoneExtensionNumberText)

## WellInformation

Description of the attributes of a well.

**Parameters:**

- `wellTypeText` (WellTypeText)
- `aquiferTypeName` (AquiferTypeName)
- `nationalAquiferCode` (NationalAquiferCode)
- `aquiferInformation` (AquiferInformation)
- `formationTypeText` (FormationTypeText)
- `wellHoleDepthMeasure` (MeasureCompact)
- `constructionDate` (ConstructionDate)
- `wellDepthMeasure` (MeasureCompact)

## WQX

Main Schema used to transfer water monitoring results to EPA Office of Water.

**Parameters:**

- `organization` (Organization)

## WQXTime

Custom WQX datatype that defines a local time and corresponding time zone in which the time is measured.

**Parameters:**

- `time` (Time)
- `timeZoneCode` (TimeZoneCode)

## WQXDelete

Main Schema used to delete a portion of water monitoring results from EPA Office of Water system.

**Parameters:**

- `organizationDelete` (List[OrganizationDelete])

## WQXUpdateIdentifiers

Main Schema used to update identifiers for major entities (projects, monitoring locations, activity, activity groups, and indexes).

**Parameters:**

- `updateIdentifiers` (List[UpdateIdentifiers])
