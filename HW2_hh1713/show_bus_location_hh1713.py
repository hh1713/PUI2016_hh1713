from __future__ import print_function
import sys
import json
import urllib as ulr

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_location_hh1713.py YourKeyHere <BusLine>")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print ("Bus Line : %s" %(sys.argv[2]))
print ("Number of Active Buses : %d" %(len(busData)))

i = 0
for bus in busData:
    longitude = busData[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = busData[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print ("Bus %d is at latitude %f and longitude %f" %(i, latitude, longitude))
    i += 1