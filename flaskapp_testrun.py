
# def hello_world():
#  return "hello from kerry test 1"
# # register hops app as middleware
# app = Flask(__name__)
from flask import Flask
import ghhops_server as hs
from bs4 import BeautifulSoup

import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

html_doc = ""


@hops.component(
    "/pointat",
    name="PointAt",
    description="Get specific information from a website",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on curve at t")
    ],
)
def pointat(curve: rhino3dm.Curve, t):
    return curve.PointAt(t)


if __name__ == "__main__":
    app.run()
