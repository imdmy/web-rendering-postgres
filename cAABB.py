import pdal
import json

# 获取 PDAL 版本信息
pdal_version = pdal.__version__

# 输出 PDAL 版本信息
print("PDAL 版本:", pdal_version)


# 读取点云文件并获取信息
pipeline = {
    "pipeline": [
        {
            "type": "readers.las",
            "filename": "G:\\pointcloudsrc\\laoshan5.las"
        },
        {
            "type": "filters.stats"
        }
    ]
}

# 创建 PDAL Pipeline 对象
pipeline_obj = pdal.Pipeline(json.dumps(pipeline))

# 执行 Pipeline
pipeline_obj.execute()

# 获取点云信息
metadata = pipeline_obj.metadata

# 检查是否存在 'filters.stats' 键
if "filters.stats" in metadata:
    stats = metadata["filters.stats"]

    # 打印点云信息
    print("点云信息：")
    print(f"点的数量: {stats['pointcount']}")
    print(f"X 范围: {stats['bbox']['native']['minx']} - {stats['bbox']['native']['maxx']}")
    print(f"Y 范围: {stats['bbox']['native']['miny']} - {stats['bbox']['native']['maxy']}")
    print(f"Z 范围: {stats['bbox']['native']['minz']} - {stats['bbox']['native']['maxz']}")
else:
    print("未找到 'filters.stats' 信息")

