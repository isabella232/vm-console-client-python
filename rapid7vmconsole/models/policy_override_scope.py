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


class PolicyOverrideScope(object):
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
        'asset': 'int',
        'links': 'list[Link]',
        'new_result': 'str',
        'original_result': 'str',
        'rule': 'int',
        'type': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'links': 'links',
        'new_result': 'newResult',
        'original_result': 'originalResult',
        'rule': 'rule',
        'type': 'type'
    }

    def __init__(self, asset=None, links=None, new_result=None, original_result=None, rule=None, type=None):  # noqa: E501
        """PolicyOverrideScope - a model defined in Swagger"""  # noqa: E501

        self._asset = None
        self._links = None
        self._new_result = None
        self._original_result = None
        self._rule = None
        self._type = None
        self.discriminator = None

        if asset is not None:
            self.asset = asset
        if links is not None:
            self.links = links
        self.new_result = new_result
        if original_result is not None:
            self.original_result = original_result
        self.rule = rule
        self.type = type

    @property
    def asset(self):
        """Gets the asset of this PolicyOverrideScope.  # noqa: E501

        The identifier of the asset whose compliance results are to be overridden. Property is required if the property `scope` is set to either `\"specific-asset\"` or `\"specific-asset-until-next-scan\"`.  # noqa: E501

        :return: The asset of this PolicyOverrideScope.  # noqa: E501
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this PolicyOverrideScope.

        The identifier of the asset whose compliance results are to be overridden. Property is required if the property `scope` is set to either `\"specific-asset\"` or `\"specific-asset-until-next-scan\"`.  # noqa: E501

        :param asset: The asset of this PolicyOverrideScope.  # noqa: E501
        :type: int
        """

        self._asset = asset

    @property
    def links(self):
        """Gets the links of this PolicyOverrideScope.  # noqa: E501


        :return: The links of this PolicyOverrideScope.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyOverrideScope.


        :param links: The links of this PolicyOverrideScope.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def new_result(self):
        """Gets the new_result of this PolicyOverrideScope.  # noqa: E501

        The new policy rule result after the override is applied.  # noqa: E501

        :return: The new_result of this PolicyOverrideScope.  # noqa: E501
        :rtype: str
        """
        return self._new_result

    @new_result.setter
    def new_result(self, new_result):
        """Sets the new_result of this PolicyOverrideScope.

        The new policy rule result after the override is applied.  # noqa: E501

        :param new_result: The new_result of this PolicyOverrideScope.  # noqa: E501
        :type: str
        """
        if new_result is None:
            raise ValueError("Invalid value for `new_result`, must not be `None`")  # noqa: E501
        allowed_values = ["pass", "fail", "not-applicable", "fixed"]  # noqa: E501
        if new_result not in allowed_values:
            raise ValueError(
                "Invalid value for `new_result` ({0}), must be one of {1}"  # noqa: E501
                .format(new_result, allowed_values)
            )

        self._new_result = new_result

    @property
    def original_result(self):
        """Gets the original_result of this PolicyOverrideScope.  # noqa: E501

        The original policy rule result before the override was applied. This property only applies to overrides with a scope of either `\"specific-asset\"` or `\"specific-asset-until-next-scan\"`.  # noqa: E501

        :return: The original_result of this PolicyOverrideScope.  # noqa: E501
        :rtype: str
        """
        return self._original_result

    @original_result.setter
    def original_result(self, original_result):
        """Sets the original_result of this PolicyOverrideScope.

        The original policy rule result before the override was applied. This property only applies to overrides with a scope of either `\"specific-asset\"` or `\"specific-asset-until-next-scan\"`.  # noqa: E501

        :param original_result: The original_result of this PolicyOverrideScope.  # noqa: E501
        :type: str
        """
        allowed_values = ["pass", "fail", "error", "unknown", "not-applicable", "not-checked", "not-selected", "informational", "fixed"]  # noqa: E501
        if original_result not in allowed_values:
            raise ValueError(
                "Invalid value for `original_result` ({0}), must be one of {1}"  # noqa: E501
                .format(original_result, allowed_values)
            )

        self._original_result = original_result

    @property
    def rule(self):
        """Gets the rule of this PolicyOverrideScope.  # noqa: E501

        The identifier of the policy rule whose compliance results are to be overridden.  # noqa: E501

        :return: The rule of this PolicyOverrideScope.  # noqa: E501
        :rtype: int
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this PolicyOverrideScope.

        The identifier of the policy rule whose compliance results are to be overridden.  # noqa: E501

        :param rule: The rule of this PolicyOverrideScope.  # noqa: E501
        :type: int
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

    @property
    def type(self):
        """Gets the type of this PolicyOverrideScope.  # noqa: E501

        The scope of assets affected by the policy override. Can be one of the following values:  | Value                              | Description                                                                                                                                                 |  | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |  | `\"all-assets\"`                     | Overrides the compliance result of all assets evaluated with the specified policy rule.                                                                     |  | `\"specific-asset\"`                 | Overrides the compliance result of a single asset evaluated with the specified policy rule.                                                                 |  | `\"specific-asset-until-next-scan\"` | Overrides the compliance result of a single asset evaluated with the specified policy rule until the next time asset is evaluated against that policy rule. |    # noqa: E501

        :return: The type of this PolicyOverrideScope.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyOverrideScope.

        The scope of assets affected by the policy override. Can be one of the following values:  | Value                              | Description                                                                                                                                                 |  | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |  | `\"all-assets\"`                     | Overrides the compliance result of all assets evaluated with the specified policy rule.                                                                     |  | `\"specific-asset\"`                 | Overrides the compliance result of a single asset evaluated with the specified policy rule.                                                                 |  | `\"specific-asset-until-next-scan\"` | Overrides the compliance result of a single asset evaluated with the specified policy rule until the next time asset is evaluated against that policy rule. |    # noqa: E501

        :param type: The type of this PolicyOverrideScope.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(PolicyOverrideScope, dict):
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
        if not isinstance(other, PolicyOverrideScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
