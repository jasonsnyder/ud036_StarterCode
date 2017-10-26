import fresh_tomatoes
import media

# Create objects of your favorite movies with some attributes.

rudy = media.Movie("Rudy",
					"https://images-na.ssl-images-amazon.com/images/M/MV5BZGUzMDU1YmQtMzBkOS00MTNmLTg5ZDQtZjY5Njk4Njk2MmRlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",
					"https://youtu.be/eEFG8QA7y2w",
					"7.5/10")

the_fifth_element = media.Movie("The Fifth Element",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_SY1000_CR0,0,696,1000_AL_.jpg",
								"https://youtu.be/7-9mTiBawSM",
								"7.7/10")

reservoir_dogs = media.Movie("Reservoir Dogs",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
								"https://youtu.be/vayksn4Y93A",
								"8.3/10")

full_metal_jacket = media.Movie("Full Metal Jacket",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BNzc2ZThkOGItZGY5YS00MDYwLTkyOTAtNDRmZWIwMGRhYTc0L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,656,1000_AL_.jpg",
								"https://youtu.be/Ks_MbPPkhmA",
								"8.3/10")

trainspotting = media.Movie("Trainspotting",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg",
								"https://youtu.be/8LuxOYIpu-I",
								"8.2/10")

the_big_lebowski = media.Movie("The Big Lebowski",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BZTFjMjBiYzItNzU5YS00MjdiLWJkOTktNDQ3MTE3ZjY2YTY5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
								"https://youtu.be/cd-go0oBF4Y",
								"8.2/10")

stand_by_me = media.Movie("Stand By Me",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxODliZDYtMGMyYy00ZDQzLTgzOTMtMWY5YWEyNTBhNzk5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
							"https://youtu.be/soEFK6PSKEY",
							"8.1/10")

v_for_vendetta = media.Movie("V For Vendetta",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BYzllMjJkODAtYjMwMi00YmNhLWFhYzAtZjZjODg5YzEwOGUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,679,999_AL_.jpg",
							"https://youtu.be/lSA7mAHolAw",
							"8.2/10")

the_goonies = media.Movie("The Goonies",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BOTlmMWU5YTQtOWMxMi00OWE0LTg2MDItMjEyZDBjNWY0NDdhL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
							"https://youtu.be/hJ2j4oWdQtU",
							"7.8/10")

the_sandlot = media.Movie("The Sandlot",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BODllYjM1ODItYjBmOC00MzkwLWJmM2YtMjMyZDU3MGJhNjc4L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
							"https://youtu.be/ec9W8JbFykw",
							"7.8/10")


office_space = media.Movie("Office Space",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BOTA5MzQ3MzI1NV5BMl5BanBnXkFtZTgwNTcxNTYxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
							"https://youtu.be/dMIrlP61Z9s",
							"7.8/10")


# Create a list of the movie objects
movies = rudy, stand_by_me, office_space, full_metal_jacket, the_fifth_element, the_sandlot, the_goonies, trainspotting, reservoir_dogs, the_big_lebowski, v_for_vendetta

# Create and launch your page with your list of movies.
fresh_tomatoes.open_movies_page(movies)