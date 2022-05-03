'''
Testing the Logos schemas
'''
import pytest
from marshmallow import ValidationError
from tenable.io.v3.mssp.logos.schema import LogoSchema


def test_schema():
    '''
    Validates schema for Logos API
    '''
    payload = {
        'account_ids': ['0fc4ef49-2649-4c76-bfa7-c181be3adf26'],
        'logo_id': 'a39f6b74-9b7f-4372-a7ac-a2a4bcb8dbad'
    }
    schema = LogoSchema()
    assert schema.load(schema.dump(payload)) == payload


def test_logos_schema_logo_id_typeerror():
    '''
    Test to raise exception when type of request header logo_id parameter does not match the expected type.
    '''
    schema = LogoSchema()
    payload = {
        'logo_id': 00
    }
    with pytest.raises(ValidationError):
        schema.load(payload)


def test_logos_delete_typeerror(api):
    '''test to raise the exception when pass extra argument'''
    with pytest.raises(TypeError):
        api.v3.mssp.logos.delete("Test", 11)


def test_logo_schema_parameters_validation_error():
    '''
    Test to raise exception when values of account_ids parameters of Logo schema do not match the expected type.
    '''
    payload = {
        'account_ids': 1
    }
    with pytest.raises(ValidationError) as validation_error:
        LogoSchema().load(payload)
    assert len(validation_error.value.messages) == 1, "Test case should raise validation errors for 1 parameters."

    assert len(validation_error.value.messages['account_ids']) == 1, \
        "Only one validation error should be raised by test-case for account_ids parameter."

    assert validation_error.value.messages['account_ids'][0] == "Not a valid list.", \
        "Invalid type validation error for account_ids parameter is not raised by test-case."
