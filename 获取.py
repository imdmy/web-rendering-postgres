import pdal
import json
# 构建 PDAL 管道
pipeline = {
    "pipeline": [
        {
            "type": "readers.pgpointcloud",
            "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' port='5432'",
            "query": "(SELECT PC_AsText(PC_Explode(result)) AS exploded_result FROM (SELECT PC_Intersection(pa, 'SRID=4326;POLYGON((425412.86 3265875.98,427103.66 3265875.98,427103.66 3267250.81,425412.86 3267250.81,425412.86 3265875.98))'::geometry) AS result FROM laoshan)) AS q",
        },
        {
            "type": "writers.las",
            "filename": "C:\\Users\\Admin\\Desktop\\OctreeRender\\pointsave\\output.las"
        }
    ]
}

# 执行 PDAL 管道
pdal_pipeline = pdal.Pipeline(json.dumps(pipeline))
pdal_pipeline.execute()
