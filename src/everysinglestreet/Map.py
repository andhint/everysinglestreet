import random
import folium

class Map:
    def __init__(self, lat=42.89, lon=-78.82, zoom=12, tiles='Stamen Toner'):
        self.map = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=tiles)
        self._colors = [
                        '#d35400', '#e67e22', '#f39c12', '#f1c40f', '#2ecc71', 
                        '#27ae60', '#16a085', '#1abc9c', '#3498db', '#2980b9', 
                        '#8e44ad', '#9b59b6', '#e74c3c', '#c0392b'
                        ]

    def add_ride_gps_to_map(self, Ride):
        folium.PolyLine(Ride.gps_points,
                        color=random.choice(self._colors),
                        weight=4,
                        opacity=1, 
                        tooltip=f"{Ride.ride_length_miles:.1f} miles on {Ride.ride_date:%Y-%m-%d}"
                        ).add_to(self.map)

    def add_city_boundary(self, filename):
        style = {'fillOpacity': 0.2, 'color': 'black'}

        folium.GeoJson(
            filename,
            style_function=lambda x: style
        ).add_to(self.map)

    def save_to_html(self, filename):
        self.map.save(filename)