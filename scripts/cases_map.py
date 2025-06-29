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

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

covid = pd.read_csv("covid19_italy_regions.csv")
covid["total_positive_cases_per_10k"] = covid["total_positive_cases"]/(covid["region_population"]/10000)

months_years = covid["month_year"].unique()
region_names = covid["region_name"].unique()

grouped_covid = covid.groupby(["month_year", "region_name"])

groups = dict(list(grouped_covid))

grouped_months_years = []
grouped_regions = []
grouped_total_cases = []


for region in region_names:
    for month_year in months_years:
        grouped_months_years.append(month_year)
        grouped_regions.append(region)
        grouped_total_cases.append(groups[(month_year, region)]["total_positive_cases_per_10k"].tolist()[-1])


final_df = pd.DataFrame()
final_df["region_name"] = grouped_regions
final_df["month_year"] = grouped_months_years
final_df["total_positive_cases_per_10k"] = grouped_total_cases

counties = json.load(open("NUTS2_g.geojson"))

def plot_map(df):
    fig = px.choropleth_mapbox(df, geojson=counties, locations='region_name', featureidkey="properties.Nome", color='total_positive_cases_per_10k',
                            color_continuous_scale="Viridis",
                            range_color=(0, max(df["total_positive_cases_per_10k"])),
                            mapbox_style="carto-positron",
                            zoom=5.4, center = {"lat": 42.0902, "lon": 9.1129},
                            opacity=0.5,
                            labels = {'total_positive_cases_per_10k':'total cases per 10 000{}'.format(get_sub('2'))},
                            animation_frame = "month_year"
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.write_html("cases_map.html")
    fig.write_image("cases_map.png")


if __name__ == "__main__":
     plot_map(final_df)