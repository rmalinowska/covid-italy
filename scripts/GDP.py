import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.offline as offline

df = pd.read_csv('gdp_countries.csv')

# Selection of data from 2010-2022
columns = df.columns[2:][(df.columns[2:] >= '2010') & (df.columns[2:] <= '2022')]
df = df[['Country Name'] + list(columns)]

fig = go.Figure()

# Adding lines for each country
for country in df["Country Name"]:
    fig.add_trace(go.Scatter(x=df.columns[1:], y=df.loc[df["Country Name"] == country].values[0][1:],
                             mode='lines', name=country, line=dict(width=3)))

fig.update_layout(
    legend=dict(font=dict(size=25)),  
    xaxis=dict(title='Year', tickfont=dict(size=20)),  
    yaxis=dict(title='GDP (in USD trillions)', tickfont=dict(size=20)),  
    title=dict(text='GDP growth in different countries', x=0.5, font=dict(size=35)),
    font=dict(
        size=20,
        color="black"
    )
)

fig.show()
offline.plot(fig, filename='gdp.html', auto_open=False)