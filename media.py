import webbrowser

class Movie():
	""" Creates Movie objects. 

	Creates Movie objects that contain information related to the movie. 

	Args:
		title: Proper title of the movie.
		poster_image_url: Url of the poster image.
		trailer_youtube_url: Url of the youtube hosted trailer of the movie.
		imdb_score: IMDB score in the format of *.*/10.
	"""
	def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_score):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.imdb_score = imdb_score

	def show_trailer(self):
		""" Opens the trailer in a web browser. """
		webbrowser.open(self.trailer_youtube_url)