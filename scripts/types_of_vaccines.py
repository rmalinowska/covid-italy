import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.offline as offline

df = pd.read_csv("vaccinations.csv")
df = df.drop(columns=["area", "N1", "N2", "ISTAT", "m", "f"], errors='ignore')
df.rename(columns = {'data':'date', 'forn':'vaccine_name', 'eta':'age_range',  'reg':'region'}, inplace = True)

# Creating a column with month and year
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df['month_year'] = df['date'].dt.strftime('%m-%Y')

# Data cleaning
df = df.drop(df[df['vaccine_name'] == 'Sanofi'].index)
df = df.drop(df[df['vaccine_name'] == 'Novavax'].index)

# Grouping by month, year and type of vaccine
df_monthly = df.groupby(['month_year', 'vaccine_name']).sum()
df_monthly = df_monthly.sort_values('month_year', key=lambda x: pd.to_datetime(x, format='%m-%Y'))

# Creating a chart
fig = go.Figure()

# Adding bars for each month,year and vaccine type
for vaccine in df_monthly.index.get_level_values('vaccine_name').unique():
     data = df_monthly.xs(vaccine, level='vaccine_name')
     fig.add_trace(go.Bar(x=data.index, y=data.sum(axis=1), name=vaccine, width=0.16))

# Customization of axis title and descriptions
fig.update_layout(
    legend=dict(font=dict(size=16)),  
    xaxis=dict(title='Date', tickfont=dict(size=13)),  
    yaxis=dict(title='Sum of vaccinations', tickfont=dict(size=13)),  
    title=dict(text='Total vaccinations per month, year and vaccine type', x=0.5, font=dict(size=20))
)

fig.show()
offline.plot(fig, filename='types_of_vaccines.html', auto_open=False)