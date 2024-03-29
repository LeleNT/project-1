# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:45:28 2024

@author: ntand
"""
import pandas as pd
df = pd.read_csv("C:\\Users\\ntand\\CSS2024_day1\\CSS2024_day1\\CSS2024_day3\\Project 1\\movie_dataset.csv")

# Filter the Data for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]
number_of_high_rated_movies = len(high_rated_movies)
print(f"The number of movies in the dataset with a rating of at least 8.0 is {number_of_high_rated_movies}.")

 #Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
print(f"Movies directed by Christopher Nolan is {nolan_movies}.")

 #Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")

# Calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()
# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")

# Calculate the percentage increase in number of movies made beteen 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

count_2006 = len(movies_2006)
count_2016 = len(movies_2016)
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is {percentage_increase:.2f}%.")

# The most common actor
actors_df = df['Actors'].str.split(', ', expand=True)
actors_list = actors_df.values.flatten()
actors_count = pd.Series(actors_list).value_counts()
most_common_actor = actors_count.idxmax()
print(f"The most common actor in all the movies is: {most_common_actor}")

# number of unique genres in the dataset
genres_df = df['Genre'].str.split(', ', expand=True)
genres_list = genres_df.values.flatten()
unique_genres_count = len(set(genres_list))
print(f"The number of unique genres in the dataset is: {unique_genres_count}")

# Correlation of the numerical features
numerical_features = df[['Rank', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]
correlation_matrix = numerical_features.corr()
print("Correlation Matrix:")
print(correlation_matrix)

