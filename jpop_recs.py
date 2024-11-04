# this will give a user a jpop recommendation based on their kpop likes

class JpopRecommendationService:
    def __init__(self, artists):
        self.artists = artists

    def recommend_jpop_from_kpop(self, kpop_attributes):
        return [artist.name for artist in self.artists if artist.pop =="jpop" and
                any(attr in artist.attributes for attr in kpop_attributes)]