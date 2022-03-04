import requests
import json
import trend 
import lockdown
import active
import cases
from writejson import writejsonfile
lockdown_limiter = 1000






url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()

#print(y['Confirmed'])



cases = (cases.TotalactiveCases(response))
active = (active.activeCases(response))

trend = (trend.trendcalculate(response))

lockdown = (lockdown.lockdowncalculate(response, lockdown_limiter))

writejsonfile(json.dumps({"cases": cases, "active": active, "trend": trend, "lockdown": lockdown}))

