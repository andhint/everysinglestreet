class GPSPoint:
    def __init__(self, lat:float, lon:float, elevation, timestamp):
        self.lat = lat
        self.lon = lon
        self.elevation = elevation
        self.timestamp = timestamp

    def print_point(self):
       print('{} {} at time {} at elevation {}'.format(self.lat, self.lon, self.timestamp, self.elevation))
