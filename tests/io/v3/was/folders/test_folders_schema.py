'''
Testing the Folders Schema
'''
import pytest
from marshmallow.exceptions import ValidationError
from tenable.io.v3.was.folders.schema import FolderSchema

FOLDER_NAME = 'folder'
FOLDER = {
    'name': FOLDER_NAME
}


def test_was_folders_schema(api):
    '''
    Test folders schema
    '''
    schema = FolderSchema()
    payload = schema.dump(schema.load(FOLDER))
    assert payload == FOLDER


def test_was_folders_schema_name_typeerror():
    '''
    Test to raise exception when type of request header name parameter does not match the expected type.
    '''
    schema = FolderSchema()
    payload = {
        'name': 00
    }
    with pytest.raises(ValidationError):
        schema.load(payload)


def test_was_folder_edit_name_typeerror(api):
    '''test to raise the exception when missing required argument'''
    with pytest.raises(TypeError):
        api.v3.was.folders.edit(00)


def test_was_folder_edit_name_validationerror(api):
    '''test to raise the exception when value is not valid'''
    with pytest.raises(ValidationError):
        api.v3.was.folders.edit("Test", 00)


def test_was_folder_create_typeerror(api):
    '''test to raise the exception when pass extra argument'''
    with pytest.raises(TypeError):
        api.v3.was.folders.create(00, 00)


def test_was_folder_create_validationerror(api):
    '''test to raise the exception when value is not valid'''
    with pytest.raises(ValidationError):
        api.v3.was.folders.create(11)
