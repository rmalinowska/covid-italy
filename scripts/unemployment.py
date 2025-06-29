import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as offline

df = pd.read_csv('unemployment.tsv', delimiter='\t')
df = df.set_index('Country').T

fig = go.Figure()

# Adding lines for each country
for country in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[country], mode='lines', name=country, line=dict(width=4)))

# Customizing the appearance of the chart
fig.update_layout(
    legend=dict(font=dict(size=25)),  
    xaxis=dict(title='Date', tickfont=dict(size=20)),  
    yaxis=dict(title='Unemployment rate', tickfont=dict(size=20)),  
    title=dict(text='Unemployment rate in different countries', x=0.5, font=dict(size=35)),
    font=dict(
        size=20,
        color="black"
    )
)

fig.show()
offline.plot(fig, filename='unemployment.html', auto_open=False)