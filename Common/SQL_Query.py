import re
from tabulate import tabulate
from common_utility import remove_token
from copy import deepcopy
from collections import defaultdict

re_whitespace = re.compile(r'\s+', flags=re.UNICODE)
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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            indices = self.select_index == other.select_index and self.agg_index == other.agg_inde
            if other.ordered:
                conds = [(col, op, str(cond).lower()) for col, op, cond in self.conditions] == [
                    (col, op, str(cond).lower()) for col, op, cond in other.conditions]
            else:
                conds = set([(col, op, str(cond).lower()) for col, op, cond in self.conditions]) == set(
                    [(col, op, str(cond).lower()) for col, op, cond in other.conditions])

            return indices and conds
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        rep = 'SELECT {agg} {sel} FROM table'.format(agg=self.agg_ops[self.agg_index],sel='col{}'.format(self.select_index),)
        if self.conditions:
            rep += ' WHERE ' + ' AND '.join(
                ['{} {} {}'.format('col{}'.format(i), self.cond_ops[o], v) for i, o, v in self.conditions])
        return rep

