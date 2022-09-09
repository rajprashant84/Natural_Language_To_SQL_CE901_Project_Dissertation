
from __future__ import division, print_function, unicode_literals
import pandas as pd
import nltk
import records
from Common.SQL_Query import SQL_Query
from Common.table import table



class SQL_To_Text_Convertor:
    def __init__(self):
        self.table_map = {}  # key is table_id, value is all the table data