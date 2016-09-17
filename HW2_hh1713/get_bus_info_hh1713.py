from __future__ import print_function
import sys
import csv
import json
import urllib as ulr

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
"0faf290d-2b50-4e21-86eb-69fbbf4466f7&VehicleMonitoringDetailLevel=calls&LineRef=B54"

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

no_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

with open (sys.argv[3],'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    for i in range(0, no_buses):
        Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        if(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls'] == {}):
            stopname = "N/A"
            stopstatus = "N/A"
        else:
            stopname = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            stopstatus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']\
            ['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        writer.writerow([Latitude,Longitude,stopname,stopstatus])
