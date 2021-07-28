from re import L, T
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import osmnx as ox

import numpy as np
import matplotlib.pyplot as plt

def read_txt_column(data_name,f_row='delete'):
    data=open(data_name)
    result=[]
    for line in data.readlines():
        a=line.split(',')
        result.append(a)
    if f_row=='delete':
        del result[0]
    result_array=np.array(result,dtype=float)
    return result_array

bsm_file = "./x_y_bsm.txt"
sanitized_bsm_file="./x_y_bsm_sanitized.txt"
data_bsm = read_txt_column(bsm_file)
sanitized_bsm = read_txt_column(sanitized_bsm_file)

x = data_bsm[:,0]
y = data_bsm[:,1]
s_x = sanitized_bsm[:,0]
s_y = sanitized_bsm[:,1]


plt.ion()
G_pro=joblib.load('NTU_project_map_filled.pkl')
fig,ax=ox.plot_graph(G_pro,show=False,close=False,node_color='#16d2d9', bgcolor="#ffffff")

ax.scatter(x[0],y[0], s=60, label='Start', c='y')
plt.pause(1)
ax.scatter(s_x[0],s_y[0], s=60, label='EKF Start', c='g')
ax.legend(loc='best')
plt.pause(3)

for i in range(len(x)//5):
    ax.set_title('Driver behavior: Normal')
    ax.scatter(x[5*i],y[5*i], s=50, label='GPS Measurements', c='r',marker='+')
    plt.pause(0.001)
    ax.scatter(s_x[5*i],s_y[5*i],s=50, label='EKF Position', c='k', marker='+')
    if i==0:
        plt.pause(2)
        ax.legend(loc='best')
    plt.pause(0.001)

ax.scatter(s_x[-1],s_y[-1], s=60, label='EKF Goal', c='r') 
ax.scatter(x[-1],y[-1], s=60, label='Goal', c='b')
ax.legend(loc='best')
plt.pause(2)


app=Flask(__name__)

# model = pickle.load(open('generate_video.py'))

# @app.route('/')

# def home(): 
#     return render_template('index.html')

# @app.route('/predict', methods = ['POST'])
# def predict():
#     int_features = [x for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('index.html', prediction_text = 'Salary is {}'.format(output))

# @app.route('/predict_api', methods = ['POST'])

# def predict_api():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.aray(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

#example code for matplotlib:
# from flask import render_template
import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route("/mysuperplot", methods=["GET"])
def plotView():

    # Generate plot
    # fig = Figure()
    # axis = fig.add_subplot(1, 1, 1)
    # axis.set_title("title")
    # axis.set_xlabel("x-axis")
    # axis.set_ylabel("y-axis")
    # axis.grid()
    # axis.plot(range(5), range(5), "ro-")
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("image.html", image=pngImageB64String)


if __name__ == "__main__":
    app.run(debug=True)