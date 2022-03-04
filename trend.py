def trendcalculate(data):
    thisweekactives = data[-1]["Active"] - data[-8]["Active"]
    lastweekactives = data[-8]["Active"] - data[-15]["Active"]
    
    if thisweekactives == lastweekactives:
        
        trend = "Constant"
    elif thisweekactives <= lastweekactives:
        
        trend = "Down"
        
        
    else:
        
        trend = "UP"
        
    return trend