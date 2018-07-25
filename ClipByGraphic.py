import arcpy
import datetime

out_dir = arcpy.GetParameterAsText(0) # Directory where output will go
arcpy.env.workspace = out_dir

execution_time = datetime.datetime.now()
version_string = execution_time.strftime('%Y%m%d_%H%M%S')
print(version_string)

mxd = arcpy.mapping.MapDocument("CURRENT")
activeDataFrame = mxd.activeDataFrame

dataFrames = arcpy.mapping.ListDataFrames(mxd)

selectedDataFrame = ""

for df in dataFrames:
    if activeDataFrame.name == df.name:
        selectedDataFrame = df
        print("The selected data frame is called {0}.".format(df.name))
        
