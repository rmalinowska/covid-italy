#!/usr/bin/env python3
from tokenize import group
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import json
import sys
import geopandas as gpd
from dash import Dash, dcc, html, Input, Output
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go


covid = pd.read_csv("../data/covid19_italy_regions.csv")
covid["total_cases_per_10k"] = covid["total_positive_cases"]/(covid["region_population"]/10000)
covid["total_deaths_per_10k"] = covid["deaths"]/(covid["region_population"]/10000)

region_names = covid["region_name"].unique()

grouped_covid = covid.groupby(["region_name"])

grouped_regions = []
grouped_total_deaths = []
grouped_total_cases = []

groups = dict(list(grouped_covid))

for region in region_names:
	grouped_regions.append(region)
	grouped_total_deaths.append(groups[(region)]["total_deaths_per_10k"].tolist()[-1])
	grouped_total_cases.append(groups[(region)]["total_cases_per_10k"].tolist()[-1])

final_df = pd.DataFrame()
final_df["region_name"] = grouped_regions
final_df["total_deaths_per_10k"] = grouped_total_deaths
final_df["total_cases_per_10k"] = grouped_total_cases

color_palette = sns.color_palette("Set2", n_colors=len(region_names))
plotly_color_palette = [f"rgb({int(color[0]*255)}, {int(color[1]*255)}, {int(color[2]*255)})"
                        for color in color_palette]
def regression(x, y):
	x = np.array(x).reshape(-1, 1)
	y = np.array(y)
	model = LinearRegression().fit(x, y)
	y_pred = model.predict(x)

	return y_pred


def make_correlation_plot(df, output_filename):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x = final_df["total_cases_per_10k"], y = final_df["total_deaths_per_10k"],
			  mode = 'markers',
			  name = 'total deaths per 10k people',
			  marker = dict( color = plotly_color_palette),
			  text = final_df["region_name"]))
	fig.add_trace(go.Scatter(x = final_df["total_cases_per_10k"], y = regression(final_df["total_cases_per_10k"], final_df["total_deaths_per_10k"]),
			  mode = 'lines',
			  name = 'linear regression line'))
			  	
	fig.update_layout(
    title="Correlation between total number of cases and deaths per 10 000 people in regions of Italy",
    xaxis_title="total number of cases per 10 000 people",
    yaxis_title="total number of deaths per 10 000 people")

	fig.update_traces(marker_size=10)
	fig.write_html(output_filename)

if __name__ == "__main__":
	make_correlation_plot(final_df, "../for_report/cases_vs_deaths.html")



