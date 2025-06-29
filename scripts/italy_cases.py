#!/usr/bin/env python3
import datetime

from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import plotly.express as px


def plot_cases_and_deaths(df):
	ymax = 400
	ymin = min(df["new_positive_cases_per_100k"])
	ylim = [ymin*.95, ymax*1.05]
	xmin = "2020-02-24"
	xmax = "2023-04-01"
	fig = px.bar(df, x="date", y="new_positive_cases_per_100k",  width=1000, height=600)
	fig.update_layout(
    title="Daily Covid-19 cases in Italy per 100k people",
    xaxis_title="date",
    yaxis_title="daily positive cases per 100k people",
    yaxis=dict(range=[ylim[0],ylim[1]]),
    xaxis = dict(range = [xmin, xmax]),
    font=dict(
        size=12,
		color='black'
    ))
	fig.update_xaxes(
    tickmode='linear',
    tickformat='%Y-%m-%d',
    tickangle=45,
    dtick='M1'
	)

	fig.update_traces(marker_color='black')

	fig.add_shape(
		type = "rect",
		x0 = "2020-02-24",
		y0 = ylim[0],
		x1="2020-03-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "lightblue",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2020-03-01",
		y0 = ylim[0],
		x1="2020-05-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "green",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2020-05-01",
		y0 = ylim[0],
		x1="2020-09-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "yellow",
		opacity = 0.15,
	)


	fig.add_shape(
		type = "rect",
		x0 = "2020-09-01",
		y0 = ylim[0],
		x1="2020-12-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "orange",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2020-12-01",
		y0 = ylim[0],
		x1="2021-03-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "lightblue",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2021-03-01",
		y0 = ylim[0],
		x1="2021-05-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "green",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2021-05-01",
		y0 = ylim[0],
		x1="2021-09-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "yellow",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2021-09-01",
		y0 = ylim[0],
		x1="2021-12-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "orange",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2021-12-01",
		y0 = ylim[0],
		x1="2022-03-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "lightblue",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2022-03-01",
		y0 = ylim[0],
		x1="2022-05-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "green",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2022-05-01",
		y0 = ylim[0],
		x1="2022-09-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "yellow",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2022-09-01",
		y0 = ylim[0],
		x1="2022-12-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "orange",
		opacity = 0.1,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2022-12-01",
		y0 = ylim[0],
		x1="2023-03-01",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "lightblue",
		opacity = 0.15,
	)

	fig.add_shape(
		type = "rect",
		x0 = "2023-03-01",
		y0 = ylim[0],
		x1="2023-04-10",
		y1 = ylim[1],
		line_width = 0,
		fillcolor = "green",
		opacity = 0.1,
	)

	fig.write_html("../for_report/italy_cases.html")
	fig.write_image("../for_poster/italy_cases.png")


covid = pd.read_csv("../data/covid19_italy.csv")
covid["new_positive_cases_per_100k"] = covid["new_positive_cases"]/(59110000/100000)
if __name__ == "__main__":
	plot_cases_and_deaths(covid)