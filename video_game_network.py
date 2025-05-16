import holoviews as hv
import pandas as pd
import numpy as np

hv.extension('bokeh')

df = pd.read_csv("./imports/all_video_games.csv")
df = df.head(40)

df.drop(columns=[
    "Release Date", "Product Rating", "User Score",
    "User Ratings Count", "Platforms Info", "Developer", "Publisher"
], inplace=True)
df['Genres Splitted'] = df['Genres'].apply(lambda x: x.strip("[]").replace("'", ""))

genre_counts = {}
for index, row in df.iterrows():
    genres_list = [genre.strip() for genre in row['Genres Splitted'].split(",")]
    primary_genre = genres_list[0]
    genre_counts[primary_genre] = genre_counts.get(primary_genre, 0) + 1

df['value'] = df['Genres Splitted'].map(genre_counts).fillna(1)
df['target'] = df['Genres Splitted']
df['source'] = df['Title']

df = df[['source', 'target', 'value']]

df = df.sort_values(by='value', ascending=True)

sankey = hv.Sankey(df, label='Video Game Genre Network')
sankey.opts(
    label_position='left', 
    edge_color='target', 
    node_color='index', 
    cmap='tab20',
    edge_line_width=9,
    )
hv.save(sankey, './exports/sankey_chart.html')