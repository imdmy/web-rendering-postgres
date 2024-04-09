from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mock point cloud data
point_cloud_data = [
    {"x": 1.0, "y": 2.0, "z": 3.0},
    {"x": 4.0, "y": 5.0, "z": 6.0},
    # Add more points here
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/point_cloud_data')
def get_point_cloud_data():
    return jsonify(point_cloud_data)

if __name__ == '__main__':
    app.run(debug=True)
