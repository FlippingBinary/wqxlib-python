from datetime import datetime

import pandas as pd
from dateutil import tz

# wqxlib has one import for what we are doing
from wqxlib import WQXSubmission

# Load data from a CSV file using Pandas.
# Data could be gathered from any method you choose.
csv = pd.read_csv(
    "data_report_03-04-2021_13-22-37.csv",
    header=[0, 1, 2],
    index_col=None,
    engine="c",
    na_values="",
    parse_dates=[0],
    infer_datetime_format=True,
)

# Our csv specifies the timezone in the header of the index.
tzlocal = tz.gettz(csv.columns.values[0][1][5:-10])

# Set the index
csv.set_index(csv.columns.values[0], inplace=True)

# Define new columns for year, month, and day for daily grouping
# The three-value index avoids a performance warning
csv["Site", "Date", "Year"] = csv.index.year
csv["Site", "Date", "Month"] = csv.index.month
csv["Site", "Date", "Day"] = csv.index.day
median = csv.groupby(
    [("Site", "Date", "Year"), ("Site", "Date", "Month"), ("Site", "Date", "Day")]
).median()

# Drop the first and last days as they may be incomplete
median = median.drop(median.index[[0, -1]])

# This is our starting point. It creates a new submission and specifies where to save it
with WQXSubmission(fileName="continuous.xml") as submission:
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

    # Lookup table to translate into WQX-Aware monitoring locations
    # We must translate into a monitoring location which has already
    # been created in WQX Web or in this submission.
    # We are using existing monitoring locations, so we simply
    # translate local names to global names.
    monitoring_locations = {
        "Ohio River Robert C Byrd Locks": "Robert C Byrd Locks",
        "Ohio River Greenup Locks": "Greenup Locks",
    }

    # Lookup table to translate into WQX-Approved Characteristic names
    # https://cdx.epa.gov/WQXWeb/DomainValueListWqx.aspx?downloadTable=CHARACTERISTIC
    characteristics = {
        "Battery": "Battery voltage",
        "Temperature": "Temperature, water",
        "Sp Cond": "Conductivity",
        "pH": "pH",
        "Turbidity": "Turbidity",
        "ODOSat": "Dissolved oxygen saturation",
        "ODO": "Dissolved oxygen (DO)",
        "Chlorophyll": "Chlorophyll",
        "Chlorophyll RFU": "Chlorophyll",
        "BGA-Phycocyanin": "Chlorophyll",
        "BGA-Phycocyanin RFU": "Chlorophyll",
        "Depth": "Depth",
        "Wiper Pos": "Dry deposition",
        "Cable Pwr": "Data-logger operating voltage",
        "PAR": "Light, photosynthetic active radiation at depth (PAR)",
        "Nitrate": "Nitrate",
        "Optical Brighteners RFU": "Optical brighteners fluorescent whitening agents by fluorescence",  # noqa B950
    }

    # Lookup table to translate into WQX-Approved Measurement Units
    # https://cdx.epa.gov/WQXWeb/DomainValueListWqx.aspx?downloadTable=MEASUREMENT%20UNIT
    unit_codes = {
        "V": "volts",
        "C": "deg C",
        "uS/cm": "uS/cm",
        "NTU": "NTU",
        "%": "%",
        "mg/L": "mg/l",
        "ug/L": "ug/l",
        "RFU": "RFU",
        "m": "m",
        "umol/s/m2": "umol/S/m2",
        "uMol.1": "umol",
        "mg/L.1": "mg/l",
    }

    # Iterate each day
    for date, day_data in median.iterrows():
        # Group by the site name, which is level 0 of the index
        row = day_data.groupby(level=0)

        # Iterate each site
        for name, site_data in row:
            # Use lookup table to translate monitoring location name
            site = monitoring_locations.get(name)

            # The group index is a tuple representing the date
            # We can create the activity_date by joining it.
            activity_date = "".join(map(str, date))

            # The activity identifier will default to something similar,
            # but it is good practice to explicity set it.
            # If an activity identifier is repeated, the newer one will
            # replace the older one.
            activity_id = f"{site}:{activity_date}:FM:PRS"

            # Create a new activity in the submission
            with submission.activity() as activity:
                activity.activityIdentifier = activity_id
                activity.monitoringLocationIdentifier = site
                activity.activityTypeCode = "Field Msr/Obs"
                activity.activityMediaName = "Water"
                # This timestamp will be reused later, so define a variable
                timestamp = datetime(*date, tzinfo=tzlocal)
                activity.activityStartDate = timestamp
                activity.projectIdentifier = "TEST"

                # Create a new sample in the activity
                with activity.sample() as sample:
                    sample.methodIdentifier = "QAPP"
                    sample.methodIdentifierContext = "WQXTEST"
                    sample.methodName = "Quality Assurance Project Plan for WQX test"
                    sample.methodQualifierTypeName = "WQXTEST"
                    sample.sampleCollectionEquipmentName = "Probe/Sensor"

                # Iterate each fact in the day's data
                for key, fact in site_data.items():
                    # Translate characteristic name to approved value
                    characteristic = characteristics.get(key[1])
                    # We skipped a few values which need to be ignored
                    if characteristic is not None:
                        # Create a new result in the activity for each fact
                        with activity.result() as result:
                            # The characteristic name must be an approved value
                            result.characteristicName = characteristic
                            # The user-supplied name can be anything for your reference
                            result.characteristicNameUserSupplied = key[1]
                            # Measurement Unit must be an approved value
                            result.resultMeasureUnitCode = unit_codes.get(key[2], "None")
                            # Measure value must be a string (so you can control precision)
                            result.resultMeasureValue = str(fact)
                            # Analysis start time should be a datetime object with timezone
                            result.analysisStartTime = timestamp
