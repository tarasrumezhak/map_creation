import pandas as pd
import folium
import geocoder
import map

def main(film_count, city, film):
    '''
    (bool, bool, str) --> None
    This function creates the map with markers of filming locations
    and if film_count and city are True, shows the choropleth of filming
    locations count in country and cities with the most films
    '''
    data = pd.read_csv("data3.csv")
    df = pd.read_csv("data.csv")
    df2 = df[df["title"].str.contains(film, na=False)]["location"]
    df2 = df2.reset_index()

    m = folium.Map(zoom_start=10)

    for i in df2["index"]:
        folium.Marker( location=[float(x) for x in map.get_coords(df["location"][i])],
             popup=df["title"][i],
             icon = folium.Icon(color="orange", icon="camera")
              ).add_to(m)

    if film_count:
        country_geo = 'world.geo.json'
        m.choropleth(
         geo_data=country_geo,
         name='choropleth',
         data=data,
         columns=['country', 'count'],
         key_on= 'feature.properties.name',
         fill_color='YlGn',
         fill_opacity=0.7,
         line_opacity=0.2,
         legend_name='Films',
         threshold_scale=[0, 50, 1000, 10000, 100000, 250000, 500000]
        )
        folium.LayerControl().add_to(m)

    if city:
        data4 = pd.read_csv("data4.csv")
        for i in range(0,len(data4)):
           folium.Circle(
              location=[float(x) for x in map.get_coords(data4["city"][i])],
              popup=data4.iloc[i]['city'],
              radius=int(data4.iloc[i]['count'])*2,
              color='red',
              fill=True,
              fill_color='crimson'
           ).add_to(m)

    m.save('Map.html')

if __name__ == '__main__':
    info = map.info_request()
    main(info[0], info[1], info[2])
