import gpxpy

from .GPSPoint import GPSPoint

class Ride:
    def __init__(self, filename):
        self._gpx = gpxpy.parse(open(filename, 'r'))
        self.ride_date = self._gpx.time
        self.filename = filename
        self.gps_points = self.parse_gpx_file()
        self.ride_length_meters = self._gpx.length_2d()

    def parse_gpx_file(self):
        points = []
        for track in self._gpx.tracks:
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
                    