import unittest
import xml.etree.cElementTree as ET

from wqxlib import Document, Header, Payload, Submission
from wqxlib.wqx_v3_0 import (
    WQX,
    MonitoringLocation,
    MonitoringLocationGeospatial,
    MonitoringLocationIdentity,
    Organization,
    OrganizationDescription,
)


class TestCreateWQXDocument(unittest.TestCase):
    def test_create_wqx_document(self):

        submission = Submission(
            document=Document(
                id="20201209ML8",
                header=Header(
                    author="Test Author",
                    organization="Test Organization",
                    contactInfo="Test Organization Mailing or Physical Address",
                    notification="test@example.org",
                ),
                # Even though we are assigning a single object to the payload key here,
                # it becomes a list item which can be appended to later
                payload=Payload(
                    operation="Update-Insert",
                    wqx=WQX(
                        organization=Organization(
                            organizationDescription=OrganizationDescription(
                                organizationIdentifier="WQXTEST",
                                organizationFormalName="WQX Test Organization",
                                organizationDescriptionText="Test",
                            ),
                            monitoringLocation=MonitoringLocation(
                                monitoringLocationGeospatial=MonitoringLocationGeospatial(
                                    latitudeMeasure="38.6470",
                                    longitudeMeasure="-82.8587",
                                    sourceMapScale="2400",
                                    horizontalCollectionMethodName="Interpolation-Map",
                                    horizontalCoordinateReferenceSystemDatumName="NAD83",
                                    countryCode="US",
                                    stateCode="WV",
                                    countyCode="039",
                                ),
                                monitoringLocationIdentity=MonitoringLocationIdentity(
                                    monitoringLocationIdentifier="GREENUP",
                                    monitoringLocationName="Greenup Dam",
                                    monitoringLocationTypeName="River/Stream",
                                    hucEightDigitCode="05090103",
                                    hucTwelveDigitCode="050901030107",
                                    tribalLandIndicator=False,
                                ),
                            ),
                        )
                    ),
                ),
            )
        )
        doc = submission.document.generateXML()

        tree = ET.ElementTree(ET.fromstring(doc))
        root = tree.getroot()
        self.assertEqual(
            root.tag,
            "{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Document",
        )
        header = root[0]
        self.assertEqual(
            header.tag,
            "{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Header",
        )
        self.assertEqual(header[0].text, "Test Author")
        self.assertEqual(header[1].text, "Test Organization")
        self.assertEqual(header[2].text, "WQX")
        self.assertEqual(header[4].text, "Test Organization Mailing or Physical Address")
        self.assertEqual(header[5].text, "test@example.org")
        payload = root[1]
        self.assertEqual(
            payload.tag,
            "{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Payload",
        )
        self.assertEqual(payload.attrib.get("Operation"), "Update-Insert")
