
def lockdowncalculate(data, limiter):
    actives = data[-1]["Active"] - data[-8]["Active"]
    
    
    
    if actives >= limiter:
        print("lockdown")
        lockdown = True
    else:
        print("no lockdown")
        lockdown = False
        
    return lockdown