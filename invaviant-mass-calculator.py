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
            pt = tree["Muon/Muon.PT"].array(library = "np")
            eta = tree["Muon/Muon.Eta"].array(library = "np")
            phi = tree["Muon/Muon.Phi"].array(library = "np")
            charge = tree["Muon/Muon.Charge"].array(library = "np")
            c = True
            
        elif p1 == "electron":
            pt = tree["Electron/Electron.PT"].array(library = "np")
            eta = tree["Electron/Electron.Eta"].array(library = "np")
            phi = tree["Electron/Electron.Phi"].array(library = "np")
            charge = tree["Electron/Electron.Charge"].array(library = "np")
            c = True
            
        elif p1 == "photon":
            pt = tree["Photon/Photon.PT"].array(library = "np")
            eta = tree["Photon/Photon.Eta"].array(library = "np")
            phi = tree["Photon/Photon.Phi"].array(library = "np")
            c = False
            
        elif flavor1 != 0:
            pt = tree["Jet/Jet.PT"].array(library = "np")
            eta = tree["Jet/Jet.Eta"].array(library = "np")
            phi = tree["Jet/Jet.Phi"].array(library = "np")
            charge = tree["Jet/Jet.Charge"].array(library = "np")
            c = True
        
    # The jet flavor is computed using the the Simple Δ𝑅
    # highest-flavor match and it is asigned as follows:
    #   gluon --> 21
    #   d --> 1
    #   u --> 2
    #   s --> 3
    #   c --> 4
    #   b --> 5
    
    # For different particles that aren't photons:
    if p1 != p2 and (c1 == True and c2 == True):
        
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

        # Both kind of particles aren't jets
        if flavor1 == 0 and flavor2 == 0:
            
            for i in range(events):
                if len(pt1[i]) > 0 and len(pt2[i]) > 0: # At least one of each
                    index1 = np.argmax(pt1[i])
                    index2 = np.argmax(pt2[i])
                    
                    if charge1[i,index1] + charge2[i,index2] == charge:
                        
                        pt_1.append(pt1[i,index1])
                        eta_1.append(eta1[i,index1])
                        phi_1.append(phi1[i,index1])
                        cha_1.append(charge1[i,index1])
                            
                        pt_2.append(pt2[i,index2])
                        eta_2.append(eta2[i,index2])
                        phi_2.append(phi2[i,index2])
                        cha_2.append(charge2[i,index2])
                            
                        event_1.append(i)
                        event_2.append(i)
            
        # For collisions with decayment particles being jets
        elif flavor1 != 0 or flavor2 !=0:
            
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

            # For both particles being jets:
            if flavor1 != 0 and flavor2 != 0:
                for i in range(events):
                    suma_1 = np.sum(flavor[i] == flavor1)
                    suma_2 = np.sum(flavor[i] == flavor2)

                    if suma_1 > 0 and suma_2 > 0:
                        index1 = np.argmax(pt1[i])
                        index2 = np.argmax(pt2[i])

                        if charge1[i,index1] + charge2[i,index2] == charge:
                            pt_1.append(pt1[i,index1])
                            eta_1.append(eta1[i,index1])
                            phi_1.append(phi1[i,index1])
                            cha_1.append(charge1[i,index1])
                                
                            pt_2.append(pt2[i,index2])
                            eta_2.append(eta2[i,index2])
                            phi_2.append(phi2[i,index2])
                            cha_2.append(charge2[i,index2])
                                
                            event_1.append(i)
                            event_2.append(i)             

            # For just the first particle being a jet:
            elif flavor1 != 0 and flavor2 == 0:
                for i in range(events):
                    suma_1 = np.sum(flavor[i] == flavor1)

                    if suma_1 > 0 and len(pt2[i]) > 0:
                        index1 = np.argmax(pt1[i])
                        index2 = np.argmax(pt2[i])

                        if charge1[i,index1] + charge2[i,index2] == charge:
                            pt_1.append(pt1[i,index1])
                            eta_1.append(eta1[i,index1])
                            phi_1.append(phi1[i,index1])
                            cha_1.append(charge1[i,index1])
                                
                            pt_2.append(pt2[i,index2])
                            eta_2.append(eta2[i,index2])
                            phi_2.append(phi2[i,index2])
                            cha_2.append(charge2[i,index2])
                                
                            event_1.append(i)
                            event_2.append(i)

            # For just the 2nd particle being a jet: 
            elif flavor1 == 0 and flavor2 != 0:
                for i in range(events):
                    suma_2 = np.sum(flavor[i] == flavor2)

                    if suma_2 > 0 and len(pt1[i]) > 0:
                        index1 = np.argmax(pt1[i])
                        index2 = np.argmax(pt2[i])

                        if charge1[i,index1] + charge2[i,index2] == charge:
                            pt_1.append(pt1[i,index1])
                            eta_1.append(eta1[i,index1])
                            phi_1.append(phi1[i,index1])
                            cha_1.append(charge1[i,index1])
                                
                            pt_2.append(pt2[i,index2])
                            eta_2.append(eta2[i,index2])
                            phi_2.append(phi2[i,index2])
                            cha_2.append(charge2[i,index2])
                                
                            event_1.append(i)
                            event_2.append(i)
             
        pt_1 = np.array(pt_1)
        eta_1 = np.array(eta_1)
        phi_1 = np.array(phi_1)
        cha_1 = np.array(cha_1)
            
        pt_2 = np.array(pt_2)
        eta_2 = np.array(eta_2)
        phi_2 = np.array(phi_2)
        cha_2 = np.array(cha_2)
             
        event_1 = np.array(event_1)
        event_2 = np.array(event_2)
        
        if df == True:
            data = {
                    "pt_1": pt_1,
                    "pt_2": pt_2,
                    "eta_1": eta_1,
                    "eta_2": eta_2,
                    "phi_1": phi_1,
                    "phi_2": phi_2,
                    "charge_1": cha_1,
                    "charge_2": cha_2
                    }
                
            data = pd.DataFrame(data)
            
    # For different particles with one kind of them are photons
    elif p1 != p2 and (c1 == False or c2 == False):
        
        events = len(pt1)
        
        pt_1 = []
        eta_1 = []
        phi_1 = []
        
        pt_2 = []
        eta_2 = []
        phi_2 = []
        
        event_1 = []
        event_2 = []

        charge_12 = []

        # When none of them are jets so ones are photons and the others
        # are some other kind
        if flavor1 == 0 and flavor2 == 0:
        
            for i in range(events):
                if len(pt1) > 0 and len(pt2) > 0:

                    index1 = np.argmax(pt1[i])
                    index2 = np.argmax(pt2[i])

                    if c1 == True and charge1[i,index1] == charge:
                        charge_12.append(charge1[i,index1])

                        pt_1.append(pt1[i,index1])
                        eta_1.append(eta1[i,index1])
                        phi_1.append(phi1[i,index1])
                            
                        pt_2.append(pt2[i,index2])
                        eta_2.append(eta2[i,index2])
                        phi_2.append(phi2[i,index2])
                            
                        event_1.append(i)
                        event_2.append(i)

                    elif charge2[i,index2] == charge:
                        charge_12.append(charge2[i,index2])

                        pt_1.append(pt1[i,index1])
                        eta_1.append(eta1[i,index1])
                        phi_1.append(phi1[i,index1])
                            
                        pt_2.append(pt2[i,index2])
                        eta_2.append(eta2[i,index2])
                        phi_2.append(phi2[i,index2])
                            
                        event_1.append(i)
                        event_2.append(i)

        # If one of the particles is a jet and the other a photon:
        elif flavor1 != 0 or flavor2 != 0:
            # If the first kind are jets and the second are photons
            if flavor1 != 0:
                for i in range(events):
                    suma_1 = np.sum(flavor[i] == flavor1)

                    if suma_1 > 0 and len(pt2[i]) > 0:
                        index1 = np.argmax(pt1[i])
                        index2 = np.argmax(pt2[i])

                        if charge1[i,index1] == charge:
                            charge_12.append(charge1[i,index1])

                            pt_1.append(pt1[i,index1])
                            eta_1.append(eta1[i,index1])
                            phi_1.append(phi1[i,index1])
                                
                            pt_2.append(pt2[i,index2])
                            eta_2.append(eta2[i,index2])
                            phi_2.append(phi2[i,index2])
                                
                            event_1.append(i)
                            event_2.append(i)
            # If the first ones are photons and the second are jets
            elif flavor2 != 0:
                for i in range(events):
                    suma_2 = np.sum(flavor[i] == flavor2)

                    if suma_2 > 0 and len(pt1[i]) > 0:
                        index1 = np.argmax(pt1[i])
                        index2 = np.argmax(pt2[i])

                        if charge2[i,index2] == charge:
                            charge_12.append(charge2[i,index2])

                            pt_1.append(pt1[i,index1])
                            eta_1.append(eta1[i,index1])
                            phi_1.append(phi1[i,index1])
                                
                            pt_2.append(pt2[i,index2])
                            eta_2.append(eta2[i,index2])
                            phi_2.append(phi2[i,index2])
                                
                            event_1.append(i)
                            event_2.append(i)

        pt_1 = np.array(pt_1)
        eta_1 = np.array(eta_1)
        phi_1 = np.array(phi_1)
        
        pt_2 = np.array(pt_2)
        eta_2 = np.array(eta_2)
        phi_2 = np.array(phi_2)
         
        event_1 = np.array(event_1)
        event_2 = np.array(event_2)

        charge_12 = np.array(charge_12)
        
        if df == True:
            data = {
                    "pt_1": pt_1,
                    "pt_2": pt_2,
                    "eta_1": eta_1,
                    "eta_2": eta_2,
                    "phi_1": phi_1,
                    "phi_2": phi_2,
                    "charge12": charge_12
                    }
                
            data = pd.DataFrame(data)
                    
        
        
                
           
        
    
    