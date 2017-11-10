import pandas as pd
from os import listdir
import os.path
directory = [f for f in listdir('./') if '.xlsx' in f]
print(directory)
for files in directory:
    data_xls = pd.read_excel(files, index_col=None)
    data_xls.to_csv('../'+files[:-5]+'.csv', index=False)
