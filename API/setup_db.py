#!/usr/bin/python3
# Extract

import pandas as pd

subject_df = pd.read_csv('./resources/subject', sep=',')
colors_df = pd.read_csv('./resources/colors', sep=',')
dates_df = pd.read_csv('./resources/modified_dates', sep=',', header=None, names=['title', 'date'], usecols=[0, 1])

subject_df.drop(list(subject_df.filter(regex = 'FRAME')), axis = 1, inplace = True)
subject_df.columns = subject_df.columns.str.replace('_', ' ')
subject_df.columns = subject_df.columns.str.lower()

def get_subjects(row):
	cols = []
	for col in row.index:
		if row[col] == 1:
			cols.append(col)
	return cols

subject_df['subject_list'] = subject_df.apply(lambda row: get_subjects(row), axis=1)
subject_df['subject_list'] = subject_df['subject_list'].apply(lambda x: ', '.join(x))
subject_df = subject_df.drop(subject_df.columns.difference(['subject_list']), axis=1)
subject_df['id'] = range(0, len(subject_df))


colors_df.drop('Unnamed: 0', axis=1, inplace=True)
colors_df.drop('episode', axis=1, inplace=True)

colors_df['id'] = range(0, len(colors_df))

colors_df.columns = colors_df.columns.str.lower()


merged_df = pd.merge(subject_df, colors_df, on='id')
# sort columns alphabetically
merged_df = merged_df.reindex(sorted(merged_df.columns), axis=1)
# print(merged_df.columns)


dates_df.columns = dates_df.columns.str.lower()
# print(dates_df.columns)
dates_df['id'] = range(0, len(dates_df))
final_df = pd.merge(merged_df, dates_df, on='id')
final_df.columns = final_df.columns.str.replace(' ', '_')
final_df = final_df.reindex(sorted(final_df.columns), axis=1)


# Send dataframe to sqlite database
import sqlite3
conn = sqlite3.connect('episodes.db')
final_df.to_sql('episodes', conn, if_exists='replace', index = False)
conn.close()

