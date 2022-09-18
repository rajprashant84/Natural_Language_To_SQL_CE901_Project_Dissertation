from numpy.core import records
import re
from babel.numbers import parse_number, parse_decimal, format_number, NumberFormatError

Schema = re.compile(r'\((.+)\)')
number = re.compile(r'[-+]?\d*\.\d+|\d+')

Agg_Command = ['SUM', 'MIN', 'MAX', 'COUNT', 'AVG', '']
Conditional_Command = ['<', '>', '=', 'OP']


class SQL_Connection:
    def __init__(self, database):
        self.database = records.Database('sqlite:///{}'.format(database))
        self.con = self.db.get_connection()

    def query_execute(self, table_ID, query, *args, **kwargs):
        return self.execute(table_ID, query.select_index, query.agg_index, query.conditions, *args, **kwargs)

    def execute(self, table_ID, select_index, aggregation_index, conditions, lower=True):
        if not table_ID.startswith('table'):
            table_ID = 'table_{}'.format(table_ID.replace('-', '_'))
        table_info = self.conn.query('SELECT sql from sqlite_master WHERE tbl_name = :name', name=table_ID).all()[
            0].sql.replace('\n', '')
        schema_str = Schema.findall(table_info)[0]
        schema = {}
        for tup in schema_str.split(', '):
            c, t = tup.split()
            schema[c] = t
        select = 'col{}'.format(select_index)
        agg = Agg_Command[aggregation_index]
        if agg:
            select = '{}({})'.format(agg, select)
        where_clause = []
        where_map = {}
        for col_index, op, val in conditions:
            if lower and (isinstance(val, str) or isinstance(val, bytes)):
                val = val.lower()
            if schema['col{}'.format(col_index)] == 'real' and not isinstance(val, (int, float)):
                try:
                    val = float(parse_decimal(val, locale='en_US'))
                except NumberFormatError as e:
                    val = float(number.findall(val)[0])
            where_clause.append('col{} {} :col{}'.format(col_index, Conditional_Command[op], col_index))
            where_map['col{}'.format(col_index)] = val
        where_str = ''
        if where_clause:
            where_str = 'WHERE ' + ' AND '.join(where_clause)
        query = 'SELECT {} AS result FROM {} {}'.format(select, table_ID, where_str)
        out = self.conn.query(query, **where_map)
        return [o.result for o in out]
