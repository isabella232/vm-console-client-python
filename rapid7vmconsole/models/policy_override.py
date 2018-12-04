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

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.policy_override_reviewer import PolicyOverrideReviewer  # noqa: F401,E501
from rapid7vmconsole.models.policy_override_scope import PolicyOverrideScope  # noqa: F401,E501
from rapid7vmconsole.models.policy_override_submitter import PolicyOverrideSubmitter  # noqa: F401,E501


class PolicyOverride(object):
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
        'expires': 'str',
        'id': 'int',
        'links': 'list[Link]',
        'review': 'PolicyOverrideReviewer',
        'scope': 'PolicyOverrideScope',
        'state': 'str',
        'submit': 'PolicyOverrideSubmitter'
    }

    attribute_map = {
        'expires': 'expires',
        'id': 'id',
        'links': 'links',
        'review': 'review',
        'scope': 'scope',
        'state': 'state',
        'submit': 'submit'
    }

    def __init__(self, expires=None, id=None, links=None, review=None, scope=None, state=None, submit=None):  # noqa: E501
        """PolicyOverride - a model defined in Swagger"""  # noqa: E501

        self._expires = None
        self._id = None
        self._links = None
        self._review = None
        self._scope = None
        self._state = None
        self._submit = None
        self.discriminator = None

        if expires is not None:
            self.expires = expires
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if review is not None:
            self.review = review
        self.scope = scope
        self.state = state
        self.submit = submit

    @property
    def expires(self):
        """Gets the expires of this PolicyOverride.  # noqa: E501

        The date the policy override is set to expire. Date is represented in ISO 8601 format.  # noqa: E501

        :return: The expires of this PolicyOverride.  # noqa: E501
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this PolicyOverride.

        The date the policy override is set to expire. Date is represented in ISO 8601 format.  # noqa: E501

        :param expires: The expires of this PolicyOverride.  # noqa: E501
        :type: str
        """

        self._expires = expires

    @property
    def id(self):
        """Gets the id of this PolicyOverride.  # noqa: E501

        The identifier of the policy override.  # noqa: E501

        :return: The id of this PolicyOverride.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyOverride.

        The identifier of the policy override.  # noqa: E501

        :param id: The id of this PolicyOverride.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this PolicyOverride.  # noqa: E501


        :return: The links of this PolicyOverride.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyOverride.


        :param links: The links of this PolicyOverride.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def review(self):
        """Gets the review of this PolicyOverride.  # noqa: E501

        Details regarding the review and/or approval of the policy override.  # noqa: E501

        :return: The review of this PolicyOverride.  # noqa: E501
        :rtype: PolicyOverrideReviewer
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this PolicyOverride.

        Details regarding the review and/or approval of the policy override.  # noqa: E501

        :param review: The review of this PolicyOverride.  # noqa: E501
        :type: PolicyOverrideReviewer
        """

        self._review = review

    @property
    def scope(self):
        """Gets the scope of this PolicyOverride.  # noqa: E501

        The scope of the policy override. Indicates which assets' policy compliance results are to be affected by the override.  # noqa: E501

        :return: The scope of this PolicyOverride.  # noqa: E501
        :rtype: PolicyOverrideScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PolicyOverride.

        The scope of the policy override. Indicates which assets' policy compliance results are to be affected by the override.  # noqa: E501

        :param scope: The scope of this PolicyOverride.  # noqa: E501
        :type: PolicyOverrideScope
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def state(self):
        """Gets the state of this PolicyOverride.  # noqa: E501

        The state of the policy override. Can be one of the following values:  | Value            | Description                                                                         | Affects Compliance Results |  | ---------------- | ----------------------------------------------------------------------------------- |:--------------------------:|  | `\"deleted\"`      | The policy override has been deleted.                                               |                            |  | `\"expired\"`      | The policy override had an expiration date and it has expired.                      |                            |  | `\"approved\"`     | The policy override was submitted and approved.                                     | &check;                    |  | `\"rejected\"`     | The policy override was rejected by the reviewer.                                   |                            |  | `\"under-review\"` | The policy override was submitted but not yet approved or rejected by the reviewer. |                            |    # noqa: E501

        :return: The state of this PolicyOverride.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PolicyOverride.

        The state of the policy override. Can be one of the following values:  | Value            | Description                                                                         | Affects Compliance Results |  | ---------------- | ----------------------------------------------------------------------------------- |:--------------------------:|  | `\"deleted\"`      | The policy override has been deleted.                                               |                            |  | `\"expired\"`      | The policy override had an expiration date and it has expired.                      |                            |  | `\"approved\"`     | The policy override was submitted and approved.                                     | &check;                    |  | `\"rejected\"`     | The policy override was rejected by the reviewer.                                   |                            |  | `\"under-review\"` | The policy override was submitted but not yet approved or rejected by the reviewer. |                            |    # noqa: E501

        :param state: The state of this PolicyOverride.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def submit(self):
        """Gets the submit of this PolicyOverride.  # noqa: E501

        Details regarding the submission of the policy override.  # noqa: E501

        :return: The submit of this PolicyOverride.  # noqa: E501
        :rtype: PolicyOverrideSubmitter
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        """Sets the submit of this PolicyOverride.

        Details regarding the submission of the policy override.  # noqa: E501

        :param submit: The submit of this PolicyOverride.  # noqa: E501
        :type: PolicyOverrideSubmitter
        """
        if submit is None:
            raise ValueError("Invalid value for `submit`, must not be `None`")  # noqa: E501

        self._submit = submit

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
        if issubclass(PolicyOverride, dict):
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
        if not isinstance(other, PolicyOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
