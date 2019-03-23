# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    lat = 0;
    lon = 0;
    def __init__(self, _lat, _lon):
        self.lat = _lat;
        self.lon = _lon;
    def __str__(self):
        return (f"Lat: {self.lat}, Lon: {self.lon}");
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    name = "";
    def __init__(self, _name,_lat,_lon):
        self.name = _name;
        LatLon.__init__(self,_lat,_lon);
    def __str__(self):
        return (f"Name: {self.name}, {LatLon.__str__(self)}");

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    difficulty = 0;
    size = (0,0);
    def __init__(self,_name,_difficulty,_size,_lat,_lon):
        self.difficulty = _difficulty;
        self.size = _size;
        Waypoint.__init__(self,_name,_lat,_lon);
    def __str__(self):
        return (f"{Waypoint.__str__(self)} Size: {self.size}, Difficulty: {self.difficulty}");

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint("Catacombs",41.70505, -121.51521);

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137,-121.41556);

# Print it--also make this print more nicely
print(geocache)
