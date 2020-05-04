from everysinglestreet import Ride, Map

# example usage

# create Ride from GPX file
my_ride = Ride('data/rides/2020-03-20-18-25.gpx')

# print some info
print(my_ride.ride_date)
print(my_ride.ride_length_meters)

# create a map to visualize rides on
my_map = Map()

# add my ride to the map
my_map.add_ride_gps_to_map(my_ride)

# add another one
my_other_ride = Ride('data/rides/2020-03-26-18-48.gpx')
my_map.add_ride_gps_to_map(my_other_ride)

# if using in notebook, can just call my_map.map to view
# otherwise need to save to save to html to view
my_map.save_to_html('docs/map.html')
