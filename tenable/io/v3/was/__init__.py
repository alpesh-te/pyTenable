'''
Web Application Scanning
========================

The following API's are available for interaction under Web Application
Scanning

Methods available on ``tio.v3.was``:


.. rst-class:: hide-signature
.. autoclass:: WebApplicationScanning
    :members:

.. toctree::
    :hidden:
    :glob:

    folders
    templates
    user-templates
'''
from tenable.io.v3.base.endpoints.explore import ExploreBaseEndpoint
from tenable.io.v3.was.folders.api import FoldersAPI
from tenable.io.v3.was.templates.api import TemplatesAPI
from tenable.io.v3.was.user_templates.api import UserTemplatesAPI


class WebApplicationScanning(ExploreBaseEndpoint):  # noqa: PLR0904
    '''
    This class will contain property for all resources under Web Application
    Scanning i.e plugins, scans, folders etc.
    '''

    @property
    def folders(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return FoldersAPI(self._api)

    @property
    def templates(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return TemplatesAPI(self._api)

    @property
    def user_templates(self):
        '''
        The interface object for the
        :doc:`Folders API <folders>`
        '''
        return UserTemplatesAPI(self._api)
