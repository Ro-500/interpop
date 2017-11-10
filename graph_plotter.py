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
        from pandas import read_csv
        if not os.path.exists(files):
            print('ERROR! '+files+' not found.')
            return
        data = read_csv(files)
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

    def indir(inputdirectory="./", outdirectory="./"):
        from os import listdir
        import os.path
        directory = [f for f in listdir(inputdirectory) if os.path.isfile(os.path.join(inputdirectory, f))]
        print(directory)
        for files in directory:
            indir = inputdirectory+files
            title = files[:-4]
            outdir = outdirectory+files[:-4]+'.html'
            print(indir, title, outdir)
            print(os.path.exists(indir))
            plotter.plot(indir, title, outdir)
        print("Completed!!")

plotter.indir('./data/', './Graph/')
#plotter.plot('./data/Internet_Time_Use.csv', 'Internet_Time_Use', 'Internet_Time_Use.html')
#plotter.plot('./data/Use_Line.csv', 'Internet_Time_Use', 'Use_Line.html')
#plotter.plot('./data/use.csv', 'Internet_Time_Use', 'use.html')