#challenge problem 
#cristofer jimenez
# DID NOT ATTEMPT! 
import math
lat1= math.radians(float(input(" Latitude 1:")))
lon1= math.radians(float(input(" Longitude 1:")))
lat2= math.radians(float(input(" Latitude 2:")))
lon2= math.radians(float(input(" Longitude 2:")))

dlon= lon2-lon1
dlat=lat2-lat1
r= 3961
a = ((math.sin(dlat/2)**2)+math.cos(lat1)) * math.cos(lat2) * (math.sin(dlon/2)**2)
c= 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
d = r * c
print(f"The spherical distance is {d} miles")


