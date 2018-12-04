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


class EnginePool(object):
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
        'engines': 'list[int]',
        'id': 'int',
        'links': 'list[Link]',
        'name': 'str'
    }

    attribute_map = {
        'engines': 'engines',
        'id': 'id',
        'links': 'links',
        'name': 'name'
    }

    def __init__(self, engines=None, id=None, links=None, name=None):  # noqa: E501
        """EnginePool - a model defined in Swagger"""  # noqa: E501

        self._engines = None
        self._id = None
        self._links = None
        self._name = None
        self.discriminator = None

        if engines is not None:
            self.engines = engines
        self.id = id
        if links is not None:
            self.links = links
        self.name = name

    @property
    def engines(self):
        """Gets the engines of this EnginePool.  # noqa: E501

        The identifiers of the scan engines in the engine pool.  # noqa: E501

        :return: The engines of this EnginePool.  # noqa: E501
        :rtype: list[int]
        """
        return self._engines

    @engines.setter
    def engines(self, engines):
        """Sets the engines of this EnginePool.

        The identifiers of the scan engines in the engine pool.  # noqa: E501

        :param engines: The engines of this EnginePool.  # noqa: E501
        :type: list[int]
        """

        self._engines = engines

    @property
    def id(self):
        """Gets the id of this EnginePool.  # noqa: E501

        The identifier of the scan engine.  # noqa: E501

        :return: The id of this EnginePool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnginePool.

        The identifier of the scan engine.  # noqa: E501

        :param id: The id of this EnginePool.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def links(self):
        """Gets the links of this EnginePool.  # noqa: E501


        :return: The links of this EnginePool.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EnginePool.


        :param links: The links of this EnginePool.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this EnginePool.  # noqa: E501

        The name of the scan engine.  # noqa: E501

        :return: The name of this EnginePool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnginePool.

        The name of the scan engine.  # noqa: E501

        :param name: The name of this EnginePool.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(EnginePool, dict):
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
        if not isinstance(other, EnginePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
