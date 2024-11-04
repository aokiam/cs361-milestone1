# this will compare two artists and show brief information about both of them

class ComparisonService:
    def __init__(self, artists):
        self.artists = artists

    def compare_artists(self, artist1_name, artist2_name):
        for artist1 in self.artists:
            if artist1.name == artist1_name:
                artist1 = artist1
            
        for artist2 in self.artists:
            if artist2.name == artist2_name:
                artist2 = artist2

        if artist1 and artist2:
            comparison = {
                "Artist Name":(artist1.name, artist2.name),
                "Type":(artist1.pop, artist2.pop),
                "Top 3 Songs":(artist1.top3, artist2.top3),
                "Genre Attributes":(artist1.attributes, artist2.attributes),
            }
            return comparison
        return None