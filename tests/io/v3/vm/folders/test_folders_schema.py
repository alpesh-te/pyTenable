'''
Testing the Folders Schema
'''
import pytest
from marshmallow import ValidationError
from tenable.io.v3.vm.folders.schema import FolderSchema

FOLDER_NAME = 'folder'
FOLDER = {
    'name': FOLDER_NAME
}


def test_folders_schema(api):
    schema = FolderSchema()
    payload = schema.dump(schema.load(FOLDER))
    assert payload == FOLDER


def test_folders_schema_name_typeerror():
    '''
    Test to raise exception when type of request header name parameter does not match the expected type.
    '''
    schema = FolderSchema()
    payload = {
        'name': 1
    }
    with pytest.raises(ValidationError):
        schema.load(payload)
