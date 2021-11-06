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
print(vddata)
vddata['Yposition'] *= -1
vddata['Yaw'] *= 180/math.pi
print(vddata)

# fig1, axs = plt.subplots(3, 1)
# plot_labels_vddata=[('Time, Xposition'), ('Time, Yposition'), ('Time, Yaw')]
# ax1.plot(vddata['Time'], vddata['Xposition'] / 100, 'b-', label='VD Output')
# ax1.plot(sumodata['timestep_time'], sumodata['vehicle_x'], 'r-', label='SUMO')
# ax2.plot(vddata['Time'], -vddata['Yposition'] / 100, 'b-', label='VD Output')
# ax2.plot(sumodata['timestep_time'], sumodata['vehicle_y'], 'r-', label='SUMO')
# ax2.set_xlabel('Time (s)')
# ax1.set_ylabel('X-Position (m)')
# ax2.set_ylabel('Y-Position (m)')
# plt.legend()
# plt.savefig(fname='X_and_Y_Pos_vs_Time.pdf')
#
# fig2, ax = plt.subplots()
# ax.plot(sumodata['vehicle_x'], sumodata['vehicle_y'], 'r-', label='SUMO')
# ax.plot(vddata['Xposition'] / 100, -vddata['Yposition'] / 100, 'b--', label='VD Output')
# ax.set_xlabel('X-Position (m)')
# ax.set_ylabel('Y-Position (m)')
#
# plt.legend()
# plt.savefig(fname='X_vs_Y_Pos.pdf')
# plt.show()
