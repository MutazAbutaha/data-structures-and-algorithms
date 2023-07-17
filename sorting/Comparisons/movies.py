class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year}, genres={self.genres})"


class MovieSorter:
    @staticmethod
    def sortByYearDescending(movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
        return sorted_movies

    @staticmethod
    def sortAlphabeticallyIgnoringArticles(movies):
        def remove_leading_articles(title):
            articles = ["A ", "An ", "The "]
            for article in articles:
                if title.startswith(article):
                    return title[len(article):]
            return title

        sorted_movies = sorted(movies, key=lambda movie: remove_leading_articles(movie.title))
        return sorted_movies


movies = [
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
    Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
]

sorted_by_year = MovieSorter.sortByYearDescending(movies)
print("Sorted by year descending:")
for movie in sorted_by_year:
    print(movie.title, movie.year)

sorted_alphabetically = MovieSorter.sortAlphabeticallyIgnoringArticles(movies)
print("\nSorted alphabetically (ignoring articles):")
for movie in sorted_alphabetically:
    print(movie.title)
