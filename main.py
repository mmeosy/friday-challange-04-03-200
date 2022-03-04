import requests
import json
import trend 
import lockdown
import active
import cases
from writejson import writejsonfile
from creates3 import create_bucket, upload_file
lockdown_limiter = 1000






url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()

#print(y['Confirmed'])



cases = (cases.TotalactiveCases(response))
active = (active.activeCases(response))

trend = (trend.trendcalculate(response))

lockdown = (lockdown.lockdowncalculate(response, lockdown_limiter))

writejsonfile(json.dumps({"cases": cases, "active": active, "trend": trend, "lockdown": lockdown}))

bucket_name = 'my-lilya-3'
create_bucket(bucket_name)
upload_file('coronainfo.json', bucket_name)