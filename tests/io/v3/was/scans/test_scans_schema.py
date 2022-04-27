import pytest
from marshmallow.exceptions import ValidationError

from tenable.io.v3.was.scans.schema import ScanReportSchema, ScanStatusSchema


def test_scan_status_schema():
    '''
    Tests ScanStatusSchema
    '''
    schema = ScanStatusSchema()
    payload = {
        'requested_action': 'stop'
    }
    assert payload == schema.dump(schema.load(payload))


def test_scan_report_schema():
    '''
    Tests ScanReportSchema
    '''
    schema = ScanReportSchema()
    payload = {
        'content_type': 'text/csv'
    }
    assert payload == schema.dump(schema.load(payload))


def test_scan_report_schema_contenttype_type_error():
    '''
    Test to raise exception when type of request header Content-Type parameter does not match the expected type.
    '''
    payload = {
        'content_type': 1
    }
    with pytest.raises(ValidationError) as validation_error:
        ScanReportSchema().load(payload)
    assert len(validation_error.value.messages) == 1, "Test case should raise validation error for only one parameter."

    assert len(validation_error.value.messages['content_type']) == 1, \
        "Only one validation error should be raised by test-case for content_type parameter."

    assert validation_error.value.messages['content_type'][0] == "Not a valid string.", \
        "Invalid type validation error for content_type parameter is not raised by test-case."


def test_scan_report_schema_contenttype_invalid_value():
    '''
    Test to raise exception when request header Content-Type parameter value does not match the choices.
    '''
    payload = {
        'content_type': 'test/test'
    }
    with pytest.raises(ValidationError) as validation_error:
        ScanReportSchema().load(payload)
    assert len(validation_error.value.messages) == 1, "Test case should raise validation error for only one parameter."

    assert len(validation_error.value.messages['content_type']) == 1, \
        "Only one validation error should be raised by test-case for content_type parameter."

    assert validation_error.value.messages['content_type'][0].startswith("Must be one of"), \
        "Invalid choice validation error for content_type parameter is not raised by test-case."


def test_scan_status_schema_requestedaction_type_error():
    '''
    Test to raise exception when type of requested_action parameter does not match the expected type.
    '''
    payload = {
        'requested_action': 1
    }
    with pytest.raises(ValidationError) as validation_error:
        ScanStatusSchema().load(payload)
    assert len(validation_error.value.messages) == 1, "Test case should raise validation error for only one parameter."

    assert len(validation_error.value.messages['requested_action']) == 1, \
        "Only one validation error should be raised by test-case for requested_action parameter."

    assert validation_error.value.messages['requested_action'][0] == "Not a valid string.", \
        "Invalid type validation error for requested_action parameter is not raised by test-case."


def test_scan_status_schema_requestedaction_invalid_value():
    '''
    Test to raise exception when requested_action parameter value does not match the choices.
    '''
    payload = {
        'requested_action': 'test'
    }
    with pytest.raises(ValidationError) as validation_error:
        ScanStatusSchema().load(payload)
    assert len(validation_error.value.messages) == 1, "Test case should raise validation error for only one parameter."

    assert len(validation_error.value.messages['requested_action']) == 1, \
        "Only one validation error should be raised by test-case for requested_action parameter."

    assert validation_error.value.messages['requested_action'][0] == "Value not supported", \
        "Invalid value validation error for requested_action parameter is not raised by test-case."
