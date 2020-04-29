import gpxpy

class GPSPoint:
    def __init__(self, lat:float, lon:float, elevation, timestamp):
        self.lat = lat
        self.lon = lon
        self.elevation = elevation
        self.timestamp = timestamp

    def print_point(self):
       print('{} {} at time {} at elevation {}'.format(self.lat, self.lon, self.timestamp, self.elevation))


class Ride:
    def __init__(self, filename):
        gpx = gpxpy.parse(open(filename, 'r'))
        self.rideDate = gpx.time
        self.filename = filename
        self.GPSPoints = self.parseGPXFile()

    def parseGPXFile(self):
        # read in file create GPX object
        gpx_file = open(self.filename, 'r')
        gpx = gpxpy.parse(gpx_file)

        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    point = GPSPoint(
                                point.latitude
                                , point.longitude
                                , point.elevation
                                , point.time
                                )
                    points.append(point)
        
        return points
                    