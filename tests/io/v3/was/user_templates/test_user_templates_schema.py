'''
Test User Template Schema
'''
import pytest
from marshmallow.exceptions import ValidationError

from tenable.io.v3.was.user_templates.schema import (PermissionSchema,
                                                     UserTemplateSchema)

permission_obj = {
    'entity': 'user',
    'entity_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    'permissions_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    'level': 'no_access',
}

user_template_obj = {
    'name': 'Edited template name',
    'default_permissions': 'no_access',
    'permissions': [permission_obj],
    'description': 'edited description',
    'owner_id': 'a8ff6f60-a7e0-43a5-a9d4-0bd079e1d9fa',
    'results_visibility': 'private'
}


def test_user_template_schema():
    '''
    Test user template schema
    '''
    schema = UserTemplateSchema()
    assert user_template_obj == schema.dump(schema.load(user_template_obj))


def test_permission_schema():
    '''
    Test permission schema
    '''
    schema = PermissionSchema()
    assert permission_obj == schema.dump(schema.load(permission_obj))


def test_user_template_schema_parameters_type_error():
    '''
    Test to raise exception when values of name, default_permissions, description, owner_id, results_visibility
    parameters of UserTemplate schema do not match the expected type.
    '''
    payload = {
        'name': 1,
        'default_permissions': 1,
        'description': 1,
        'owner_id': 123,
        'results_visibility': 1
    }
    with pytest.raises(ValidationError) as validation_error:
        UserTemplateSchema().load(payload)
    assert len(validation_error.value.messages) == 5, "Test case should raise validation errors for five parameters."

    assert len(validation_error.value.messages['name']) == 1, \
        "Only one validation error should be raised by test-case for name parameter."
    assert len(validation_error.value.messages['default_permissions']) == 1, \
        "Only one validation error should be raised by test-case for default_permissions parameter."
    assert len(validation_error.value.messages['description']) == 1, \
        "Only one validation error should be raised by test-case for description parameter."
    assert len(validation_error.value.messages['owner_id']) == 1, \
        "Only one validation error should be raised by test-case for owner_id parameter."
    assert len(validation_error.value.messages['results_visibility']) == 1, \
        "Only one validation error should be raised by test-case for results_visibility parameter."

    assert validation_error.value.messages['name'][0] == "Not a valid string.", \
        "Invalid type validation error for name parameter is not raised by test-case."
    assert validation_error.value.messages['default_permissions'][0] == "Not a valid string.", \
        "Invalid type validation error for default_permissions parameter is not raised by test-case."
    assert validation_error.value.messages['description'][0] == "Not a valid string.", \
        "Invalid type validation error for description parameter is not raised by test-case."
    assert validation_error.value.messages['owner_id'][0] == "Not a valid UUID.", \
        "Invalid type validation error for owner_id parameter is not raised by test-case."
    assert validation_error.value.messages['results_visibility'][0] == "Not a valid string.", \
        "Invalid type validation error for results_visibility parameter is not raised by test-case."


def test_user_template_schema_parameters_invalid_value():
    '''
    Test to raise exception when values of default_permissions, results_visibility parameters of UserTemplate schema
    do not match the choices.
    '''
    payload = {
        'default_permissions': 'test',
        'results_visibility': 'test'
    }
    with pytest.raises(ValidationError) as validation_error:
        UserTemplateSchema().load(payload)
    assert len(validation_error.value.messages) == 2, "Test case should raise validation errors for two parameters."

    assert len(validation_error.value.messages['default_permissions']) == 1, \
        "Only one validation error should be raised by test-case for default_permissions parameter."
    assert len(validation_error.value.messages['results_visibility']) == 1, \
        "Only one validation error should be raised by test-case for results_visibility parameter."

    assert validation_error.value.messages['default_permissions'][0].startswith("Must be one of"), \
        "Invalid choice validation error for default_permissions parameter is not raised by test-case."
    assert validation_error.value.messages['results_visibility'][0].startswith("Must be one of"), \
        "Invalid choice validation error for results_visibility parameter is not raised by test-case."


