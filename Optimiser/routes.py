import searoute as sr
import folium

# Define origin and destination as [longitude, latitude]
origin = [103.8198, 1.3521]       # Singapore
destination = [121.4737, 31.2304] # Shanghai

# Compute the SeaRoute
route_geo = sr.searoute(origin, destination, units='naut')  # returns GeoJSON-like object

# Extract distance
distance_nautical_miles = route_geo.properties['length']
units = route_geo.properties['units']
print(f"Distance: {distance_nautical_miles:.1f} {units}")

# Extract coordinates for plotting (list of [lon, lat])
coordinates = route_geo.geometry['coordinates']

# Center the map on the midpoint
midpoint = [(origin[1] + destination[1]) / 2, (origin[0] + destination[0]) / 2]
m = folium.Map(location=midpoint, zoom_start=4)

# Plot the SeaRoute as a blue polyline
folium.PolyLine(
    locations=[(lat, lon) for lon, lat in coordinates],
    color='blue',
    weight=3,
    opacity=0.8
).add_to(m)

# Add markers for origin and destination
folium.Marker(location=[origin[1], origin[0]], popup='Singapore').add_to(m)
folium.Marker(location=[destination[1], destination[0]], popup='Shanghai').add_to(m)

# Save map to HTML
m.save("sea_route_map.html")

print("SeaRoute map saved as 'sea_route_map.html'. Open this file in a browser to view the route.")
