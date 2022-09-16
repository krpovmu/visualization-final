from flask import Flask, render_template
import altair as alt
import pandas as pd

app = Flask(__name__)

def read_data(filename):
    return pd.read_csv(filename,skipinitialspace=True) 

# Flask routes
# render index.html home page
@app.route("/")
def index():
    return render_template('index.html')

# Altair Data Routes

FILE_WATER='./data/renewable_internal_freshwater_resources_europe.csv'
FILE_TEMP='./data/temperature_mean_europe_1990-2020.csv'
FILE_POPULA='./data/porcentage_population_cities_rural_1990-2018.csv'
FILE_PRECIPI='./data/average_precipitation_in_depth_europe_1992-2018.csv'

@app.route("/data/waterfall")
def data_waterfall():
    water_data = read_data(FILE_WATER)
    meltdata = water_data.melt(id_vars=['country'])

    input_dropdown = alt.binding_select(options=['1992','1997','2002','2007',
                         '2012','2017','2018'], name='Year')

    selection = alt.selection_single(fields=['variable'],bind=input_dropdown)

    chart = alt.Chart(meltdata).mark_bar(color='seagreen', opacity=0.6).encode(
            alt.X('value:Q', title="Total Water (billion cubic meters)"),
            alt.Y('country:N', title="Country", sort=None),
            tooltip = [alt.Tooltip('value',title="Total Water"),
            alt.Tooltip('country',title="Country"),
            alt.Tooltip('variable',title="Year")]
    ).add_selection(
            selection
    ).transform_filter(
            selection
    ).properties(
            width=800,
            height=800,
            title="Renewable internal freshwater resources")

    return chart.to_json()

@app.route("/data/line")
def data_line():
    temp_data = read_data(FILE_TEMP)
    meltdata = temp_data.melt(id_vars=['year'])

    chart = alt.Chart(meltdata,title="Temperature Mean Europe 1990 - 2020").mark_rect().encode(
            x=alt.X('year:N', title="Year"),
            y=alt.Y('variable:N', title="Month", sort=None),
            color=alt.Color('value:Q', title="Temperature", scale=alt.Scale(scheme='goldred')),
            tooltip = [alt.Tooltip('year',title="Year"),
                alt.Tooltip('variable', title="Month"),
                alt.Tooltip('value',title="Temp")]
    ).properties(
            width=800,
            height=400
    )

    return chart.to_json()

@app.route("/data/multiline")
def data_multiline():
    pop_data = read_data(FILE_POPULA)
    meltdata = pop_data.melt(id_vars=['year'])

    chart = alt.Chart(meltdata).mark_line().encode(
        alt.X('year:O', title='Year'),
        alt.Y('value:Q', title='Percentage of people'),
        alt.Color('variable:N', title="Key", scale=alt.Scale(scheme='goldred')),
        tooltip = [alt.Tooltip('year',title="Year"),
            alt.Tooltip('value',title="% people")],
    ).properties(
            width=800,
            height=400,
            title="Share of European population living in rural or urban areas with grow rate percentage"
    )

    return chart.to_json()

@app.route("/data/stocks")
def stocks():
    pre_data = read_data(FILE_PRECIPI)
    meltdata = pre_data.melt(id_vars=['countries']) 

    chart = alt.Chart(meltdata).mark_point(filled=True).encode(
        alt.X('variable:N', title="Year"),
        alt.Y('value:Q', title="Value in mm"),
        alt.Size('value'),
        alt.Color('countries:N',scale=alt.Scale(scheme='category20')),
        alt.OpacityValue(0.7),
        tooltip = [alt.Tooltip('value',title="% precipit"),
             alt.Tooltip('countries',title="Country"),
             alt.Tooltip('variable',title="Year")]
    ).properties(
     width=500,
     height=500,
     title="Europe's average precipitation in depth (mm per year)"
    ).interactive()

    return chart.to_json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
