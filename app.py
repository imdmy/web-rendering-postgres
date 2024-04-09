from flask import Flask, render_template, Response
import json
import numpy as np
import io
import pdal


app = Flask(__name__)


json_str = r"""
[
    {
        "type":"readers.pgpointcloud",
        "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' port='5432'",
        "table":"laoshan_triangle",
        "column":"pa",
        "where":"id = 3"
    }
]

"""




pipeline = pdal.Pipeline(json_str)
count = pipeline.execute()  #返回总点数
arrays = pipeline.arrays #获取处理后的点
#metadata = pipeline.metadata
#log = pipeline.log #获取执行日志
print("当前子集的点数为:" + str(count))




@app.route('/')
def index():
    return render_template('index.html')

def generate_point_cloud():
    # 获取点云数据
    points = arrays[0]

    # 提取坐标信息
    x = points['X']
    y = points['Y']
    z = points['Z']

    # 将坐标数据转换为JSON格式
    data = json.dumps({'x': x.tolist(), 'y': y.tolist(), 'z': z.tolist()})

    yield f"data:{data}\n\n"

@app.route('/pointcloud')
def point_cloud():
    return Response(generate_point_cloud(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
