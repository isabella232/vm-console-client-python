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


class ScanSettings(object):
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
        'connection_timeout': 'str',
        'incremental': 'bool',
        'maximum_threads': 'int',
        'read_timeout': 'str',
        'status_idle_timeout': 'str',
        'status_threads': 'int'
    }

    attribute_map = {
        'connection_timeout': 'connectionTimeout',
        'incremental': 'incremental',
        'maximum_threads': 'maximumThreads',
        'read_timeout': 'readTimeout',
        'status_idle_timeout': 'statusIdleTimeout',
        'status_threads': 'statusThreads'
    }

    def __init__(self, connection_timeout=None, incremental=None, maximum_threads=None, read_timeout=None, status_idle_timeout=None, status_threads=None):  # noqa: E501
        """ScanSettings - a model defined in Swagger"""  # noqa: E501

        self._connection_timeout = None
        self._incremental = None
        self._maximum_threads = None
        self._read_timeout = None
        self._status_idle_timeout = None
        self._status_threads = None
        self.discriminator = None

        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        if incremental is not None:
            self.incremental = incremental
        if maximum_threads is not None:
            self.maximum_threads = maximum_threads
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if status_idle_timeout is not None:
            self.status_idle_timeout = status_idle_timeout
        if status_threads is not None:
            self.status_threads = status_threads

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this ScanSettings.  # noqa: E501

        The connection timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: `\"PT15S\"`.  # noqa: E501

        :return: The connection_timeout of this ScanSettings.  # noqa: E501
        :rtype: str
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this ScanSettings.

        The connection timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: `\"PT15S\"`.  # noqa: E501

        :param connection_timeout: The connection_timeout of this ScanSettings.  # noqa: E501
        :type: str
        """

        self._connection_timeout = connection_timeout

    @property
    def incremental(self):
        """Gets the incremental of this ScanSettings.  # noqa: E501

        Whether incremental scan results is enabled.  # noqa: E501

        :return: The incremental of this ScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this ScanSettings.

        Whether incremental scan results is enabled.  # noqa: E501

        :param incremental: The incremental of this ScanSettings.  # noqa: E501
        :type: bool
        """

        self._incremental = incremental

    @property
    def maximum_threads(self):
        """Gets the maximum_threads of this ScanSettings.  # noqa: E501

        The maximum number of scan threads to use in any scan. -1 means this is set by the scan template.  # noqa: E501

        :return: The maximum_threads of this ScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._maximum_threads

    @maximum_threads.setter
    def maximum_threads(self, maximum_threads):
        """Sets the maximum_threads of this ScanSettings.

        The maximum number of scan threads to use in any scan. -1 means this is set by the scan template.  # noqa: E501

        :param maximum_threads: The maximum_threads of this ScanSettings.  # noqa: E501
        :type: int
        """

        self._maximum_threads = maximum_threads

    @property
    def read_timeout(self):
        """Gets the read_timeout of this ScanSettings.  # noqa: E501

        The read timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: `\"PT15M\"`.  # noqa: E501

        :return: The read_timeout of this ScanSettings.  # noqa: E501
        :rtype: str
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this ScanSettings.

        The read timeout when establishing connections to remote scan engines, in ISO 8601 format. For example: `\"PT15M\"`.  # noqa: E501

        :param read_timeout: The read_timeout of this ScanSettings.  # noqa: E501
        :type: str
        """

        self._read_timeout = read_timeout

    @property
    def status_idle_timeout(self):
        """Gets the status_idle_timeout of this ScanSettings.  # noqa: E501

        The idle timeout when checking the status of running scans, in ISO 8601 format. For example: `\"PT3M\"`.  # noqa: E501

        :return: The status_idle_timeout of this ScanSettings.  # noqa: E501
        :rtype: str
        """
        return self._status_idle_timeout

    @status_idle_timeout.setter
    def status_idle_timeout(self, status_idle_timeout):
        """Sets the status_idle_timeout of this ScanSettings.

        The idle timeout when checking the status of running scans, in ISO 8601 format. For example: `\"PT3M\"`.  # noqa: E501

        :param status_idle_timeout: The status_idle_timeout of this ScanSettings.  # noqa: E501
        :type: str
        """

        self._status_idle_timeout = status_idle_timeout

    @property
    def status_threads(self):
        """Gets the status_threads of this ScanSettings.  # noqa: E501

        The number of threads to use when checking the status of running scans.  # noqa: E501

        :return: The status_threads of this ScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._status_threads

    @status_threads.setter
    def status_threads(self, status_threads):
        """Sets the status_threads of this ScanSettings.

        The number of threads to use when checking the status of running scans.  # noqa: E501

        :param status_threads: The status_threads of this ScanSettings.  # noqa: E501
        :type: int
        """

        self._status_threads = status_threads

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
        if issubclass(ScanSettings, dict):
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
        if not isinstance(other, ScanSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
