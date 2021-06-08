from wqxlib import WQXSubmission

with WQXSubmission(filename="monitoring_location.xml") as submission:
    submission.comment = "new data"
    submission.id = "72420"
    submission.author = "John Doe"
    submission.organization = "WVSU / Agricultural and Environmental Research Station"
    submission.title = "WQX"
    submission.contactInfo = """P.O. Box 1000
    Nowhere, AK
    12345
    123-546-7890
    jdoe@nowhere.edu"""
    submission.notification = "jdoe@nowhere.edu"

    # We are using the WQXTEST organization to avoid polluting the database
    # with this example.
    submission.organizationIdentifier = "WQXTEST"
    submission.organizationFormalName = "WQX Test Organization (Tribal)"
    submission.organizationDescriptionText = "Test"
    submission.tribalCode = "820"

    with submission.electronicAddress() as email:
        email.electronicAddressText = "storet@epa.gov"
        email.electronicAddressTypeName = "Email"

    with submission.telephonic() as phone:
        phone.telephoneNumberText = "800-424-9067"
        phone.telephoneNumberTypeName = "Office"

    with submission.organizationAddress() as address:
        address.addressTypeName = "Location"
        address.addressText = "1201 Oakridge Dr."
        address.localityName = "Fort Collins"
        address.stateCode = "CO"
        address.postalCode = "80525"
        address.countryCode = "US"

    with submission.monitoringLocation() as ml:
        with ml.monitoringLocationGeospatial() as geospatial:
            geospatial.latitudeMeasure = "38.6470"
            geospatial.longitudeMeasure = "-82.8587"
            geospatial.sourceMapScale = "2400"
            geospatial.horizontalCollectionMethodName = "Interpolation-Map"
            geospatial.horizontalCoordinateReferenceSystemDatumName = "NAD83"
            geospatial.countryCode = "US"
            geospatial.stateCode = "WV"
            geospatial.countyCode = "039"
        with ml.monitoringLocationIdentity() as identity:
            identity.monitoringLocationIdentifier = "GREENUP"
            identity.monitoringLocationName = "Greenup Dam"
            identity.monitoringLocationTypeName = "River/Stream"
            identity.hucEightDigitCode = "05090103"
            identity.hucTwelveDigitCode = "050901030107"
            identity.tribalLandIndicator = False
