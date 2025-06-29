#!/usr/bin/env python3

import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import argparse

covid = pd.read_csv("covid19_italy_regions.csv")
covid["density"] = covid["region_population"]/covid["region_area"]
covid = covid.sort_values(by = "density")

def plot_density(df):
	
	fig = px.bar(df, x = "region_name", y="density", color = "region_name")
	# fig.update_layout(
    # title="Total positive Covid-19 cases vs total recoveries in Italy",
    # xaxis_title="date",
    # yaxis_title="total positive cases",
    # font=dict(
    #     family="Courier New, monospace",
    #     size=18,
	# 	color='black'
    # ))
	fig.write_html("density_regions.html")


#separate years subplots

plot_density(covid)