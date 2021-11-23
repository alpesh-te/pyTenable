from tenable.base.endpoint import APIEndpoint

from .groups import GroupsAPI
from .users import UsersAPI

'''
Version3API
==================

The following sub-package allows for interaction with the Tenable.io
Version3API APIs.

.. rst-class:: hide-signature
.. autoclass:: Version3API
    :members:

.. toctree::
    :hidden:
    :glob:

    groups
    users

'''


class Version3API(APIEndpoint):
    '''
    Version 3 API base class
    '''

    @property
    def groups(self):
        '''
        The interface object for the Groups APIs
        :doc:`Tenable.io.v3.groups Groups APIs <groups>`.
        '''
        return GroupsAPI(self._api)

    @property
    def users(self):
        '''
        The interface object for the
        :doc:`Tenable.io users APIs`.
        '''
        return UsersAPI(self._api)
