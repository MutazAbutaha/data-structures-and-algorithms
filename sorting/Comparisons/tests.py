import pytest
from movies import Movie, MovieSorter


@pytest.fixture
def movies():
    return [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    ]


def test_sortByYearDescending(movies):
    sorted_movies = MovieSorter.sortByYearDescending(movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2012, 2008, 2004]


def test_sortAlphabeticallyIgnoringArticles(movies):
    sorted_movies = MovieSorter.sortAlphabeticallyIgnoringArticles(movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ["Anchorman: The Legend of Ron Burgundy", "The Avengers", "The Dark Knight"]
