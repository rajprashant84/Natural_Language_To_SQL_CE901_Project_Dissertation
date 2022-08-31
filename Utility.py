import numpy as np
import pandas as pd
import json
#from library.dbengine import DBEngine



def load_dataset(dataset_to_load):
    """Load the given dataset into memory."""
    print("Loading dataset : ", dataset_to_load)
    sql_data_path = 'data/tokenized_' + dataset_to_load + '.jsonl'
    table_data_path = 'data/tokenized_' + dataset_to_load + '.tables.jsonl'
    db_file = 'data/' + dataset_to_load + '.db'

    sql_data = []
    table_data = {}
    with open(sql_data_path, encoding="utf-8") as lines:
        for line in lines:
            sql = json.loads(line.strip())
            sql_data.append(sql)

    # Build a mapping of the tables with table_id as the key
    with open(table_data_path, encoding="utf-8") as lines:
        for line in lines:
            tab = json.loads(line.strip())
            table_data[tab[u'id']] = tab

    return sql_data, table_data, db_file


if __name__ == '__main__':
  load_dataset('dataset_to_load')