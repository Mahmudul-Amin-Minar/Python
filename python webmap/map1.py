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
fg_volcanoes = folium.FeatureGroup("Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el), fill_color=color_generator(el), color='grey', fill_opacity=0.7))

# add GeoJson data to the map
fg_population = folium.FeatureGroup('Population')
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
 if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg_volcanoes)
map.add_child(fg_population)
# adding Layer Control
map.add_child(folium.LayerControl())
map.save("Map1.html")