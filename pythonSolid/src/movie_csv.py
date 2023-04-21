import csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        self.fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]

    def write_data(self, data):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            for movie in data:
                writer.writerow({**movie})
