import numpy as np
import pandas as pd
import matrix_factorization_utilities


raw_dataset_df = pd.read_csv("movie_ratings_data_set.csv")
movies_df = pd.read_csv("movies.csv", index_col='movie_id')
ratings_df = pd.pivot_table(raw_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

# Apply matrix factorization to find the latent features
U, M = matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.as_matrix(),
                                                                    num_features=15,
                                                                    regularization_amount=0.1)

# Swap the rows and columns of product_features just so it's easier to work with
M = np.transpose(M)

movie_id = 1
movie_information = movies_df.loc[movie_id]

print("We are finding movies similar to this movie:")
print("Movie title: {}".format(movie_information.title))
print("Genre: {}".format(movie_information.genre))

# Get the features for movie #1 we found via matrix factorization
current_movie_features = M[movie_id - 1]

print("The attributes for this movie are:")
print(current_movie_features)

# The main logic for finding similar movies:

# 1. Subtract the current movie's features from every other movie's features
difference = M - current_movie_features

# 2. Take the absolute value of that difference (so all numbers are positive)
absolute_difference = np.abs(difference)

# 3. Each movie has 15 features. Sum those 15 features to get a total 'difference score' for each movie
total_difference = np.sum(absolute_difference, axis=1)

# 4. Create a new column in the movie list with the difference score for each movie
movies_df['difference_score'] = total_difference

# 5. Sort the movie list by difference score, from least different to most different
sorted_movie_list = movies_df.sort_values('difference_score')

# 6. Print the result, showing the 5 most similar movies to movie_id #1
print("The five most similar movies are:")
print(sorted_movie_list[['title', 'difference_score']][0:5])
