import numpy as np
import pandas as pd
import uproot

def inv_m(file, p1, p2, charge = 0, flavor1 = 0, flavor2 = 0, df = False, graph = True):
    file = uproot.open(file)
    tree = file["Delphes"]
    
    if flavor1 != 0 or flavor2 != 0:
        flavor = tree["Jet/Jet.Flavor"].array(library = "np")
    
    if p1 != p2:
        if p1 == "muon":
            pt1 = tree["Muon/Muon.PT"].array(library = "np")
            eta1 = tree["Muon/Muon.Eta"].array(library = "np")
            phi1 = tree["Muon/Muon.Phi"].array(library = "np")
            charge1 = tree["Muon/Muon.Charge"].array(library = "np")
            c1 = True
            
        elif p1 == "electron":
            pt1 = tree["Electron/Electron.PT"].array(library = "np")
            eta1 = tree["Electron/Electron.Eta"].array(library = "np")
            phi1 = tree["Electron/Electron.Phi"].array(library = "np")
            charge1 = tree["Electron/Electron.Charge"].array(library = "np")
            c1 = True
            
        elif p1 == "photon":
            pt1 = tree["Photon/Photon.PT"].array(library = "np")
            eta1 = tree["Photon/Photon.Eta"].array(library = "np")
            phi1 = tree["Photon/Photon.Phi"].array(library = "np")
            c1 = False
            
        elif flavor1 != 0:
            pt1 = tree["Jet/Jet.PT"].array(library = "np")
            eta1 = tree["Jet/Jet.Eta"].array(library = "np")
            phi1 = tree["Jet/Jet.Phi"].array(library = "np")
            charge1 = tree["Jet/Jet.Charge"].array(library = "np")
            c1 = True
        
        if p2 == "muon":
            pt2 = tree["Muon/Muon.PT"].array(library = "np")
            eta2 = tree["Muon/Muon.Eta"].array(library = "np")
            phi2 = tree["Muon/Muon.Phi"].array(library = "np")
            charge2 = tree["Muon/Muon.Charge"].array(library = "np")
            c2 = True
            
        elif p2 == "electron":
            pt2 = tree["Electron/Electron.PT"].array(library = "np")
            eta2 = tree["Electron/Electron.Eta"].array(library = "np")
            phi2 = tree["Electron/Electron.Phi"].array(library = "np")
            charge2 = tree["Electron/Electron.Charge"].array(library = "np")
            c2 = True
            
        elif p2 == "photon":
            pt2 = tree["Photon/Photon.PT"].array(library = "np")
            eta2 = tree["Photon/Photon.Eta"].array(library = "np")
            phi2 = tree["Photon/Photon.Phi"].array(library = "np")
            c2 = False
            
        elif flavor2 != 0:
            pt2 = tree["Jet/Jet.PT"].array(library = "np")
            eta2 = tree["Jet/Jet.Eta"].array(library = "np")
            phi2 = tree["Jet/Jet.Phi"].array(library = "np")
            charge2 = tree["Jet/Jet.Charge"].array(library = "np")
            c2 = True
    else:
        if p1 == "muon":
            pt1 = tree["Muon/Muon.PT"].array(library = "np")
            eta1 = tree["Muon/Muon.Eta"].array(library = "np")
            phi1 = tree["Muon/Muon.Phi"].array(library = "np")
            charge1 = tree["Muon/Muon.Charge"].array(library = "np")
            c1 = True
            
        elif p1 == "electron":
            pt1 = tree["Electron/Electron.PT"].array(library = "np")
            eta1 = tree["Electron/Electron.Eta"].array(library = "np")
            phi1 = tree["Electron/Electron.Phi"].array(library = "np")
            charge1 = tree["Electron/Electron.Charge"].array(library = "np")
            c1 = True
            
        elif p1 == "photon":
            pt1 = tree["Photon/Photon.PT"].array(library = "np")
            eta1 = tree["Photon/Photon.Eta"].array(library = "np")
            phi1 = tree["Photon/Photon.Phi"].array(library = "np")
            c1 = False
            
        elif flavor1 != 0:
            pt1 = tree["Jet/Jet.PT"].array(library = "np")
            eta1 = tree["Jet/Jet.Eta"].array(library = "np")
            phi1 = tree["Jet/Jet.Phi"].array(library = "np")
            charge1 = tree["Jet/Jet.Charge"].array(library = "np")
            c1 = True
        
    # The jet flavor is computed using the the Simple Δ𝑅
    # highest-flavor match and it is asigned as follows:
    #   gluon --> 21
    #   d --> 1
    #   u --> 2
    #   s --> 3
    #   c --> 4
    #   b --> 5
    
    # For different particles that aren't photons:
 
    