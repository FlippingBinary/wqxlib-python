from yattag import Doc

from .SimpleContent import (
    AddressText,
    AddressTypeName,
    CountryCode,
    CountyCode,
    LocalityName,
    PostalCode,
    StateCode,
    SupplementalAddressText,
)


class OrganizationAddress:
    """
    The physical address of an organization.
    """

    __addressTypeName: AddressTypeName
    __addressText: AddressText
    __supplementalAddressText: SupplementalAddressText
    __localityName: LocalityName
    __stateCode: StateCode
    __postalCode: PostalCode
    __countryCode: CountryCode
    __countyCode: CountyCode

    def __init__(
        self,
        o: dict = None,
        *,
        addressTypeName: AddressTypeName = None,
        addressText: AddressText = None,
        supplementalAddressText: SupplementalAddressText = None,
        localityName: LocalityName = None,
        stateCode: StateCode = None,
        postalCode: PostalCode = None,
        countryCode: CountryCode = None,
        countyCode: CountyCode = None
    ):
        if isinstance(o, OrganizationAddress):
            # Assign attributes from object without typechecking
            self.__addressTypeName = o.addressTypeName
            self.__addressText = o.addressText
            self.__supplementalAddressText = o.supplementalAddressText
            self.__localityName = o.localityName
            self.__stateCode = o.stateCode
            self.__postalCode = o.postalCode
            self.__countryCode = o.countryCode
            self.__countyCode = o.countyCode
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.addressTypeName = o.get("addressTypeName")
            self.addressText = o.get("addressText")
            self.supplementalAddressText = o.get("supplementalAddressText")
            self.localityName = o.get("localityName")
            self.stateCode = o.get("stateCode")
            self.postalCode = o.get("postalCode")
            self.countryCode = o.get("countryCode")
            self.countyCode = o.get("countyCode")
        else:
            # Assign attributes from named keywords with typechecking
            self.addressTypeName = addressTypeName
            self.addressText = addressText
            self.supplementalAddressText = supplementalAddressText
            self.localityName = localityName
            self.stateCode = stateCode
            self.postalCode = postalCode
            self.countryCode = countryCode
            self.countyCode = countyCode

    @property
    def addressTypeName(self) -> AddressTypeName:
        return self.__addressTypeName

    @addressTypeName.setter
    def addressTypeName(self, val: AddressTypeName) -> None:
        self.__addressTypeName = None if val is None else AddressTypeName(val)

    @property
    def addressText(self) -> AddressText:
        return self.__addressText

    @addressText.setter
    def addressText(self, val: AddressText) -> None:
        self.__addressText = None if val is None else AddressText(val)

    @property
    def supplementalAddressText(self) -> SupplementalAddressText:
        return self.__supplementalAddressText

    @supplementalAddressText.setter
    def supplementalAddressText(self, val: SupplementalAddressText) -> None:
        self.__supplementalAddressText = (
            None if val is None else SupplementalAddressText(val)
        )

    @property
    def localityName(self) -> LocalityName:
        return self.__localityName

    @localityName.setter
    def localityName(self, val: LocalityName) -> None:
        self.__localityName = None if val is None else LocalityName(val)

    @property
    def stateCode(self) -> StateCode:
        return self.__stateCode

    @stateCode.setter
    def stateCode(self, val: StateCode) -> None:
        self.__stateCode = None if val is None else StateCode(val)

    @property
    def postalCode(self) -> PostalCode:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, val: PostalCode) -> None:
        self.__postalCode = None if val is None else PostalCode(val)

    @property
    def countryCode(self) -> CountryCode:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, val: CountryCode) -> None:
        self.__countryCode = None if val is None else CountryCode(val)

    @property
    def countyCode(self) -> CountyCode:
        return self.__countyCode

    @countyCode.setter
    def countyCode(self, val: CountyCode) -> None:
        self.__countyCode = None if val is None else CountyCode(val)

    def generateXML(self, name: str = "OrganizationAddress") -> str:
        doc = Doc()
        line = doc.line
        tag = doc.tag

        with tag(name):
            if self.__addressTypeName is not None:
                line("AddressTypeName", self.__addressTypeName)
            if self.__addressText is not None:
                line("AddressText", self.__addressText)
            if self.__supplementalAddressText is not None:
                line("SupplementalAddressText", self.__supplementalAddressText)
            if self.__localityName is not None:
                line("LocalityName", self.__localityName)
            if self.__stateCode is not None:
                line("StateCode", self.__stateCode)
            if self.__postalCode is not None:
                line("PostalCode", self.__postalCode)
            if self.__countryCode is not None:
                line("CountryCode", self.__countryCode)
            if self.__countyCode is not None:
                line("CountyCode", self.__countyCode)

        return doc.getvalue()
