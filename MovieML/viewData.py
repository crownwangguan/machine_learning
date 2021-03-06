import pandas as pd
import webbrowser
import os


data_table = pd.read_csv("movie_ratings_data_set.csv")
html = data_table[0:100].to_html()

movie_table = pd.read_csv("movies.csv")
html1 = movie_table.to_html()

movie_rating_table = pd.read_csv("predicted_ratings.csv")
html2 = movie_rating_table.to_html()

with open("data.html", "w") as f:
    f.write(html)

with open("movie_list.html", "w") as f:
    f.write(html1)

with open("movie_rating_list.html", "w") as f:
    f.write(html2)

full3_filename = os.path.abspath("movie_rating_list.html")
webbrowser.open("file://{}".format(full3_filename))

full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))

full2_filename = os.path.abspath("movie_list.html")
webbrowser.open("file://{}".format(full2_filename))
