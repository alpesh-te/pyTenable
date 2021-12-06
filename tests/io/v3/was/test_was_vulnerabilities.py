'''
Testing the WAS Vulnerabilities endpoints actions
'''
import responses

from tenable.io.v3.was.vulnerability import VulnerabilityIterator

VUL_BASE_URL = r'https://cloud.tenable.com/api/v3/findings/vulnerabilities'
BASE_URL = r'https://cloud.tenable.com'


@responses.activate
def test_get_details(api):
    '''
    Test the get_details method for WAS Vulnerabilities
    '''
    id = '00089a45-44a7-4620-bf9f-75ebedc6cc6c'
    response = {
        'findings': [{
            'id': id,
            'asset': {},
            'definition': {
                'vpr': {},
                'cvss2': {},
                'cvss3': {},
                'references': [],
                'exploit_frameworks': []
            },
            'scan': {}
        }],
        'pagination': {
            'total': 1
        }
    }
    responses.add(
        responses.GET,
        f"{VUL_BASE_URL}/webapp/{id}",
        json=response
    )

    resp = api.v3.was.vulnerability.get_details(id)
    assert resp == response


@responses.activate
def test_search(api):
    '''
    Test the search functionality of Vulnerability API
    '''
    filter = ('id', 'eq', '00089a45-44a7-4620-bf9f-75ebedc6cc6c')
    fields = ["id"]
    limit = 2

    payload = {
        'fields': ['id'],
        'limit': 2,
        'sort': [],
        'filter': {
            'operator': 'eq',
            'property': 'id',
            'value': '00089a45-44a7-4620-bf9f-75ebedc6cc6c'
        }
    }
    response = {
        'findings': [{
            'id': '00089a45-44a7-4620-bf9f-75ebedc6cc6c',
            'asset': {},
            'definition': {
                'vpr': {},
                'cvss2': {},
                'cvss3': {},
                'references': [],
                'exploit_frameworks': []
            },
            'scan': {}
        }],
        'pagination': {
            'total': 1
        }
    }
    responses.add(
        responses.POST,
        f"{VUL_BASE_URL}/webapp/search",
        json=response
    )

    resp = api.v3.was.vulnerability.search(filter, fields=fields, limit=limit)
    assert isinstance(resp, VulnerabilityIterator)
    assert resp._payload == payload
    assert list(resp) == response.get("findings")
