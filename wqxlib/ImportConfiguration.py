from .wqx_v3_0 import (
    ActivityDescription,
    ElectronicAddress,
    OrganizationAddress,
    OrganizationDescription,
    Telephonic,
)


class ImportConfiguration:
    __activityDescription: ActivityDescription
    __electronicAddress: ElectronicAddress
    __organizationAddress: OrganizationAddress
    __organizationDescription: OrganizationDescription
    __telephonic: Telephonic

    def __init__(
        self,
        o: dict = None,
        *,
        activityDescription: ActivityDescription = None,
        electronicAddress: ElectronicAddress = None,
        organizationAddress: OrganizationAddress = None,
        organizationDescription: OrganizationDescription = None,
        telephonic: Telephonic = None
    ):
        if isinstance(o, ImportConfiguration):
            # Assign attributes from object without typechecking
            self.__activityDescription = o.activityDescription
            self.__electronicAddress = o.electronicAddress
            self.__organizationAddress = o.organizationAddress
            self.__organizationDescription = o.organizationDescription
            self.__telephonic = o.telephonic
        elif isinstance(o, dict):
            # Assign attributes from dictionary with typechecking
            self.activityDescription = o.get("activityDescription")
            self.electronicAddress = o.get("electronicAddress")
            self.organizationAddress = o.get("organizationAddress")
            self.organizationDescription = o.get("organizationDescription")
            self.telephonic = o.get("telephonic")
        else:
            # Assign attributes from named keywords with typechecking
            self.activityDescription = activityDescription
            self.electronicAddress = electronicAddress
            self.organizationAddress = organizationAddress
            self.organizationDescription = organizationDescription
            self.telephonic = telephonic

    @property
    def activityDescription(self) -> ActivityDescription:
        return self.__activityDescription

    @activityDescription.setter
    def activityDescription(self, val: ActivityDescription) -> None:
        self.__activityDescription = None if val is None else ActivityDescription(val)

    @property
    def electronicAddress(self) -> ElectronicAddress:
        return self.__electronicAddress

    @electronicAddress.setter
    def electronicAddress(self, val: ElectronicAddress) -> None:
        self.__electronicAddress = None if val is None else ElectronicAddress(val)

    @property
    def organizationAddress(self) -> OrganizationAddress:
        return self.__organizationAddress

    @organizationAddress.setter
    def organizationAddress(self, val: OrganizationAddress) -> None:
        self.__organizationAddress = None if val is None else OrganizationAddress(val)

    @property
    def organizationDescription(self) -> OrganizationDescription:
        return self.__organizationDescription

    @organizationDescription.setter
    def organizationDescription(self, val: OrganizationDescription) -> None:
        self.__organizationDescription = (
            None if val is None else OrganizationDescription(val)
        )

    @property
    def telephonic(self) -> Telephonic:
        return self.__telephonic

    @telephonic.setter
    def telephonic(self, val: Telephonic) -> None:
        self.__telephonic = None if val is None else Telephonic(val)
