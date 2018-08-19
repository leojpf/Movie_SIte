import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on a alien planet.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                    "https://youtu.be/d1_JBMrrYw8")

inception = media.Movie("Inception",
                        "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_Mummy = media.Movie("The Mummy",
                        "An old ass Mummy comes back alive!",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/The_mummy.jpg",  # noqa
                        "https://www.youtube.com/watch?v=h3ptPtxWJRs")

limitless = media.Movie("Limitless",
                        "A very lazy guy finds out a kikcing ass drug.",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6d1Uc68wt3c")

averngers_infity = media.Movie("Averngers Infity War",
                        "The fisrt part part of the end. Of phase One",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movies = [toy_story, avatar, inception, the_Mummy, limitless, averngers_infity]
fresh_tomatoes.open_movies_page(movies)
