import searoute as sr
import json

sgp = [103.8198, 1.3521]
sgh = [121.4737, 31.2304]

route = sr.searoute(sgp, sgh, units = 'naut')
distance_nautical_miles = route.properties['length']
units = route.properties['units']
print(f"Distance: {distance_nautical_miles:.1f} {units}")