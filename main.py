import requests
import json
import trend 
import lockdown
lockdown_limiter = 1000






url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()
y = response[-1]
#print(y['Confirmed'])

cases = response[-1]['Confirmed'] - response[-8]['Confirmed']
active = response[-1]['Active'] - response [-8]['Active']
print(cases)
print(active)

print(trend.trendcalculate(response))

print(lockdown.lockdowncalculate(response, lockdown_limiter))






def writejsonfile(data):
    with open('coronainfo.json', 'a') as file:
        file.write(data)
        
        


#confirmedinfo = input("if info is confirmed, type yes for write in json file :")

#if confirmedinfo == "yes":
    #writejsonfile(covidinfo)