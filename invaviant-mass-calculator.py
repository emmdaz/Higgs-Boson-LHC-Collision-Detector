import numpy as np
import uproot
import pandas

def inv_m(file, p1, p2, flavor1 = 0, flavor2 = 0, df = False, graph = True):
    file = uproot.open(file)
    tree = file["Delphes"]
    flavor = tree["Jet/Jet.Flavor"].array(library = "np")
    
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
        
    # The jet flavor is computed using the the Simple Δ𝑅
    # highest-flavor match and it is asigned as follows:
    #   gluon --> 21
    #   d --> 1
    #   u --> 2
    #   s --> 3
    #   c --> 4
    #   b --> 5
    
    if (c1 == True and c2 == True) and (flavor1 == 0 and flavor2 == 0):
        events = len(pt1)
        
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
        
        if p1 != p2:
            for i in range(events):
                if len(pt1) > 0 and len(pt2) > 0: 
                    index1 = np.argmax(pt1[i])
                    index2 = np.argmax(pt2[i])
                    
                    pt_1.append(pt1[i,index1])
                    eta_1.append(eta1[i,index1])
                    phi_1.append(phi1[i,index1])
                    cha_1.append(charge1[i,index1])
                    
                    pt_2.append(pt2[i,index2])
                    eta_2.append(eta2[i,index2])
                    phi_2.append(phi2[i,index2])
                    cha_2.append(charge2[i,index2])
                    
        
        
                
           
        
    
    