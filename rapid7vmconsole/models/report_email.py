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

from rapid7vmconsole.models.report_email_smtp import ReportEmailSmtp  # noqa: F401,E501


class ReportEmail(object):
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
        'access': 'str',
        'additional': 'str',
        'additional_recipients': 'list[str]',
        'asset_access': 'bool',
        'owner': 'str',
        'smtp': 'ReportEmailSmtp'
    }

    attribute_map = {
        'access': 'access',
        'additional': 'additional',
        'additional_recipients': 'additionalRecipients',
        'asset_access': 'assetAccess',
        'owner': 'owner',
        'smtp': 'smtp'
    }

    def __init__(self, access=None, additional=None, additional_recipients=None, asset_access=None, owner=None, smtp=None):  # noqa: E501
        """ReportEmail - a model defined in Swagger"""  # noqa: E501

        self._access = None
        self._additional = None
        self._additional_recipients = None
        self._asset_access = None
        self._owner = None
        self._smtp = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if additional is not None:
            self.additional = additional
        if additional_recipients is not None:
            self.additional_recipients = additional_recipients
        if asset_access is not None:
            self.asset_access = asset_access
        if owner is not None:
            self.owner = owner
        if smtp is not None:
            self.smtp = smtp

    @property
    def access(self):
        """Gets the access of this ReportEmail.  # noqa: E501

        The format to distribute the report in when sending to users who have explicit access to the report.  # noqa: E501

        :return: The access of this ReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this ReportEmail.

        The format to distribute the report in when sending to users who have explicit access to the report.  # noqa: E501

        :param access: The access of this ReportEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "zip", "url", "none"]  # noqa: E501
        if access not in allowed_values:
            raise ValueError(
                "Invalid value for `access` ({0}), must be one of {1}"  # noqa: E501
                .format(access, allowed_values)
            )

        self._access = access

    @property
    def additional(self):
        """Gets the additional of this ReportEmail.  # noqa: E501

        The format to distribute the report to additional recipients.  # noqa: E501

        :return: The additional of this ReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._additional

    @additional.setter
    def additional(self, additional):
        """Sets the additional of this ReportEmail.

        The format to distribute the report to additional recipients.  # noqa: E501

        :param additional: The additional of this ReportEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "zip", "none"]  # noqa: E501
        if additional not in allowed_values:
            raise ValueError(
                "Invalid value for `additional` ({0}), must be one of {1}"  # noqa: E501
                .format(additional, allowed_values)
            )

        self._additional = additional

    @property
    def additional_recipients(self):
        """Gets the additional_recipients of this ReportEmail.  # noqa: E501

        The email address of additional recipients to distribute the report to.  # noqa: E501

        :return: The additional_recipients of this ReportEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_recipients

    @additional_recipients.setter
    def additional_recipients(self, additional_recipients):
        """Sets the additional_recipients of this ReportEmail.

        The email address of additional recipients to distribute the report to.  # noqa: E501

        :param additional_recipients: The additional_recipients of this ReportEmail.  # noqa: E501
        :type: list[str]
        """

        self._additional_recipients = additional_recipients

    @property
    def asset_access(self):
        """Gets the asset_access of this ReportEmail.  # noqa: E501

        ${report.config.email.additional.asset.access.description}  # noqa: E501

        :return: The asset_access of this ReportEmail.  # noqa: E501
        :rtype: bool
        """
        return self._asset_access

    @asset_access.setter
    def asset_access(self, asset_access):
        """Sets the asset_access of this ReportEmail.

        ${report.config.email.additional.asset.access.description}  # noqa: E501

        :param asset_access: The asset_access of this ReportEmail.  # noqa: E501
        :type: bool
        """

        self._asset_access = asset_access

    @property
    def owner(self):
        """Gets the owner of this ReportEmail.  # noqa: E501

        The format to distribute the report to the owner.  # noqa: E501

        :return: The owner of this ReportEmail.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ReportEmail.

        The format to distribute the report to the owner.  # noqa: E501

        :param owner: The owner of this ReportEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "url", "zip", "none"]  # noqa: E501
        if owner not in allowed_values:
            raise ValueError(
                "Invalid value for `owner` ({0}), must be one of {1}"  # noqa: E501
                .format(owner, allowed_values)
            )

        self._owner = owner

    @property
    def smtp(self):
        """Gets the smtp of this ReportEmail.  # noqa: E501

        SMTP delivery settings.  # noqa: E501

        :return: The smtp of this ReportEmail.  # noqa: E501
        :rtype: ReportEmailSmtp
        """
        return self._smtp

    @smtp.setter
    def smtp(self, smtp):
        """Sets the smtp of this ReportEmail.

        SMTP delivery settings.  # noqa: E501

        :param smtp: The smtp of this ReportEmail.  # noqa: E501
        :type: ReportEmailSmtp
        """

        self._smtp = smtp

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
        if issubclass(ReportEmail, dict):
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
        if not isinstance(other, ReportEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
