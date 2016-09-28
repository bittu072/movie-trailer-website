import fresh_tomatoes
import media

# instances for class movie from the file media.py
sherlock_holmes = media.Movie("Sherlock holmes",
                        "A story of murder mystery",
                        "http://www.impawards.com/2009/posters/sherlock_holmes.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=V1OYiPa-eLg")

inception = media.Movie("Inception",
                    "The mystery movie of the journey of the dreams",
                    "http://www.warnerbros.com/sites/default/files/inception_keyart.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=8hP9D6kZseM")

interstellar = media.Movie("Interstellar",
                    "A blackhole theory",
                    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

fast_and_furious = media.Movie("Fast and furious",
                    "A story of street car racer",
                    "http://screenshots.en.sftcdn.net/en/scrn/319000/319951/fast-five-fast-furious-5-9.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=tPZfa7bZzF4")

armageddon = media.Movie("Armageddon",
                    "A sci-fi movie, about saving the world from an astroid"
                    " impact",
                    "http://4.bp.blogspot.com/-0gIuz22Xca4/UfQJLyN0EbI/AAAAAAAAAAA/4a4oo5FbINo/s1600/armageddon_1998_580x745_848715.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=kg_jH47u480")

wolf_of_wallstreet = media.Movie("Wolf of wallstreet",
                    "A journey of a stock-broker, from zero to millionaire",
                    "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=iszwuX1AK6A")

dark_knight = media.Movie("The Dark knight",
                    "A story of Batman and Joker",
                    "http://cdn.playbuzz.com/cdn/1ed7ba7c-df09-4a9e-852f-d983e9a52dcb/37af3fe7-038d-44c1-99c3-8b60f9db2573.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("The matrix",
                    "Humans perceived a reality of the matrix",
                    "https://upload.wikimedia.org/wikipedia/en/9/9a/The_Matrix_soundtrack_cover.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# defining array for the movie instances
movies = [sherlock_holmes, inception, interstellar, fast_and_furious,
            armageddon, wolf_of_wallstreet , dark_knight, avatar, matrix]
fresh_tomatoes.open_movies_page(movies)  # calling function "open_movies_page"
