import pandas as pd

import plotly.graph_objects as go

df = pd.read_csv("./imports/vgsales.csv")
df.dropna(how="any",inplace = True)

df.Year = df.Year.astype(int)

df2015 = df[df.Year == 2015].iloc[:20,:]

fig = go.Figure(data=go.Scatter(
    x=df2015["Rank"],
    y=df2015["NA_Sales"],
    mode='markers+text',
    marker=dict(
        size=df2015["Global_Sales"] * 5,
        color=df2015["EU_Sales"],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(
            title="EU Sales (millions)"
        )
    ),
    text=df2015["Name"],        
    hoverinfo='text'            
))

fig.update_layout(
    title="World rank (first 20) Games vs Nort America Sales with Europe Sales and Global Sales in 2015",
    xaxis_title="Rank",               
    yaxis_title="NA Sales (millions)",
)

fig.show()