import media
import fresh_tomatoes

# movie objects which will be displayed in the webpage
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=e8GBfNo3IHY")
                            
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=U_3gIxrcWK8&t=1s")
                            
hunger_games = media.Movie("The Hunger Games",
                           "A really real reality show.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=EAzGXqJSDJ8&t=1s")

dhadak = media.Movie("Dhadak",
                     "This love story explores how the protagonists deal with issues like differences between castes and honor killings.",
                     "https://upload.wikimedia.org/wikipedia/en/f/fb/Dhadak_2018_film.jpg",
                     "https://www.youtube.com/watch?v=TIE92mUvSsw")

#creating a list of movies to feed to open_movie_page function
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, dhadak]
fresh_tomatoes.open_movies_page(movies)



