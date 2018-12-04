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


class SiteOrganization(object):
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
        'address': 'str',
        'city': 'str',
        'contact': 'str',
        'country': 'str',
        'email': 'str',
        'job_title': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'phone': 'str',
        'state': 'str',
        'url': 'str',
        'zip_code': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'contact': 'contact',
        'country': 'country',
        'email': 'email',
        'job_title': 'jobTitle',
        'links': 'links',
        'name': 'name',
        'phone': 'phone',
        'state': 'state',
        'url': 'url',
        'zip_code': 'zipCode'
    }

    def __init__(self, address=None, city=None, contact=None, country=None, email=None, job_title=None, links=None, name=None, phone=None, state=None, url=None, zip_code=None):  # noqa: E501
        """SiteOrganization - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._city = None
        self._contact = None
        self._country = None
        self._email = None
        self._job_title = None
        self._links = None
        self._name = None
        self._phone = None
        self._state = None
        self._url = None
        self._zip_code = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if contact is not None:
            self.contact = contact
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if job_title is not None:
            self.job_title = job_title
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if url is not None:
            self.url = url
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def address(self):
        """Gets the address of this SiteOrganization.  # noqa: E501

        The address.  # noqa: E501

        :return: The address of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SiteOrganization.

        The address.  # noqa: E501

        :param address: The address of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this SiteOrganization.  # noqa: E501

        The city.  # noqa: E501

        :return: The city of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SiteOrganization.

        The city.  # noqa: E501

        :param city: The city of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def contact(self):
        """Gets the contact of this SiteOrganization.  # noqa: E501

        The contact person name.  # noqa: E501

        :return: The contact of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this SiteOrganization.

        The contact person name.  # noqa: E501

        :param contact: The contact of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def country(self):
        """Gets the country of this SiteOrganization.  # noqa: E501

        The country.  # noqa: E501

        :return: The country of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SiteOrganization.

        The country.  # noqa: E501

        :param country: The country of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this SiteOrganization.  # noqa: E501

        The e-mail address.  # noqa: E501

        :return: The email of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SiteOrganization.

        The e-mail address.  # noqa: E501

        :param email: The email of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def job_title(self):
        """Gets the job_title of this SiteOrganization.  # noqa: E501

        The job title.  # noqa: E501

        :return: The job_title of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this SiteOrganization.

        The job title.  # noqa: E501

        :param job_title: The job_title of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def links(self):
        """Gets the links of this SiteOrganization.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this SiteOrganization.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SiteOrganization.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this SiteOrganization.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this SiteOrganization.  # noqa: E501

        The organization name.  # noqa: E501

        :return: The name of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteOrganization.

        The organization name.  # noqa: E501

        :param name: The name of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this SiteOrganization.  # noqa: E501

        The phone number.  # noqa: E501

        :return: The phone of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SiteOrganization.

        The phone number.  # noqa: E501

        :param phone: The phone of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """Gets the state of this SiteOrganization.  # noqa: E501

        The state.  # noqa: E501

        :return: The state of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SiteOrganization.

        The state.  # noqa: E501

        :param state: The state of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def url(self):
        """Gets the url of this SiteOrganization.  # noqa: E501

        The organization URL.  # noqa: E501

        :return: The url of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SiteOrganization.

        The organization URL.  # noqa: E501

        :param url: The url of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def zip_code(self):
        """Gets the zip_code of this SiteOrganization.  # noqa: E501

        The zip or region code.  # noqa: E501

        :return: The zip_code of this SiteOrganization.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this SiteOrganization.

        The zip or region code.  # noqa: E501

        :param zip_code: The zip_code of this SiteOrganization.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

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
        if issubclass(SiteOrganization, dict):
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
        if not isinstance(other, SiteOrganization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
