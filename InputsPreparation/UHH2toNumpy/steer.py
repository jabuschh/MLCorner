#!/usr/bin/env python

import subprocess
import os
import time

from python.ModuleRunner import *
from python.constants import *


"""This is a macro to steer the Root to Numpy conversion. """


# paths are set in constants.py
ModuleRunner = ModuleRunner(path_MLDIR, outpath)

# ---- Macro for ML inputs preparation ----
# names of the process, e.g part after uhh2.AnalysisModuleRunner. in the input file name
procnames = ['TTbar', 'ST', 'WJets', 'DY'] # 'Diboson', 'QCD' # no signal to stay model-independent
# name of branches to be skipped in conversion
## exact names
unwanted_exact_tags = ['Mttbar', 'NPV', 'event', 'isRealData', 'luminosityBlock', 'met_pt', 'passEcalBadCalib','rho', 'run', 'GenParticles', 'offlineSlimmedPrimaryVertices', 'year', 'rec_chi2', 'M_tt', 'CHS_matched.tags.tagdata', 'chi2']
## partial names to exclude common set of variables at once
unwanted_tags = ['ak4jet1_', 'ak8jet1_', 'beamspot_', 'weight_pu', 'prefiringWeight', 'trigger', 'gen', 'jets', 'slimmed', 'm_', 'offlineSlimmedPrimaryVertices_', 'GenParticles_', 'lep1_', 'weight', 'hotvr', 'TopTagSF', 'muonrecSF_', 'CHS_matched_', 'Ak4_j6_', 'deepak8tscore', 'Ele'] # Ele / Mu

syst_vars = ['NOMINAL']
for syst_var in syst_vars:
    print'--- Convert inputs for ',syst_var,' variation ---'
    ModuleRunner.ReadoutMLVariables(procnames=procnames, unwanted_tags=unwanted_tags, unwanted_exact_tags=unwanted_exact_tags, syst_var=syst_var)
