# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.scan_template_discovery_performance_packets_rate import ScanTemplateDiscoveryPerformancePacketsRate  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_discovery_performance_parallelism import ScanTemplateDiscoveryPerformanceParallelism  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_discovery_performance_scan_delay import ScanTemplateDiscoveryPerformanceScanDelay  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_discovery_performance_timeout import ScanTemplateDiscoveryPerformanceTimeout  # noqa: F401,E501


class ScanTemplateDiscoveryPerformance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'packet_rate': 'ScanTemplateDiscoveryPerformancePacketsRate',
        'parallelism': 'ScanTemplateDiscoveryPerformanceParallelism',
        'retry_limit': 'int',
        'scan_delay': 'ScanTemplateDiscoveryPerformanceScanDelay',
        'timeout': 'ScanTemplateDiscoveryPerformanceTimeout'
    }

    attribute_map = {
        'packet_rate': 'packetRate',
        'parallelism': 'parallelism',
        'retry_limit': 'retryLimit',
        'scan_delay': 'scanDelay',
        'timeout': 'timeout'
    }

    def __init__(self, packet_rate=None, parallelism=None, retry_limit=None, scan_delay=None, timeout=None):  # noqa: E501
        """ScanTemplateDiscoveryPerformance - a model defined in Swagger"""  # noqa: E501

        self._packet_rate = None
        self._parallelism = None
        self._retry_limit = None
        self._scan_delay = None
        self._timeout = None
        self.discriminator = None

        if packet_rate is not None:
            self.packet_rate = packet_rate
        if parallelism is not None:
            self.parallelism = parallelism
        if retry_limit is not None:
            self.retry_limit = retry_limit
        if scan_delay is not None:
            self.scan_delay = scan_delay
        if timeout is not None:
            self.timeout = timeout

    @property
    def packet_rate(self):
        """Gets the packet_rate of this ScanTemplateDiscoveryPerformance.  # noqa: E501

        The number of packets to send per second during scanning.  # noqa: E501

        :return: The packet_rate of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :rtype: ScanTemplateDiscoveryPerformancePacketsRate
        """
        return self._packet_rate

    @packet_rate.setter
    def packet_rate(self, packet_rate):
        """Sets the packet_rate of this ScanTemplateDiscoveryPerformance.

        The number of packets to send per second during scanning.  # noqa: E501

        :param packet_rate: The packet_rate of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :type: ScanTemplateDiscoveryPerformancePacketsRate
        """

        self._packet_rate = packet_rate

    @property
    def parallelism(self):
        """Gets the parallelism of this ScanTemplateDiscoveryPerformance.  # noqa: E501

        The number of discovery connection requests to be sent to target host simultaneously. These settings has no effect if values have been set for `scanDelay`.  # noqa: E501

        :return: The parallelism of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :rtype: ScanTemplateDiscoveryPerformanceParallelism
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this ScanTemplateDiscoveryPerformance.

        The number of discovery connection requests to be sent to target host simultaneously. These settings has no effect if values have been set for `scanDelay`.  # noqa: E501

        :param parallelism: The parallelism of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :type: ScanTemplateDiscoveryPerformanceParallelism
        """

        self._parallelism = parallelism

    @property
    def retry_limit(self):
        """Gets the retry_limit of this ScanTemplateDiscoveryPerformance.  # noqa: E501

        The maximum number of attempts to contact target assets. If the limit is exceeded with no response, the given asset is not scanned. Defaults to `3`.  # noqa: E501

        :return: The retry_limit of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :rtype: int
        """
        return self._retry_limit

    @retry_limit.setter
    def retry_limit(self, retry_limit):
        """Sets the retry_limit of this ScanTemplateDiscoveryPerformance.

        The maximum number of attempts to contact target assets. If the limit is exceeded with no response, the given asset is not scanned. Defaults to `3`.  # noqa: E501

        :param retry_limit: The retry_limit of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :type: int
        """
        if retry_limit is not None and retry_limit > 15:  # noqa: E501
            raise ValueError("Invalid value for `retry_limit`, must be a value less than or equal to `15`")  # noqa: E501
        if retry_limit is not None and retry_limit < 1:  # noqa: E501
            raise ValueError("Invalid value for `retry_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._retry_limit = retry_limit

    @property
    def scan_delay(self):
        """Gets the scan_delay of this ScanTemplateDiscoveryPerformance.  # noqa: E501

        The duration to wait between sending packets to each target host during a scan.  # noqa: E501

        :return: The scan_delay of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :rtype: ScanTemplateDiscoveryPerformanceScanDelay
        """
        return self._scan_delay

    @scan_delay.setter
    def scan_delay(self, scan_delay):
        """Sets the scan_delay of this ScanTemplateDiscoveryPerformance.

        The duration to wait between sending packets to each target host during a scan.  # noqa: E501

        :param scan_delay: The scan_delay of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :type: ScanTemplateDiscoveryPerformanceScanDelay
        """

        self._scan_delay = scan_delay

    @property
    def timeout(self):
        """Gets the timeout of this ScanTemplateDiscoveryPerformance.  # noqa: E501

        The duration to wait between retry attempts.  # noqa: E501

        :return: The timeout of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :rtype: ScanTemplateDiscoveryPerformanceTimeout
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ScanTemplateDiscoveryPerformance.

        The duration to wait between retry attempts.  # noqa: E501

        :param timeout: The timeout of this ScanTemplateDiscoveryPerformance.  # noqa: E501
        :type: ScanTemplateDiscoveryPerformanceTimeout
        """

        self._timeout = timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScanTemplateDiscoveryPerformance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScanTemplateDiscoveryPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
