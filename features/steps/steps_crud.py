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

    if not table_name in crud.show_tables():
        # Create the table and insert the test data
        data = load_data_from_file('/app/assets/data.json')
        data_dict = convert_json_to_data_dict(data)
        crud.create('test', data_dict)

@when(u'I call the insert method with the data')
def step_impl(context):
    insert_data = []
    for row in context.table:
        row_dict = {}
        for header, value in row.as_dict().items():
            row_dict[header] = value
        insert_data.append(row_dict)

    context.insert_data = insert_data
    crud.insert('test', insert_data)




@then(u'the data should be inserted into the specified table')
def step_impl(context):
    inserted_data = crud.read('test')

    for row_dict in context.insert_data:

        # Convert numeric string values to their respective numeric types
        row_dict['Price'] = float(row_dict['Price'])
        row_dict['MarketCap'] = int(row_dict['MarketCap'])
        row_dict['MagicformulaIndex'] = int(row_dict['MagicformulaIndex'])
        row_dict['AquirersMultiple'] = int(row_dict['AquirersMultiple'])

        print("INSERTED", inserted_data)
        assert row_dict in inserted_data








@when(u'I call the read method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    context.returned_data = crud.read('test', f"Symbol = '{symbol}'")

@then(u'the data returned should be')
def step_impl(context):
    for row in context.table:
        row_dict = {key: value for key, value in row.as_dict().items()}
        
        # REFACTOR THIS
        row_dict['Price'] = float(row_dict['Price'])
        row_dict['MarketCap'] = int(row_dict['MarketCap'])
        row_dict['MagicformulaIndex'] = int(row_dict['MagicformulaIndex'])
        row_dict['AquirersMultiple'] = int(row_dict['AquirersMultiple'])

        print("RETURNED", context.returned_data)
        assert row_dict in context.returned_data


@when(u'I call the update method with the set_data and the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    set_data = {}
    for row in context.table:
        for header, value in row.as_dict().items():
            set_data[header] = value

    crud.update('test', set_data, f"Symbol = '{symbol}'")

@then(u'the data in the specified table should be updated')
def step_impl(context):
    updated_data = crud.read('test')
    row = context.active_outline
    row_dict = {key: value for key, value in row.as_dict().items()}
    
    # REFACTOR THIS
    row_dict['Price'] = float(row_dict['Price'])
    row_dict['MarketCap'] = int(row_dict['MarketCap'])
    row_dict['MagicformulaIndex'] = int(row_dict['MagicformulaIndex'])
    row_dict['AquirersMultiple'] = int(row_dict['AquirersMultiple'])
    assert any(row_dict.items() <= data_row.items() for data_row in updated_data)





@when(u'I call the delete method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    context.symbol = symbol
    crud.delete('test', f"Symbol = '{symbol}'")


@then(u'the data with the specified symbol should be deleted from the table')
def step_impl(context):
    deleted_data = crud.read('test')
    symbol = context.symbol
    for row in deleted_data:
        assert row['Symbol'] != symbol



@when(u'I call the drop_table method')
def step_impl(context):
    crud.drop_table('test')

@then(u'the specified table should be dropped from the database')
def step_impl(context):
    table_name = 'test'
    assert table_name not in crud.show_tables()
    crud.close()
