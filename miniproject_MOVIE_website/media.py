# class declaration
class Movie():
    """this class can be used to save movies data"""

    # init constructor for movies' data (user defined function)
    def __init__(self, movie_title, movie_storyline,
                poster_image, trailer_youtube):
        # declaration of instance variable
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
