import numpy as np
import pandas as pd
import json

# from library.dbengine import DBEngine


path = '/Users/prashantraj/Documents/Natural_Language_To_SQL_CE901_Project_Dissertation/WikiSQL_DataSet'


def build_table_mapping(dataset):
    """Reads the tables file and creates a dictionary with table id as key and all other data as value"""
    print(dataset)
    tables = pd.read_json("WikiSQL_DataSet/" + dataset + ".tables.jsonl", lines=True)
    print(tables)
    data = pd.DataFrame()
    print(data)
    return data


def load_dataset(dataset_to_load):
    """Load the given dataset into memory."""
    print("Loading dataset : ", dataset_to_load)
    sql_data_path = 'WikiSQL_DataSet/' + dataset_to_load + '.jsonl'
    table_data_path = 'WikiSQL_DataSet/' + dataset_to_load + '.tables.jsonl'
    db_file = 'WikiSQL_DataSet/' + dataset_to_load + '.db'
    print(sql_data_path)

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
     sql_data, table_data, TRAIN_DB = load_dataset('train')
     print(table_data)
