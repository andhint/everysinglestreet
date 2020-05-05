import glob

from everysinglestreet import Ride, Map

my_map = Map()

# read in municipal boundary
buffalo = 'data/geo/buffalo_boundary.json'
my_map.add_city_boundary(buffalo)

# read in all GPX files and create a Ride() for each one
gpx_files = glob.glob('data/rides/*.gpx')

for filename in gpx_files:
    my_ride = Ride(filename)
    my_map.add_ride_gps_to_map(my_ride)

my_map.save_to_html('docs/map.html')