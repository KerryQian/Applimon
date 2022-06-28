
from flask import Flask, request
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/np_addMatrix",
    name="np_addMatrix",
    description="np_addMatrix",
    inputs=[
        hs.HopsNumber("M1", "M1", "M1", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("M2", "M2", "M2", access=hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("M3", "M3", "M3")
    ]
)
@app.route('/urlend')
def np_addMatrix(M1, M2):
    import numpy as np
    # import json
    # import pandas as pd
    # args = request.args
    # variables = dict(args)
    # variables["m1"] = variables["m1"].split(",")
    # variables["m2"] = variables["m2"].split(",")

    # variables["m1"] = list(map(lambda x: float(x), variables["m1"]))
    # variables["m2"] = list(map(lambda x: float(x), variables["m2"]))

    # matrix1 = np.array(variables["m1"]).reshape(
    #     (int(variables["m1_y"]), int(variables["m1_x"])))
    # matrix2 = np.array(variables["m2"]).reshape(
    #     (int(variables["m2_y"]), int(variables["m2_x"])))

    # # Actual Function
    # result = np.add(matrix1, matrix2)

    # # Serialisation
    # data = pd.DataFrame(result)
    # data.to_csv()

    # return str(data)
    matrix1 = np.array(M1).reshape((2, 2))
    matrix2 = np.array(M2).reshape((2, 2))

    result = np.add(matrix1, matrix2)
    result = result.flatten()
    print(result)
    return list(result)


# def main():
#     app.run()


if __name__ == "__main__":
    app.run()
