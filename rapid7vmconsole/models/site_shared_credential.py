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


class SiteSharedCredential(object):
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
        'enabled': 'bool',
        'id': 'int',
        'links': 'list[Link]',
        'name': 'str',
        'service': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'service': 'service'
    }

    def __init__(self, enabled=None, id=None, links=None, name=None, service=None):  # noqa: E501
        """SiteSharedCredential - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._id = None
        self._links = None
        self._name = None
        self._service = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if service is not None:
            self.service = service

    @property
    def enabled(self):
        """Gets the enabled of this SiteSharedCredential.  # noqa: E501

        Flag indicating whether the shared credential is enabled for the site's scans.  # noqa: E501

        :return: The enabled of this SiteSharedCredential.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SiteSharedCredential.

        Flag indicating whether the shared credential is enabled for the site's scans.  # noqa: E501

        :param enabled: The enabled of this SiteSharedCredential.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this SiteSharedCredential.  # noqa: E501

        The identifier of the shared credential.  # noqa: E501

        :return: The id of this SiteSharedCredential.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteSharedCredential.

        The identifier of the shared credential.  # noqa: E501

        :param id: The id of this SiteSharedCredential.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this SiteSharedCredential.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this SiteSharedCredential.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SiteSharedCredential.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this SiteSharedCredential.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this SiteSharedCredential.  # noqa: E501

        The name of the shared credential.  # noqa: E501

        :return: The name of this SiteSharedCredential.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteSharedCredential.

        The name of the shared credential.  # noqa: E501

        :param name: The name of this SiteSharedCredential.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service(self):
        """Gets the service of this SiteSharedCredential.  # noqa: E501

        The type of service the credential is configured to authenticate with.  # noqa: E501

        :return: The service of this SiteSharedCredential.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SiteSharedCredential.

        The type of service the credential is configured to authenticate with.  # noqa: E501

        :param service: The service of this SiteSharedCredential.  # noqa: E501
        :type: str
        """
        allowed_values = ["as400", "cifs", "cifshash", "cvs", "db2", "ftp", "http", "ms-sql", "mysql", "notes", "oracle", "pop", "postgresql", "remote-exec", "snmp", "snmpv3", "ssh", "ssh-key", "sybase", "telnet", "kerberos", "hana"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

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
        if issubclass(SiteSharedCredential, dict):
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
        if not isinstance(other, SiteSharedCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
