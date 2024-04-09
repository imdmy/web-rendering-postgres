import pdal
import psycopg2

#span = 2 #分为2^1 * 2^1 * 2^1 的八叉树
span = 2 #分为2^1 * 2^1 的四叉树

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

pipeline_json = r"""[
    {
        "type": "readers.pgpointcloud",
        "connection": "host='192.168.228.50' dbname='postgres' user='test' password='123456' port='5432'",
        "table": "laoshan",  # 替换成实际的表名
        "column":"pa",
        "where":"id = 2"
    },
    {
        "type": "filters.info"
    }
]
"""

global_results = [] #保存查询结果

#执行sql语句返回结果
def execute_sql_query(queries, database="postgres", username="test", password="123456", host="192.168.228.50", port="5432"):
    try:
        # 建立与数据库的连接
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=password,
            host=host,
            port=port
        )

        # 创建游标对象
        cursor = conn.cursor()

        #顺序执行每条sql指令
        for query in queries:
            cursor.execute(query)
            if cursor.description:
                # 获取列名
                column_names = [desc[0] for desc in cursor.description]
                #print("列名称:", column_names)
            #rows = cursor.fetchall() #cursor.fetchall() 方法返回所有查询结果的行数据。
            rows = cursor.fetchone()[0] #cursor.fetchone()[0] 方法仅返回查询结果的第一行的第一个字段的值。

            #print("查询结果:", rows)
            global_results.append(float(rows)) #global_results.append(rows)
            #print("===========================================")  # 打印空行作为查询结果之间的分隔


    except psycopg2.Error as e:
        print("Error executing SQL query:", e)

    finally:
        # 关闭游标和连接
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_boundingbox(result): #返回中心点和边框大小值
    x_discrepancy = result[0] - result[1]
    y_discrepancy = result[2] - result[3]
    z_discrepancy = result[4] - result[5]
    x_middle = x_discrepancy/span
    y_middle = y_discrepancy/span
    z_middle = z_discrepancy/span

    print('边框：' + '  ' + str(x_discrepancy) + '   ' + str(y_discrepancy) + '   ' + str(z_discrepancy))
    print('中心点' + '  ' + str(x_middle) + '   ' + str(y_middle) + '   ' + str(z_middle))
    #return x_discrepancy, y_discrepancy, z_discrepancy, x_middle, y_middle, z_middle

# 调用函数并传入相应参数
sql_queries = [
   # "SELECT Count(*), Sum(PC_NumPoints(pa)) FROM laoshan400 l;",
    "SELECT PC_PatchMax(pa, 'x') FROM laoshan l;",
    "SELECT PC_PatchMin(pa, 'x') FROM laoshan l;",
    "SELECT PC_PatchMax(pa, 'y') FROM laoshan l;",
    "SELECT PC_PatchMin(pa, 'y') FROM laoshan l;",
    "SELECT PC_PatchMax(pa, 'z') FROM laoshan l;",
    "SELECT PC_PatchMin(pa, 'z') FROM laoshan l;"
]

execute_sql_query(sql_queries) #执行sql指令


get_boundingbox(global_results)






#print(global_results)
#print(global_results[0]-global_results[1])

