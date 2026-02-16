import awkward as ak 
import numpy as np
import uproot
import pandas

def inv_m(file, p1, p2, flavor1 = 0, flavor2 = 0, df = False, graph = True):
    file = uproot.open(file)
    tree = file["Delphes"]
    flavor = tree["Jet/Jet.Flavor"].array(library = "ak")
    
    if p1 == "muon":
        pt1 = tree["Muon/Muon.PT"].array(library = "ak")
        eta1 = tree["Muon/Muon.Eta"].array(library = "ak")
        phi1 = tree["Muon/Muon.Phi"].array(library = "ak")
        charge1 = tree["Muon/Muon.Charge"].array(library = "ak")
        c1 = True
        
    elif p1 == "electron":
        pt1 = tree["Electron/Electron.PT"].array(library = "ak")
        eta1 = tree["Electron/Electron.Eta"].array(library = "ak")
        phi1 = tree["Electron/Electron.Phi"].array(library = "ak")
        charge1 = tree["Electron/Electron.Charge"].array(library = "ak")
        c1 = True
        
    elif p1 == "photon":
        pt1 = tree["Photon/Photon.PT"].array(library = "ak")
        eta1 = tree["Photon/Photon.Eta"].array(library = "ak")
        phi1 = tree["Photon/Photon.Phi"].array(library = "ak")
        c1 = False
        
    elif flavor1 != 0:
        pt1 = tree["Jet/Jet.PT"].array(library = "ak")
        eta1 = tree["Jet/Jet.Eta"].array(library = "ak")
        phi1 = tree["Jet/Jet.Phi"].array(library = "ak")
        charge1 = tree["Jet/Jet.Charge"].array(library = "ak")
        c1 = True
    
    if p2 == "muon":
        pt2 = tree["Muon/Muon.PT"].array(library = "ak")
        eta2 = tree["Muon/Muon.Eta"].array(library = "ak")
        phi2 = tree["Muon/Muon.Phi"].array(library = "ak")
        charge2 = tree["Muon/Muon.Charge"].array(library = "ak")
        c2 = True
        
    elif p2 == "electron":
        pt2 = tree["Electron/Electron.PT"].array(library = "ak")
        eta2 = tree["Electron/Electron.Eta"].array(library = "ak")
        phi2 = tree["Electron/Electron.Phi"].array(library = "ak")
        charge2 = tree["Electron/Electron.Charge"].array(library = "ak")
        c2 = True
        
    elif p2 == "photon":
        pt2 = tree["Photon/Photon.PT"].array(library = "ak")
        eta2 = tree["Photon/Photon.Eta"].array(library = "ak")
        phi2 = tree["Photon/Photon.Phi"].array(library = "ak")
        c2 = False
        
    elif flavor2 != 0:
        pt2 = tree["Jet/Jet.PT"].array(library = "ak")
        eta2 = tree["Jet/Jet.Eta"].array(library = "ak")
        phi2 = tree["Jet/Jet.Phi"].array(library = "ak")
        charge2 = tree["Jet/Jet.Charge"].array(library = "ak")
        c2 = True
        
    # The jet flavor is computed using the the Simple Δ𝑅
    # highest-flavor match and it is asigned as follows:
    #   gluon --> 21
    #   d --> 1
    #   u --> 2
    #   s --> 3
    #   c --> 4
    #   b --> 5
    
    if (c1 == True and c2 == True) and (flavor1 == 0 and flavor2 == 0):
        pt_1 = []
        eta_1 = []
        phi_1 = []
        cha_1 = []
        
        pt_2 = []
        eta_2 = []
        phi_2 = []
        cha_2 = []
        
        event_1 = []
        event_2 = []
        
        for i in range(len(pt1)):
           
        
    
    
    
    
        
        