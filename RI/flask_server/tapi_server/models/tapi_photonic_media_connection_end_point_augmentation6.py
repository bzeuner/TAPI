# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_media_channel_connection_end_point_spec import TapiPhotonicMediaMediaChannelConnectionEndPointSpec  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaConnectionEndPointAugmentation6(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, media_channel_connection_end_point_spec=None):  # noqa: E501
        """TapiPhotonicMediaConnectionEndPointAugmentation6 - a model defined in OpenAPI

        :param media_channel_connection_end_point_spec: The media_channel_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation6.  # noqa: E501
        :type media_channel_connection_end_point_spec: TapiPhotonicMediaMediaChannelConnectionEndPointSpec
        """
        self.openapi_types = {
            'media_channel_connection_end_point_spec': TapiPhotonicMediaMediaChannelConnectionEndPointSpec
        }

        self.attribute_map = {
            'media_channel_connection_end_point_spec': 'media-channel-connection-end-point-spec'
        }

        self._media_channel_connection_end_point_spec = media_channel_connection_end_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaConnectionEndPointAugmentation6':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.ConnectionEndPointAugmentation6 of this TapiPhotonicMediaConnectionEndPointAugmentation6.  # noqa: E501
        :rtype: TapiPhotonicMediaConnectionEndPointAugmentation6
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media_channel_connection_end_point_spec(self):
        """Gets the media_channel_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation6.


        :return: The media_channel_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation6.
        :rtype: TapiPhotonicMediaMediaChannelConnectionEndPointSpec
        """
        return self._media_channel_connection_end_point_spec

    @media_channel_connection_end_point_spec.setter
    def media_channel_connection_end_point_spec(self, media_channel_connection_end_point_spec):
        """Sets the media_channel_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation6.


        :param media_channel_connection_end_point_spec: The media_channel_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation6.
        :type media_channel_connection_end_point_spec: TapiPhotonicMediaMediaChannelConnectionEndPointSpec
        """

        self._media_channel_connection_end_point_spec = media_channel_connection_end_point_spec
