# Water Reserves Europe - Visualization Final Project SoSe2022 - Carlos Andres Poveda - 123802

This project is the final presentation of the subject Visualization SoSe2022 Bauhaus-Universität Weimar

This project runs with [Flask](http://flask.pocoo.org) application and use [Altair](https://altair-viz.github.io/index.html) to generate [D3](https://d3js.org) charts using [Vega](https://vega.github.io/vega/) grammar. Using Flask framework and the Altair library makes relatively easy to create D3 visualization without writing any client side code. Besides, the mouse over effect is powered by [Vega-tooltip](https://github.com/vega/vega-tooltip).

## Deployment

It is highly recommended to work with an python environment [Python Env](https://docs.python.org/3/library/venv.html).

1. `git clone https://github.com/krpovmu/visualization-final.git`
1. `cd visualization-final`
1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python ./app.py`

Visit http://localhost:5000 in your browser, that's it!

## Deployment with Docker

You can deploy and run the application locally using [Docker](https://www.docker.com/).

1. `docker build -t flask_app .`
1. `docker run --init --rm -d --publish 127.0.0.1:5000:5000 flask_app`

Once running, visit `localhost:5000` on your web browser. 

