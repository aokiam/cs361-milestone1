# this will give a user a kpop recommendation based on their jpop likes

class KpopRecommendationService:
    def __init__(self, artists):
        self.artists = artists

    def recommend_kpop_from_jpop(self, jpop_attributes):
        return [artist.name for artist in self.artists if artist.pop =="kpop" and
                any(attr in artist.attributes for attr in jpop_attributes)]