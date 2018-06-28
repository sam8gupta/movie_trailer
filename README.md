## Movie Trailer
### A project displaying all of your favorite movies including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.

## Installation
Before you start, you need to have python(python 2 preffered) installed in your computer.
If not, download python from this <a href="https://www.python.org/downloads/mac-osx/">link</a> and follow the installion process.

Now download the project zip files, extract them to a folder in a drive.

To run the project on mac, open `Terminal` and change directory to the place where you extracted the files.
Type `python ./entertainment.py` to access the webpage.

## Usage
You can add the information of your favourite movies in the `entertainment.py` file in the specified format:

variable = media.Movie(
    "Movie Title",
    "Storyline",
    "Link of the poster image",
    "Link of the Trailer"
    )
    
For instance,

dhadak = media.Movie(
    "Dhadak",
    "This love story explores how the protagonists deal with issues like differences between castes and honor killings.",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Dhadak_2018_film.jpg",
    "https://www.youtube.com/watch?v=TIE92mUvSsw"
    )
    
All the movies added will be displayed on the webpage.

## Conclusion

Here is the description of the files, incase you you want to enhance the project: 

`entertainment.py` file contains multiple instances of movie class to represent your favorite movies, grouping all the instances together in a list

`fresh_tomatoes.py` file generate a website that displays these movies.

`media.py` contains a movie class used to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
