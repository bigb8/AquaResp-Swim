##### PYTHON LIBRARIES ###############

import os,sys

##### EXTERNAL LIBRARIES ###############

import numpy as np

from bokeh.plotting import figure, output_file, show,save
from bokeh.models import BoxSelectTool,ResetTool,WheelZoomTool,HoverTool,CrosshairTool
from bokeh.core.properties import value
from bokeh.io import show, output_file

########### AQUARESP LIBRARIES ###############

import filehandling

########### INIT ###############
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
oxygenpath = mainpath + os.sep +"oxygen" + os.sep
temppath = mainpath + os.sep +"temp" + os.sep
fn = oxygenpath + "firesting.txt"
lib_p = mainpath  + os.sep + "lib" + os.sep
myp = os.path.dirname(sys.argv[0]) + os.sep


############### MO2 vs TIME #######################



mo2_ms_s,mo2s,r2s,po2s,Ubls,Ucs,hours = filehandling.getdataswim() # retrieve data

 
#Mo2 vs time plot
x = np.array(hours)
y = np.array(mo2_ms_s)

color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]

# output to static HTML file
output_file(myp + "MO2_1.html",mode="inline")

# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Mass-Specific ", x_axis_label='Time [h]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(0, np.array(y).max() +20))
p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
p.circle(x, y, legend="Respirometer 1", size =7,fill_color=color[0], fill_alpha=0.6,line_color=(0,0,0))
p.line(x, y, alpha=0.6,line_color=(0,0,0))
# show the results
save(p)
print("MO2 Plot updated")



x = np.array(Ubls)
y = np.array(mo2_ms_s)
color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
# output to static HTML file
output_file(myp + "MO2_UBLS.html",mode="inline")
# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Swim speed  ", x_axis_label='U [BL/s]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +.5), y_range=(0, np.array(y).max()))
p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
p.circle(x, y, legend="Respirometer 1", size =7,fill_color=color[0], fill_alpha=0.6,line_color=(0,0,0))


# p.line(x, y, alpha=0.6,line_color=(0,0,0))
# show the results
save(p)
print("MO2 vs UBLS Plot updated")

x = np.array(Ucs)
y = np.array(mo2_ms_s)
color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
# output to static HTML file
output_file(myp + "MO2_U.html",mode="inline")
# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Swim speed  ", x_axis_label='U [cm/s]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +.5), y_range=(0, np.array(y).max()))
p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
p.circle(x, y, legend="Respirometer 1", size =7,fill_color=color[0], fill_alpha=0.6,line_color=(0,0,0))


# p.line(x, y, alpha=0.6,line_color=(0,0,0))
# show the results
save(p)
print("MO2 vs U Plot updated")



x = np.array(po2s)
y = np.array(mo2_ms_s)
color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
# output to static HTML file
output_file(myp + "MO2_PO2.html",mode="inline")
# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: O2 water ", x_axis_label='% air sat', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +.5), y_range=(0, np.array(y).max()))
p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
p.circle(x, y, legend="Respirometer 1", size =7,fill_color=color[0], fill_alpha=0.6,line_color=(0,0,0))

# p.line(x, y, alpha=0.6,line_color=(0,0,0))
# show the results
save(p)
print("MO2 vs PO2 updated")


x = np.array(hours)
y = np.array(r2s)
color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
# output to static HTML file
output_file(myp + "R2.html",mode="inline")
# create a new plot with a title and axis labels
p = figure(title="R-squared", x_axis_label='Hours', y_axis_label='R*R',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +.5), y_range=(0, 1.1))
p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
p.circle(x, y, legend="Respirometer 1", size =7,fill_color=color[0], fill_alpha=0.6,line_color=(0,0,0))

p.line(x, y, alpha=0.6,line_color=(0,0,0))
# show the results
save(p)
print("R2 updated")
