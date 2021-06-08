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

    with submission.monitoringLocation() as location:
        # Geospatial
        location.latitudeMeasure = "38.6470"
        location.longitudeMeasure = "-82.8587"
        location.sourceMapScale = "2400"
        location.horizontalCollectionMethodName = "Interpolation-Map"
        location.horizontalCoordinateReferenceSystemDatumName = "NAD83"
        location.countryCode = "US"
        location.stateCode = "WV"
        location.countyCode = "039"
        # Identity
        location.monitoringLocationIdentifier = "GREENUP"
        location.monitoringLocationName = "Greenup Dam"
        location.monitoringLocationTypeName = "River/Stream"
        location.hucEightDigitCode = "05090103"
        location.hucTwelveDigitCode = "050901030107"
        location.tribalLandIndicator = False
