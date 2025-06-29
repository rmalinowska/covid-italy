import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import plotly.offline as offline

df = pd.read_csv("vaccinations.csv")
df = df.drop(columns=["area", "N1", "N2", "ISTAT", "m", "f"], errors='ignore')
df.rename(columns = {'data':'date', 'forn':'vaccine_name', 'eta':'age_range',  'reg':'region'}, inplace = True)
total_fully_vaccinated = df['d2'] + df['dpi']

# Vaccination data for Italy and Poland
total_population_italy = 60665551  
fully_vaccinated_italy = total_fully_vaccinated.sum()
total_population_poland = 37958138
fully_vaccinated_poland = 22648094
labels = ['Vaccinated', 'Not Vaccinated']
colors = ['purple', 'orange']
italy = [fully_vaccinated_italy, total_population_italy - fully_vaccinated_italy]
poland = [fully_vaccinated_poland, total_population_poland - fully_vaccinated_poland]

fig = make_subplots(1, 2, subplot_titles=['Italy', 'Poland'], specs=[[{"type": "pie"}, {"type": "pie"}]])

# Italy
fig.add_trace(go.Pie(labels=labels, values=italy, marker=dict(colors=colors), 
                     hoverinfo='label+percent', textinfo='value+percent', hole=0, textfont=dict(size=16)), 
              row=1, col=1)

# Poland
fig.add_trace(go.Pie(labels=labels, values=poland, marker=dict(colors=colors), 
                     hoverinfo='label+percent', textinfo='value+percent', hole=0, textfont=dict(size=16)), 
              row=1, col=2)

fig.update_layout(height=400, width=800, title_text='Vaccination ratio', title_font=dict(size=30),
                  title=dict(x=0.5),
                  legend=dict(font=dict(size=20)),
                  annotations=[dict(text='Italy', x=0.22, y=1, font=dict(size=20)),
                               dict(text='Poland', x=0.78, y=1, font=dict(size=20))])

fig.show()
offline.plot(fig, filename='vaccination_ratio.html', auto_open=False)