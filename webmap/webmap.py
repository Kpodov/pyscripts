import folium
import pandas


def draft1():

    data = pandas.read_csv("Volcanoes.txt")
    lat = list(data["LAT"])
    lon = list(data["LON"])
    elev = list(data["ELEV"])
    name = list(data["NAME"])

    html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s m
    """

    map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
    fg = folium.FeatureGroup(name = "My Map")

    for lt, ln, el, name in zip(lat, lon, elev, name):
        iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=8, fill_opacity=0.5, fill=True, color='yellow', popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))


    # create a json object
    datajson = open('world.json', 'r', encoding='utf-8-sig').read()
    fg.add_child(folium.GeoJson(datajson))

    map.add_child(fg)
    map.save("Map_html_popup_advanced.html")


draft1()
