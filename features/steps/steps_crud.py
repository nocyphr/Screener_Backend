@given(u'the database contains the following test-table data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the database contains the following test-table data')


@given(u'an existing table "{table_name}"')
def step_impl(context, table_name):
    raise NotImplementedError(u'STEP: Given an existing table "{}"'.format(table_name))


@when(u'I call the insert method with the data')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I call the insert method with the data')


@then(u'the data should be inserted into the specified table')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the data should be inserted into the specified table')


@when(u'I call the read method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    raise NotImplementedError(u'STEP: When I call the read method with the condition "Symbol = \'{}\'"'.format(symbol))


@then(u'the data returned should be')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the data returned should be')


@when(u'I call the update method with the set_data and the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    raise NotImplementedError(u'STEP: When I call the update method with the set_data and the condition "Symbol = \'{}\'"'.format(symbol))


@then(u'the data in the specified table should be updated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the data in the specified table should be updated')


@when(u'I call the delete method with the condition "Symbol = \'{symbol}\'"')
def step_impl(context, symbol):
    raise NotImplementedError(u'STEP: When I call the delete method with the condition "Symbol = \'{}\'"'.format(symbol))


@then(u'the data with the specified symbol should be deleted from the table')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the data with the specified symbol should be deleted from the table')


@when(u'I call the drop_table method')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I call the drop_table method')


@then(u'the specified table should be dropped from the database')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the specified table should be dropped from the database')
