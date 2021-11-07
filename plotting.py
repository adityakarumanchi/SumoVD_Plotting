from matplotlib import pyplot as plt
import pandas as pd
import os
import sys
import platform
import math

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)


def run_xml2csv(filepath):
    if platform.system() == 'Windows':
        os.system('cmd /c "py %s %s --separator ",""' % (os.path.join(tools, 'xml', 'xml2csv.py'), filepath))
    elif platform.system() == 'Linux':
        os.system("""python %s %s --separator "," """ % (os.path.join(tools, 'xml', 'xml2csv.py'), filepath))


def plotstuff(axis, dataset, xlabel, ylabel, style, legendlabel, axeslabels):#, bLegend, savename):
    axis.plot(dataset[xlabel], dataset[ylabel], style, label=legendlabel)
    if 'x' in axeslabels.keys():
        axis.set_xlabel(axeslabels['x'])
    elif 'y' in axeslabels.keys():
        axis.set_xlabel(axeslabels['y'])

    # if bLegend:
    #     plt.legend()
    #
    # if len(savename):
    #     plt.savefig(fname=savename)


SumoDataDir = r'/home/karumanchi.1/Downloads/Downtown/'
SumoDataXML = r'traci_single_veh_test_out.xml'
run_xml2csv(os.path.join(SumoDataDir, SumoDataXML))
VDDataDir = r'/home/karumanchi.1/Documents/UnrealProjects426/'

sumodata = pd.read_csv(os.path.join(SumoDataDir, SumoDataXML[:-4]+'.csv'), sep=',')
vddata = pd.read_csv(os.path.join(VDDataDir, 'VehicleDynamicsOut.csv'), sep='\s+|;', header=None)
vd_first_row = vddata.iloc[0]

col_names = [vd_first_row.iloc[idx] for idx in vddata.columns if idx % 2 == 0]
retained_cols = [idx for idx in vddata.columns if idx % 2 == 1]
vddata = vddata.loc[:, retained_cols]
vddata.columns = col_names
vddata['Xposition'] *= 0.01
vddata['Yposition'] *= -0.01
vddata['Yaw'] *= -180/math.pi

fig1, axs = plt.subplots(3, 1)
plot_labels_vddata= zip(axs, ['Time' for _ in range(len(axs))], ['Xposition', 'Yposition', 'Yaw'])
plot_labels_sumodata= zip(axs, ['timestep_time' for _ in range(len(axs))], ['vehicle_x', 'vehicle_y', 'vehicle_angle'])

idx = 0

for ax, sumox, sumoy in plot_labels_sumodata:
    plotstuff(ax, sumodata, sumox, sumoy, 'r-', 'SUMO', {})

for ax, vdx, vdy in plot_labels_vddata:
    plotstuff(ax, vddata, vdx, vdy, 'b-', 'Veh. Dyn.', {'x': 'Time (s)', 'y': vdx})

plt.legend(loc='upper right')
plt.savefig(fname='Time_vs_Output.pdf')

fig2, ax = plt.subplots()
plotstuff(ax, sumodata, 'vehicle_x', 'vehicle_y', style='r-', legendlabel='SUMO', axeslabels={'x': 'X-Position (m)', 'y': 'Y-Position (m)'})
plotstuff(ax, vddata, 'Xposition', 'Yposition', style='b-', legendlabel='Veh. Dyn.', axeslabels={})

plt.legend()
plt.savefig(fname='X_vs_Y_Pos.pdf')
# plt.show()
