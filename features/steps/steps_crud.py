import os
import mysql.connector
from behave import given, when, then
from src.crud import CRUD
from src.misc import *



@given(u'the database contains the following test data')
def step_impl(context):
    global crud
    crud = CRUD()

    # Ensure the table exists and is empty
    crud.drop_table('test')

    # Create the table and insert the test data
    data = load_data_from_file('/app/assets/data.json')
    data_dict = convert_json_to_data_dict(data)
    crud.create('test', data_dict)


@given(u'an existing table "{table_name}"')
def step_impl(context, table_name):
    global crud
    if not crud:
        crud = CRUD()

    assert table_name in crud.show_tables()


@when(u'I call the insert method with the data')
def step_impl(context):
    data_dict = {}
    for row in context.table:
        for header, value in row.as_dict().items():
            if header not in data_dict:
                data_dict[header] = []
            data_dict[header].append(value)

    crud.insert('test', data_dict)


@then(u'the data should be inserted into the specified table')
def step_impl(context):
    inserted_data = crud.read('test')
    for row in context.table:
        assert row in inserted_data


@when(u'I call the read method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    context.returned_data = crud.read('test', f"Symbol = '{symbol}'")


@then(u'the data returned should be')
def step_impl(context):
    for row in context.table:
        assert row in context.returned_data


@when(u'I call the update method with the set_data and the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    set_data = {}
    for row in context.table:
        for header, value in row.as_dict().items():
            if header not in set_data:
                set_data[header] = []
            set_data[header].append(value)

    crud.update('test', set_data, f"Symbol = '{symbol}'")


@then(u'the data in the specified table should be updated')
def step_impl(context):
    updated_data = crud.read('test')
    for row in context.table:
        assert row in updated_data


@when(u'I call the delete method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    crud.delete('test', f"Symbol = '{symbol}'")


@then(u'the data with the specified symbol should be deleted from the table')
def step_impl(context):
    deleted_data = crud.read('test')
    for row in context.table:
        assert row not in deleted_data


@when(u'I call the drop_table method')
def step_impl(context):
    crud.drop_table('test')


@then(u'the specified table should be dropped from the database')
def step_impl(context):
    table_name = 'test'
    assert table_name not in crud.show_tables()
    crud.close()
