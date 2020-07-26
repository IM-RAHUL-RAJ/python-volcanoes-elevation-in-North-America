import folium
import pandas
map=folium.Map(location=[46,-122],tiles='Stamen Toner',zoom_start=4)


fg=folium.FeatureGroup(name="My Map")

data=pandas.read_csv('Volcanoes.txt')
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])

def color_elev(elev):

    if(elev<1000):
        return 'green'
    elif(1000<=elev<3000):
        return 'orange'
    else:
        return 'red'

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:  {'fillcolor':'green' if(x['properties']['POP2005']<10000000) else 'orange' if (10000000<=x['properties']['POP2005']<20000000) else 'red' }))
        
    


for lt,ln,ele,jagah in zip(lat,lon,elev,name):


    folium.CircleMarker([lt,ln], tooltip=jagah,popup=str(ele)+' m',tooltip_opacity=1,color=color_elev(ele),fill_opacity=0.9,fill="True",radius=10).add_to(map)




map.save("index.html")

