import gpxpy

from everysinglestreet import GPSPoint, Ride

myride = Ride('data/rides/2020-03-20-18-25.gpx')

myride.GPSPoints[0].print_point()

mypoint = GPSPoint(43.1, -23.2, 129.2, '2020-03-20 22:25:51+00:00')

mypoint.print_point()
