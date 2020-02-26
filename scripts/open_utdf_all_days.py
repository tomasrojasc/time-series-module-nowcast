import pandas as pd

file1 = pd.read_csv('files_to_process/file1.csv')
file2 = pd.read_csv('files_to_process/file2.csv')
UTdf = pd.merge(file1, file2, how='outer', left_index=True, right_index=True, on='datetime', suffixes=('_file1', '_file2'))
UTdf.set_index('datetime', inplace=True, drop=True)
UTdf.index = pd.to_datetime(UTdf.index)
print(UTdf.columns)