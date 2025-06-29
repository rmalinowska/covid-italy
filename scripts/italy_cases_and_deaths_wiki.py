#!/usr/bin/env python3

import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

all_countries = pd.read_csv("../data/WHO-COVID-19-global-data.csv")
italy = all_countries[all_countries["Country"] == "Italy"]
italy["new_positive_cases_per_100k"] = italy["New_cases"]/(59110000/100000)
italy["new_deaths_per_100k"] = italy["New_deaths"]/(59110000/100000)


def plot_new_cases(df):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x = italy["Date_reported"], y = italy["new_positive_cases_per_100k"],
                    mode='lines', marker=dict(color='black')))
	

	fig.update_layout(
	height = 600,
	width = 1400,
    title="Daily Covid-19 cases in Italy per 100k people",
    xaxis_title="Date",
    yaxis_title="daily Covid-19 positive cases per 100k people",
    font=dict(
        size=12,
		color='black'
    ),
	)
	fig.update_xaxes(
    tickmode='linear',
    tickformat='%Y-%m-%d',
    tickangle=45,
    dtick='M1'
)
	fig.write_image("../italy_new_cases_wiki.png")

def plot_new_deaths(df):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x = italy["Date_reported"], y = italy["new_deaths_per_100k"],
                    mode='lines', marker=dict(color='black')))
	

	fig.update_layout(
	height = 600,
	width = 1400,
    title="Daily deaths due to Covid-19 in Italy per 100k people",
    xaxis_title="Date",
    yaxis_title="daily Covid-19 deaths per 100k people",
    font=dict(
        size=12,
		color='black'
    ),
	)
	fig.update_xaxes(
    tickmode='linear',
    tickformat='%Y-%m-%d',
    tickangle=45,
    dtick='M1'
)
	fig.write_image("../italy_deaths_wiki.png")

plot_new_cases(italy)
plot_new_deaths(italy)
