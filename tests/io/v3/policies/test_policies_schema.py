import pytest
from marshmallow.exceptions import ValidationError

from tenable.io.v3.policies.schema import PolicySchema


@pytest.fixture
def policies_schema():
    '''
    Policy schema
    '''
    return {
        'settings': {
            'patch_audit_over_telnet': 'no',
            'enable_plugin_list': 'no',
            'enumerate_all_ciphers': 'yes'
        },
        'uuid': '731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788aaaaaaaaa',
        'credentials': {
            'current': {}
        }
    }


def test_policies_schema(policies_schema):
    '''
    Test the policies schema
    '''
    schema = PolicySchema()
    payload = schema.dump(
        schema.load(policies_schema)
    )
    assert payload['uuid'] == policies_schema['uuid']
    assert isinstance(payload['settings'], dict)
    assert isinstance(payload['credentials'], dict)


def test_policies_schema_invalid(policies_schema):
    '''
    Test the policies schema
    '''
    schema = PolicySchema()
    policies_schema['uuid'] = 1
    with pytest.raises(ValidationError):
        schema.dump(
            schema.load(policies_schema)
        )
