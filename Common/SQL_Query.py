import re
from tabulate import tabulate
from common_utility import remove_token
from copy import deepcopy
from collections import defaultdict


class SQL_Query:
    Agg_Command = ['SUM', 'MIN', 'MAX', 'COUNT', 'AVG', '']
    Conditional_Command = ['<', '>', '=', ]
    Syntax = ['SELECT', 'WHERE', 'AND', 'OR', 'COL', 'TABLE', 'CAPTION', 'PAGE', 'SECTION', 'OP', 'COND', 'QUESTION'
        , 'AGG', 'AGGOPS', 'CONDOPS']

    def __init__(self, select_index, agg_index, conditions=tuple(), ordered=False):
        self.select_index = select_index
        self.agg_index = agg_index
        self.conditions = list(conditions)
        self.ordered = ordered