def test_permission_schema_required_parameters_missing_value_error():
    '''
    Test to raise exception when values for entity, entity_id, level, permissions_id required parameters of
    Permission schema are not provided.
    '''
    with pytest.raises(ValidationError) as validation_error:
        PermissionSchema().load({})
    assert len(validation_error.value.messages) == 4, "Test case should raise validation errors for four parameters."

    assert len(validation_error.value.messages['entity']) == 1, \
        "Only one validation error should be raised by test-case for entity parameter."
    assert len(validation_error.value.messages['entity_id']) == 1, \
        "Only one validation error should be raised by test-case for entity_id parameter."
    assert len(validation_error.value.messages['level']) == 1, \
        "Only one validation error should be raised by test-case for level parameter."
    assert len(validation_error.value.messages['permissions_id']) == 1, \
        "Only one validation error should be raised by test-case for permissions_id parameter."

    assert validation_error.value.messages['entity'][0].startswith("Missing data for required field."), \
        "Missing data validation error for entity parameter is not raised by test-case."
    assert validation_error.value.messages['entity_id'][0].startswith("Missing data for required field."), \
        "Missing data validation error for entity_id parameter is not raised by test-case."
    assert validation_error.value.messages['level'][0].startswith("Missing data for required field."), \
        "Missing data validation error for level parameter is not raised by test-case."
    assert validation_error.value.messages['permissions_id'][0].startswith("Missing data for required field."), \
        "Missing data validation error for permissions_id parameter is not raised by test-case."


def test_permission_schema_parameters_type_error():
    '''
    Test to raise exception when values of entity, entity_id, level, permissions_id parameters of Permission schema
    do not match the expected type.
    '''
    payload = {
        'entity': 1,
        'entity_id': 123,
        'level': 1,
        'permissions_id': 123,
    }
    with pytest.raises(ValidationError) as validation_error:
        PermissionSchema().load(payload)
    assert len(validation_error.value.messages) == 4, "Test case should raise validation errors for four parameters."

    assert len(validation_error.value.messages['entity']) == 1, \
        "Only one validation error should be raised by test-case for entity parameter."
    assert len(validation_error.value.messages['entity_id']) == 1, \
        "Only one validation error should be raised by test-case for entity_id parameter."
    assert len(validation_error.value.messages['level']) == 1, \
        "Only one validation error should be raised by test-case for level parameter."
    assert len(validation_error.value.messages['permissions_id']) == 1, \
        "Only one validation error should be raised by test-case for permissions_id parameter."

    assert validation_error.value.messages['entity'][0] == "Not a valid string.", \
        "Invalid type validation error for entity parameter is not raised by test-case."
    assert validation_error.value.messages['entity_id'][0] == "Not a valid UUID.", \
        "Invalid type validation error for entity_id parameter is not raised by test-case."
    assert validation_error.value.messages['level'][0] == "Not a valid string.", \
        "Invalid type validation error for level parameter is not raised by test-case."
    assert validation_error.value.messages['permissions_id'][0] == "Not a valid UUID.", \
        "Invalid type validation error for permissions_id parameter is not raised by test-case."


def test_permission_schema_parameters_invalid_value():
    '''
    Test to raise exception when values of entity, level parameters of Permission schema do not match the choices.
    '''
    payload = {
        'entity': 'test',
        'entity_id': '00000000-0000-0000-0000-000000000000',
        'level': 'test',
        'permissions_id': '00000000-0000-0000-0000-000000000000'
    }
    with pytest.raises(ValidationError) as validation_error:
        PermissionSchema().load(payload)
    assert len(validation_error.value.messages) == 2, "Test case should raise validation errors for two parameters."

    assert len(validation_error.value.messages['entity']) == 1, \
        "Only one validation error should be raised by test-case for entity parameter."
    assert len(validation_error.value.messages['level']) == 1, \
        "Only one validation error should be raised by test-case for level parameter."

    assert validation_error.value.messages['entity'][0].startswith("Must be one of"), \
        "Invalid choice validation error for entity parameter is not raised by test-case."
    assert validation_error.value.messages['level'][0].startswith("Must be one of"), \
        "Invalid choice validation error for level parameter is not raised by test-case."
