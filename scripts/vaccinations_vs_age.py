import pandas as pd
import plotly.graph_objects as go
import plotly.offline as offline

# Loading data from CSV file
df = pd.read_csv("vaccinations.csv")
df = df.drop(columns=["area", "N1", "N2", "ISTAT", "m", "f"], errors='ignore')
df.rename(columns = {'data':'date', 'forn':'vaccine_name', 'eta':'age_range',  'reg':'region'}, inplace = True)

# Determination of age ranges
bins = [0, 18, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '90+']

# Extraction of a number from an age range
df['age_range'] = df['age_range'].str.extract('(\d+)').astype(float)

# Data grouping for age ranges
df['age_group'] = pd.cut(df['age_range'], bins=bins, labels=labels, right=False)

# Adding values for each vaccine type and age range
df_grouped = df.groupby(['age_group']).sum()

# Calculate the percentage of total vaccinated for each vaccine type and age range
df_grouped_percent = df_grouped.div(df_grouped.sum(axis=1), axis=0) * 100
df_grouped['d2'] = df_grouped['d2'] + df_grouped['dpi']

fig = go.Figure()

# Adding bars for each vaccine type
vaccine_columns = ['d1', 'd2', 'db1', 'db2', 'db3']
vaccine_names = ['One dose', 'Two doses', '1. booster dose', '2. booster dose', '3. booster dose']

for i in range(len(vaccine_columns)):
    fig.add_trace(go.Bar(
        x=df_grouped[vaccine_columns[i]],
        y=df_grouped.index,
        name=vaccine_names[i],
        hovertemplate='Number of vaccine doses: %{x}<br>Percent: %{customdata:.2f}%<extra></extra>',
        customdata=df_grouped_percent[vaccine_columns[i]].round(2),
        orientation='h',
        textposition='inside'  # Centering the subtitles inside the bars
    ))

fig.update_layout(
    legend=dict(font=dict(size=16)),  
    xaxis=dict(title='Number of vaccine doses', tickfont=dict(size=13)),  
    yaxis=dict(title='Age range', tickfont=dict(size=13)),  
    title=dict(text='Number of doses taken, broken down by age of patients', x=0.5, font=dict(size=20)),
    barmode='stack' 
)

fig.update_traces(text=None)
fig.show()

offline.plot(fig, filename='vaccinations_vs_age.html', auto_open=False)