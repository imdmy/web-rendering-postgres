import pdal
import psycopg2
import json


json_str = r"""
[
    {
        "type":"readers.pgpointcloud",
        "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' port='5432'",
        "table":"laoshan10000",
        "column":"pa",
        "where":"id = 2"
    },
    {
        "type":"writers.las",
        "filename":"C:\\Users\\Admin\\Desktop\\OctreeRender\\pointsave\\laoshan10000_1.las"
    }
]

"""

json_laoshan2pg = r"""
[
    {
        "type":"readers.las",
        "filename":"G:\\pointcloudsrc\\laoshan5.las"
    },
     {
         "type":"filters.chipper",
         "capacity":10000
     },
    {
        "type": "writers.pgpointcloud",
        "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' port='5432'",
        "table": "laoshan10000",
        "compression": "dimensional", 
        "srid": "4326",
        "pcid": "1"
    }
]

"""


pipeline_json = r"""[
    {
        "type": "readers.pgpointcloud",
        "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' 
        "table": "laoshan10000"  # 替换成实际的表名
    },
    {
        "type": "filters.info"
    }
]
"""

#pipeline = pdal.Pipeline(json=pipeline_json)
pipeline = pdal.Pipeline(pipeline_json)
count = pipeline.execute()   #执行管道，并返回总点数
arrays = pipeline.arrays  #获取处理后的点
metadata = pipeline.metadata #获取元数据
#log = pipeline.log  #获取执行日志
print(metadata)
print("当前子集的点数为:" + str(count))




# for i, point in enumerate(arrays[0]):
#     # 打印每个点的信息
#     print(f"Point {i + 1}:")
#     print(f"X: {point['X']}, Y: {point['Y']}, Z: {point['Z']}")
#     print(f"Intensity: {point['Intensity']}, ReturnNumber: {point['ReturnNumber']}, NumberOfReturns: {point['NumberOfReturns']}")
#     print(f"ScanDirectionFlag: {point['ScanDirectionFlag']}, EdgeOfFlightLine: {point['EdgeOfFlightLine']}, Classification: {point['Classification']}")
#     print(f"ScanAngleRank: {point['ScanAngleRank']}, UserData: {point['UserData']}, PointSourceId: {point['PointSourceId']}")
#     print(f"Red: {point['Red']}, Green: {point['Green']}, Blue: {point['Blue']}")
#     print(f"GpsTime: {point['GpsTime']}, Synthetic: {point['Synthetic']}, KeyPoint: {point['KeyPoint']}, Withheld: {point['Withheld']}, Overlap: {point['Overlap']}")
#     print("\n")
