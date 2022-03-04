
def lockdowncalculate(data, limiter):
    actives = data[-1]['Active'] - data[-8]['Active']
    
    
    
    if actives >= limiter:
        
        lockdown = True
    else:
        
        lockdown = False
        
    return lockdown