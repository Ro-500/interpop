''' Universal Graph Plotter
    Python and Pygal
    Using for InterPop Project
        __  __   ___    __   ___ __    __ __    __
       / / / /  /   |  / /  /  / \ \  / / \ \  / /
      / / / /  / /| | / /  /  /   \ \/ /   \ \/ /
     / /_/ /  / / | |/ /  /  /    / /\ \   / /\ \
    /_____/  /_/  |___/  /__/    /_/  \_\ /_/  \_\
        _____  ______  _______  ___    __  ___ ___
       / ___/ / __  / / _____/ /   |  / / /  //  /
      / /    / / / / / /      / /| | / / /  //  /
     / /__  / /_/ / / /      / / | |/ / /__//__/
    /____/ /_____/ /_/      /_/  |___/ /__//__/

'''
import pygal
class plotter():
    ''' Call Plotter '''
    def plot(files="data.csv", title="", output='Graph.html'):
        ''' Get Graph title, CSV file path, Output path
            and render out file to 'Graph.html' or 'Output'
        '''
        print(files)
        import os.path
        import chardet
        from pandas import read_csv
        if not os.path.exists(files):
            print('ERROR! '+files+' not found.')
            return
        with open(files, 'rb') as filee:
            result = chardet.detect(filee.read())
        data = read_csv(files, encoding=result['encoding'])
        #print(data.columns.values[1:])
        line_chart = pygal.Line()
        line_chart.title = title
        line_chart.x_labels = map(str, data[data.columns.values[0]])
        count = 0
        for select in data.columns.values[1:]:
            print(data[select])
            _ = [line_chart.add(select, data[select])]
            count = count+1
        line_chart.render_to_file(output)
        print("Completed!!")

    def indir(inputdirectory="./", outdirectory="./"):
        from os import listdir
        import os.path
        directory = [f for f in listdir(inputdirectory) if os.path.isfile(os.path.join(inputdirectory, f))]
        for files in directory:
            indir = inputdirectory+files
            title = files[:-4]
            outdir = outdirectory+files[:-4]+'.html'
            plotter.plot(indir, title, outdir)
        print("Completed!!")

    def xlsxtocsv(dirin='./', dirout='./'):
        """ Covert Excel file in dir in to CSV in dir out """
        import pandas as pd
        import os
        directory = [f for f in os.listdir(dirin) if '.xlsx' in f]
        for files in directory:
            print('Coverting '+files+'\nto file   '+files[:-5]+'.csv'+'\ndirectory '+dirin+' -> '+dirout)
            data_xls = pd.read_excel(dirin+files, index_col=None)
            data_xls.to_csv(dirout+files[:-5]+'.csv', index=False)
plotter.xlsxtocsv('./data/xlsx/', './data/')
plotter.indir('./data/', './Graph/')