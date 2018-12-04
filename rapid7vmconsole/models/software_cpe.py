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


class SoftwareCpe(object):
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
        'edition': 'str',
        'language': 'str',
        'other': 'str',
        'part': 'str',
        'product': 'str',
        'sw_edition': 'str',
        'target_hw': 'str',
        'target_sw': 'str',
        'update': 'str',
        'v2_2': 'str',
        'v2_3': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'edition': 'edition',
        'language': 'language',
        'other': 'other',
        'part': 'part',
        'product': 'product',
        'sw_edition': 'swEdition',
        'target_hw': 'targetHW',
        'target_sw': 'targetSW',
        'update': 'update',
        'v2_2': 'v2.2',
        'v2_3': 'v2.3',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, edition=None, language=None, other=None, part=None, product=None, sw_edition=None, target_hw=None, target_sw=None, update=None, v2_2=None, v2_3=None, vendor=None, version=None):  # noqa: E501
        """SoftwareCpe - a model defined in Swagger"""  # noqa: E501

        self._edition = None
        self._language = None
        self._other = None
        self._part = None
        self._product = None
        self._sw_edition = None
        self._target_hw = None
        self._target_sw = None
        self._update = None
        self._v2_2 = None
        self._v2_3 = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if edition is not None:
            self.edition = edition
        if language is not None:
            self.language = language
        if other is not None:
            self.other = other
        self.part = part
        if product is not None:
            self.product = product
        if sw_edition is not None:
            self.sw_edition = sw_edition
        if target_hw is not None:
            self.target_hw = target_hw
        if target_sw is not None:
            self.target_sw = target_sw
        if update is not None:
            self.update = update
        if v2_2 is not None:
            self.v2_2 = v2_2
        if v2_3 is not None:
            self.v2_3 = v2_3
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def edition(self):
        """Gets the edition of this SoftwareCpe.  # noqa: E501

        Edition-related terms applied by the vendor to the product.   # noqa: E501

        :return: The edition of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this SoftwareCpe.

        Edition-related terms applied by the vendor to the product.   # noqa: E501

        :param edition: The edition of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def language(self):
        """Gets the language of this SoftwareCpe.  # noqa: E501

        Defines the language supported in the user interface of the product being described. The format is of the language tag adheres to <a target=\"_blank\" href=\"https://tools.ietf.org/html/rfc5646\">RFC5646</a>.  # noqa: E501

        :return: The language of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SoftwareCpe.

        Defines the language supported in the user interface of the product being described. The format is of the language tag adheres to <a target=\"_blank\" href=\"https://tools.ietf.org/html/rfc5646\">RFC5646</a>.  # noqa: E501

        :param language: The language of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def other(self):
        """Gets the other of this SoftwareCpe.  # noqa: E501

        Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value.   # noqa: E501

        :return: The other of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this SoftwareCpe.

        Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value.   # noqa: E501

        :param other: The other of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._other = other

    @property
    def part(self):
        """Gets the part of this SoftwareCpe.  # noqa: E501

        A single letter code that designates the particular platform part that is being identified.  # noqa: E501

        :return: The part of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this SoftwareCpe.

        A single letter code that designates the particular platform part that is being identified.  # noqa: E501

        :param part: The part of this SoftwareCpe.  # noqa: E501
        :type: str
        """
        if part is None:
            raise ValueError("Invalid value for `part`, must not be `None`")  # noqa: E501
        allowed_values = ["o", "a", "h"]  # noqa: E501
        if part not in allowed_values:
            raise ValueError(
                "Invalid value for `part` ({0}), must be one of {1}"  # noqa: E501
                .format(part, allowed_values)
            )

        self._part = part

    @property
    def product(self):
        """Gets the product of this SoftwareCpe.  # noqa: E501

        the most common and recognizable title or name of the product.  # noqa: E501

        :return: The product of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SoftwareCpe.

        the most common and recognizable title or name of the product.  # noqa: E501

        :param product: The product of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def sw_edition(self):
        """Gets the sw_edition of this SoftwareCpe.  # noqa: E501

        Characterizes how the product is tailored to a particular market or class of end users.   # noqa: E501

        :return: The sw_edition of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._sw_edition

    @sw_edition.setter
    def sw_edition(self, sw_edition):
        """Sets the sw_edition of this SoftwareCpe.

        Characterizes how the product is tailored to a particular market or class of end users.   # noqa: E501

        :param sw_edition: The sw_edition of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._sw_edition = sw_edition

    @property
    def target_hw(self):
        """Gets the target_hw of this SoftwareCpe.  # noqa: E501

        Characterize the instruction set architecture on which the product operates.   # noqa: E501

        :return: The target_hw of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._target_hw

    @target_hw.setter
    def target_hw(self, target_hw):
        """Sets the target_hw of this SoftwareCpe.

        Characterize the instruction set architecture on which the product operates.   # noqa: E501

        :param target_hw: The target_hw of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._target_hw = target_hw

    @property
    def target_sw(self):
        """Gets the target_sw of this SoftwareCpe.  # noqa: E501

        Characterize the software computing environment within which the product operates.  # noqa: E501

        :return: The target_sw of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._target_sw

    @target_sw.setter
    def target_sw(self, target_sw):
        """Sets the target_sw of this SoftwareCpe.

        Characterize the software computing environment within which the product operates.  # noqa: E501

        :param target_sw: The target_sw of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._target_sw = target_sw

    @property
    def update(self):
        """Gets the update of this SoftwareCpe.  # noqa: E501

        Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product.  # noqa: E501

        :return: The update of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this SoftwareCpe.

        Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product.  # noqa: E501

        :param update: The update of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._update = update

    @property
    def v2_2(self):
        """Gets the v2_2 of this SoftwareCpe.  # noqa: E501

        The full CPE string in the <a target=\"_blank\" href=\"https://cpe.mitre.org/files/cpe-specification_2.2.pdf\">CPE 2.2</a> format.  # noqa: E501

        :return: The v2_2 of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._v2_2

    @v2_2.setter
    def v2_2(self, v2_2):
        """Sets the v2_2 of this SoftwareCpe.

        The full CPE string in the <a target=\"_blank\" href=\"https://cpe.mitre.org/files/cpe-specification_2.2.pdf\">CPE 2.2</a> format.  # noqa: E501

        :param v2_2: The v2_2 of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._v2_2 = v2_2

    @property
    def v2_3(self):
        """Gets the v2_3 of this SoftwareCpe.  # noqa: E501

        The full CPE string in the <a target=\"_blank\" href=\"http://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf\">CPE 2.3</a> format.  # noqa: E501

        :return: The v2_3 of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._v2_3

    @v2_3.setter
    def v2_3(self, v2_3):
        """Sets the v2_3 of this SoftwareCpe.

        The full CPE string in the <a target=\"_blank\" href=\"http://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7695.pdf\">CPE 2.3</a> format.  # noqa: E501

        :param v2_3: The v2_3 of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._v2_3 = v2_3

    @property
    def vendor(self):
        """Gets the vendor of this SoftwareCpe.  # noqa: E501

        The person or organization that manufactured or created the product.  # noqa: E501

        :return: The vendor of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this SoftwareCpe.

        The person or organization that manufactured or created the product.  # noqa: E501

        :param vendor: The vendor of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this SoftwareCpe.  # noqa: E501

        Vendor-specific alphanumeric strings characterizing the particular release version of the product.  # noqa: E501

        :return: The version of this SoftwareCpe.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SoftwareCpe.

        Vendor-specific alphanumeric strings characterizing the particular release version of the product.  # noqa: E501

        :param version: The version of this SoftwareCpe.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(SoftwareCpe, dict):
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
        if not isinstance(other, SoftwareCpe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
