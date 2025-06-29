#!/usr/bin/env python3

import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_cumulative_cases(df):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x = italy["Date_reported"], y = italy["total_positive_cases_per_100k"],
                    mode='lines',
                    name='Italy'))
	fig.add_trace(go.Scatter(x = poland["Date_reported"], y = poland["total_positive_cases_per_100k"],
                    mode = 'lines',
                    name = 'Poland'))
					
	fig.add_trace(go.Scatter(x = sweden["Date_reported"], y = sweden["total_positive_cases_per_100k"],
                    mode = 'lines',
                    name = 'Sweden'))

	fig.add_trace(go.Scatter(x = china["Date_reported"], y = china["total_positive_cases_per_100k"],
                    mode = 'lines',
                    name = 'China'))

	fig.write_html("countries_total_cases.html")
	fig.update_layout(
    title="Cumulative Covid-19 cases in different countries per 100k people",
    xaxis_title="date",
    yaxis_title="cumulative Covid-19 positive cases per 100k people",
    font=dict(
        size=12,
		color='black'
    ))
	fig.write_html("../for_report/countries_total_cases.html")
	fig.write_image("../for_report/countries_total_cases.png")



all_countries = pd.read_csv("../data/WHO-COVID-19-global-data.csv")
italy = all_countries[all_countries["Country"] == "Italy"]
italy["total_positive_cases_per_100k"] = italy["Cumulative_cases"]/(59110000/100000)

poland = all_countries[all_countries["Country"] == "Poland"]
poland["total_positive_cases_per_100k"] = poland["Cumulative_cases"]/(38750000/100000)

sweden = all_countries[all_countries["Country"] == "Sweden"]
sweden["total_positive_cases_per_100k"] = sweden["Cumulative_cases"]/(10420000/100000)

china = all_countries[all_countries["Country"] == "China"]
china["total_positive_cases_per_100k"] = china["Cumulative_cases"]/(1412000000/100000)

plot_cumulative_cases(poland)