import os
import mysql.connector

class CRUD:
    def __init__(self):
        env_dict = self._load_env()
        self.connection = self._get_connection(env_dict)
        self.cursor = self.connection.cursor()

    def _load_env(self):
        env_vars = ['MYSQL_DATABASE', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_HOST']
        env_dict = {var: os.getenv(var) for var in env_vars}
        return env_dict

    def _get_connection(self, env_dict):
        connection = mysql.connector.connect(
            host=env_dict['MYSQL_HOST'],
            user=env_dict['MYSQL_USER'],
            password=env_dict['MYSQL_PASSWORD'],
            database=env_dict['MYSQL_DATABASE']
        )
        return connection

    def insert(self, table, data_dict):
        query = self._build_insert_query(table, data_dict)
        rows_data = self._get_rows_data(data_dict)

        self._execute_insert_query_for_rows(self.cursor, query, rows_data)
        self.connection.commit()

    def _build_insert_query(self, table, data_dict):
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['%s'] * len(data_dict))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return query

    def _get_rows_data(self, data_dict):
        num_rows = len(data_dict[next(iter(data_dict))])
        rows_data = [
            tuple(col_values[i] for col_values in data_dict.values())
            for i in range(num_rows)
        ]
        return rows_data

    def _execute_insert_query_for_rows(self, cursor, query, rows_data):
        print('CAVEMAN\n',rows_data)
        for row_data in rows_data:
            cursor.execute(query, row_data)

    def create_table(self, table, schema):
        columns_schema = ', '.join([f'`{col_name}` {col_type}' for col_name, col_type in schema.items()])  # Add backticks around column names
        query = f"CREATE TABLE IF NOT EXISTS {table} ({columns_schema})"
        self.cursor.execute(query)
        self.connection.commit()

    def create(self, table, data_dict):
        schema = self._infer_mysql_data_types(data_dict)
        self.create_table(table, schema)
        self.insert(table, data_dict)

    def _infer_mysql_data_types(self, data_dict):
        schema = {col: self._infer_data_type(data[0]) for col, data in data_dict.items()}
        return schema

    def _infer_data_type(self, value):
        if isinstance(value, int):
            return 'BIGINT' if value > 2147483647 else 'INT'
        if isinstance(value, float):
            return 'DOUBLE'
        if isinstance(value, str):
            return 'VARCHAR(90)'
        raise ValueError(f'Unsupported data type: {type(value)}')

    def read(self, table, condition=None):
        # Implement read method logic here
        pass

    def update(self, table, set_data, condition=None):
        # Implement update method logic here
        pass

    def delete(self, table, condition=None):
        # Implement delete method logic here
        pass

    def close(self):
        self.cursor.close()
        self.connection.close()

    def drop_table(self, table):
        query = f"DROP TABLE IF EXISTS {table}"
        self.cursor.execute(query)
        self.connection.commit()
