from movie_data import Data
from movie_csv import CSVWriter

if __name__ == '__main__':
    imdb = Data('http://www.imdb.com/chart/top')
    movie_details = imdb.get_movie_details()

    csv_writer = CSVWriter('movie_results.csv')
    csv_writer.write_data(movie_details)
