'''
Testing the CSV iterators
'''

import responses

from tenable.io.v3.base.iterators.explore_iterator import CSVChunkIterator

USERS_BASE_URL = r'https://cloud.tenable.com/api/v3/assets/search'

CSV_TEXT = (
    'created,display_ipv4_address,first_observed,id,'
    'ipv4_addresses,ipv6_addresses,is_deleted,is_licensed,'
    'is_public,last_observed,name,network.id,network.name,'
    'observation_sources,sources,types,updated\n'
    '2021-11-24T13:43:56.709Z,192.12.13.7,2021-11-24T13:43:56.442Z,'
    '"0142df77-dbc4-4706-8456-b756c06ee8a2",192.12.13.7,,false,'
    'false,true,2021-11-24T13:43:56.442Z,192.12.13.7,'
    '"00000000-0000-0000-0000-000000000000",Default,'
    '"test_v3;2021-11-24T13:43:56.442Z;2021-11-24T13:43:56.442Z",'
    'test_v3,host,2021-11-24T13:43:56.709Z\n'
)

CSV_TEXT_2 = (
    'created,display_ipv4_address,first_observed,id,ipv4_addresses,'
    'ipv6_addresses,is_deleted,is_licensed,is_public,last_observed,'
    'name,network.id,network.name,observation_sources,sources,'
    'types,updated\ncreated,display_ipv4_address,first_observed,id,'
    'ipv4_addresses,ipv6_addresses,is_deleted,is_licensed,'
    'is_public,last_observed,name,network.id,network.name,'
    'observation_sources,sources,types,updated\n'
    '2021-11-24T13:43:56.709Z,192.12.13.7,2021-11-24T13:43:56.442Z,'
    '"0142df77-dbc4-4706-8456-b756c06ee8a2",192.12.13.7,,'
    'false,false,true,2021-11-24T13:43:56.442Z,192.12.13.7,'
    '"00000000-0000-0000-0000-000000000000",Default,'
    '"test_v3;2021-11-24T13:43:56.442Z;2021-11-24T13:43:56.442Z",'
    'test_v3,host,2021-11-24T13:43:56.709Z\n'
)

CSV_HEADERS = {
    'Date': 'Wed, 08 Dec 2021 04:42:28 GMT',
    'Content-Type': 'text/csv;charset=UTF-8',
    'Content-Length': '508',
    'Connection': 'keep-alive',
    'Set-Cookie': 'nginx-cloud-site-id=qa-develop; path=/; '
    'HttpOnly; SameSite=Strict; Secure',
    'X-Request-Uuid': '4d43db5bac4decd79fc198e06a8113bd',
    'X-Continuation-Token': 'fasd563456fghfgfFGHFGHRT',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-Xss-Protection': '1; mode=block',
    'Cache-Control': 'no-store',
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains',
    'X-Gateway-Site-ID': 'nginx-router-jm8uw-us-east-1-eng',
    'Pragma': 'no-cache',
    'Expect-CT': 'enforce, max-age=86400',
    'X-Path-Handler': 'tenable-io',
}


@responses.activate
def test_csv_iterator(api):
    responses.add(
        method=responses.POST,
        url=USERS_BASE_URL,
        body=CSV_TEXT,
        headers=CSV_HEADERS
    )

    csv_iterator = CSVChunkIterator(
        api=api,
        _path='api/v3/assets/search',
        _payload={}
    )
    assert next(csv_iterator) == CSV_TEXT
    assert next(csv_iterator) == CSV_TEXT_2
