#!/usr/bin/python3
import csv
import re

table_name = ''
headers = []
data = []


def write_csv(table_name):
  # write_csv
    with open(f'{table_name}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)


with open('*******sql_file_path*********.sql', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        if line.startswith('CREATE TABLE'):
            write_csv(table_name)
            headers = []
            data = []
            # table_name
            table_name = re.search(r'`(.*?)`', line).group(1)
        elif line.startswith('INSERT INTO'):
            # headers
            headers = re.findall(r'`(.*?)`', line)
            # data
            values = re.search(r'\((.*)\)', line).group(1)
            row = values.split(',')
            data.append(row)
    write_csv(table_name)
