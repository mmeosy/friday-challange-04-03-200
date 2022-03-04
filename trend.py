def trendcalculate(data):
    thisweekactives = data[-1]["Active"] - data[-8]["Active"]
    lastweekactives = data[-8]["Active"] - data[-15]["Active"]
    
    if thisweekactives == lastweekactives:
        print("same")
        trend = "Constant"
    elif thisweekactives <= lastweekactives:
        print("lower")
        trend = "Down"
        
        
    else:
        print("hoch")
        trend = "UP"
        
    return trend