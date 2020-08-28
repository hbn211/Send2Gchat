# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.2.0
# 16:21:42  ago 27, 2020
# ----------------------------------------------
import ScriptEnv
# import os

import sys
sys.path.append(r'C:/Send2Gchat')
import IronDrive

IronDrive.status('Starting simulation...')

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("PB-SAOA-BLE-11")
oDesign = oProject.SetActiveDesign("main_cutout_Circuibras:U1")
oDesign.AnalyzeAllNominal()

IronDrive.status('DONE')
