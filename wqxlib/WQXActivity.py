from typing import List

from .exceptions import WQXLibException
from .wqx_v3_0 import (
    Activity,
    ActivityDescription,
    ReferenceMethod,
    Result,
    ResultDescription,
    ResultLabInformation,
    SampleDescription,
)
from .WQXResult import WQXResult
from .WQXSample import WQXSample


class WQXActivity(Activity, ActivityDescription):
    __samples: List[WQXSample] = []
    __results: List[WQXResult] = []

    def __init__(self,):
        Activity.__init__(self)
        ActivityDescription.__init__(self)
        self.samples = []
        self.results = []

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        id = f"{self.monitoringLocationIdentifier}:{self.activityStartDate}:{self.activityTypeCode}"  # noqa B950
        if exception_value is None:
            if self.activityIdentifier is None:
                # Give the activity a default activityIdentifier
                self.activityIdentifier = id
            self.activityDescription = ActivityDescription(self)
            if len(self.__samples) != 1:
                assert WQXLibException(
                    "Each Activity requires a single sampleDescription."
                )
            else:
                sample = self.__samples[0]
                sample.sampleCollectionMethod = ReferenceMethod(sample)
                self.sampleDescription = SampleDescription(sample)
            tmp = []
            for result in self.__results:
                result.resultDescription = ResultDescription(result)
                result.resultLabInformation = ResultLabInformation(result)
                tmp.append(Result(result))
            self.results = tmp

    def sample(self) -> WQXSample:
        tmp = WQXSample()
        self.__samples.append(tmp)
        return tmp

    def result(self) -> WQXResult:
        tmp = WQXResult()
        self.__results.append(tmp)
        return tmp
