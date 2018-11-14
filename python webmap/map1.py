import folium
import pandas

# read the comma separated text file through pandas library
data = pandas.read_csv("Volcanoes.txt")

# make list of longitude, latitude and elevation
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

# dynamic color generator depending on various variables
def color_generator(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

# create a map object which will be the center of the map
map = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles='Mapbox Bright')

# create a feature group for adding different functionality
fg = folium.FeatureGroup("My app")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el), fill_color=color_generator(el), color='grey', fill_opacity=0.7))
# add GeoJson data to the map
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))
map.add_child(fg)
map.save("Map1.html")