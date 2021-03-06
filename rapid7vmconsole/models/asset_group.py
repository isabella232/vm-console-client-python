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


class AssetGroup(object):
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
        'assets': 'int',
        'description': 'str',
        'id': 'int',
        'links': 'list[Link]',
        'name': 'str',
        'risk_score': 'float',
        'search_criteria': 'SearchCriteria',
        'type': 'str',
        'vulnerabilities': 'Vulnerabilities'
    }

    attribute_map = {
        'assets': 'assets',
        'description': 'description',
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'risk_score': 'riskScore',
        'search_criteria': 'searchCriteria',
        'type': 'type',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, assets=None, description=None, id=None, links=None, name=None, risk_score=None, search_criteria=None, type=None, vulnerabilities=None):  # noqa: E501
        """AssetGroup - a model defined in Swagger"""  # noqa: E501

        self._assets = None
        self._description = None
        self._id = None
        self._links = None
        self._name = None
        self._risk_score = None
        self._search_criteria = None
        self._type = None
        self._vulnerabilities = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        self.name = name
        if risk_score is not None:
            self.risk_score = risk_score
        if search_criteria is not None:
            self.search_criteria = search_criteria
        self.type = type
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def assets(self):
        """Gets the assets of this AssetGroup.  # noqa: E501

        The number of assets that belong to the asset group.  # noqa: E501

        :return: The assets of this AssetGroup.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetGroup.

        The number of assets that belong to the asset group.  # noqa: E501

        :param assets: The assets of this AssetGroup.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def description(self):
        """Gets the description of this AssetGroup.  # noqa: E501

        The description of the asset group.  # noqa: E501

        :return: The description of this AssetGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetGroup.

        The description of the asset group.  # noqa: E501

        :param description: The description of this AssetGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AssetGroup.  # noqa: E501

        The identifier of the asset group.  # noqa: E501

        :return: The id of this AssetGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetGroup.

        The identifier of the asset group.  # noqa: E501

        :param id: The id of this AssetGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this AssetGroup.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this AssetGroup.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssetGroup.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this AssetGroup.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this AssetGroup.  # noqa: E501

        The name of the asset group.  # noqa: E501

        :return: The name of this AssetGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetGroup.

        The name of the asset group.  # noqa: E501

        :param name: The name of this AssetGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def risk_score(self):
        """Gets the risk_score of this AssetGroup.  # noqa: E501

        The total risk score of all assets that belong to the asset group.  # noqa: E501

        :return: The risk_score of this AssetGroup.  # noqa: E501
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this AssetGroup.

        The total risk score of all assets that belong to the asset group.  # noqa: E501

        :param risk_score: The risk_score of this AssetGroup.  # noqa: E501
        :type: float
        """

        self._risk_score = risk_score

    @property
    def search_criteria(self):
        """Gets the search_criteria of this AssetGroup.  # noqa: E501

        Search criteria used to determine dynamic membership, if `type` is `\"dynamic\"`.   # noqa: E501

        :return: The search_criteria of this AssetGroup.  # noqa: E501
        :rtype: SearchCriteria
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this AssetGroup.

        Search criteria used to determine dynamic membership, if `type` is `\"dynamic\"`.   # noqa: E501

        :param search_criteria: The search_criteria of this AssetGroup.  # noqa: E501
        :type: SearchCriteria
        """

        self._search_criteria = search_criteria

    @property
    def type(self):
        """Gets the type of this AssetGroup.  # noqa: E501

        The type of the asset group.  # noqa: E501

        :return: The type of this AssetGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssetGroup.

        The type of the asset group.  # noqa: E501

        :param type: The type of this AssetGroup.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["static", "dynamic"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this AssetGroup.  # noqa: E501

        Summary information for distinct vulnerabilities found on the assets.  # noqa: E501

        :return: The vulnerabilities of this AssetGroup.  # noqa: E501
        :rtype: Vulnerabilities
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this AssetGroup.

        Summary information for distinct vulnerabilities found on the assets.  # noqa: E501

        :param vulnerabilities: The vulnerabilities of this AssetGroup.  # noqa: E501
        :type: Vulnerabilities
        """

        self._vulnerabilities = vulnerabilities

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
        if issubclass(AssetGroup, dict):
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
        if not isinstance(other, AssetGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
