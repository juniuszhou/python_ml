import os
import pandas as pd
import time


def read_old():
    old_frame = pd.read_csv("offset.txt", '\t')
    if old_frame.columns.size > 4:
        old_frame = old_frame.drop(old_frame.columns[2], 1)
    old_frame.index = old_frame['table'] + old_frame['partition'].astype(str)
    return old_frame


def run_today(latest_time):

    today_frame = pd.DataFrame(columns=['table', 'partition', latest_time])
    for topic in []:

        print(offset)
        for line in offset.split('\n'):
            print(line)
            items = line.split(':')
            table_name = items[0]
            partition = str(items[1])
            offset = items[2]
            today_frame.ix[table_name + partition, 'table'] = table_name
            today_frame.ix[table_name + partition, 'partition'] = items[1]
            today_frame.ix[table_name + partition, latest_time] = offset
    return today_frame











