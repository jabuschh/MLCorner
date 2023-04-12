#!/usr/bin/env python

year = "UL17"
channel = "muon" # electron / muon

# path to the python code
path_MLDIR = "/nfs/dust/cms/user/jabuschh/uhh2-106X_v2/CMSSW_10_6_28/src/UHH2/MLCorner/InputsPreparation/UHH2toNumpy/"

# path to UHH2 output, used as input for convertion
fullsel_path = "/nfs/dust/cms/group/zprime-uhh/Analysis_" + year + "/" + channel + "/"

# path to store converted numpy files
outpath = "/nfs/dust/cms/user/jabuschh/uhh2-106X_v2/CMSSW_10_6_28/src/UHH2/MLCorner/output/" + year + "/" + channel + "/"
