# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rapid7vmconsole.api_client import ApiClient


class RemediationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_asset_vulnerability_solutions(self, id, vulnerability_id, **kwargs):  # noqa: E501
        """Asset Vulnerability Solution  # noqa: E501

        Returns the highest-superceding rollup solutions for a vulnerability on an asset. The solution(s) selected will be the most recent and cost-effective means by which the vulnerability can be remediated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_vulnerability_solutions(id, vulnerability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the asset. (required)
        :param str vulnerability_id: The identifier of the vulnerability. (required)
        :return: ResourcesMatchedSolution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_vulnerability_solutions_with_http_info(id, vulnerability_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_vulnerability_solutions_with_http_info(id, vulnerability_id, **kwargs)  # noqa: E501
            return data

    def get_asset_vulnerability_solutions_with_http_info(self, id, vulnerability_id, **kwargs):  # noqa: E501
        """Asset Vulnerability Solution  # noqa: E501

        Returns the highest-superceding rollup solutions for a vulnerability on an asset. The solution(s) selected will be the most recent and cost-effective means by which the vulnerability can be remediated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_vulnerability_solutions_with_http_info(id, vulnerability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the asset. (required)
        :param str vulnerability_id: The identifier of the vulnerability. (required)
        :return: ResourcesMatchedSolution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'vulnerability_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_vulnerability_solutions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_asset_vulnerability_solutions`")  # noqa: E501
        # verify the required parameter 'vulnerability_id' is set
        if ('vulnerability_id' not in params or
                params['vulnerability_id'] is None):
            raise ValueError("Missing the required parameter `vulnerability_id` when calling `get_asset_vulnerability_solutions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'vulnerability_id' in params:
            path_params['vulnerabilityId'] = params['vulnerability_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/3/assets/{id}/vulnerabilities/{vulnerabilityId}/solution', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesMatchedSolution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
