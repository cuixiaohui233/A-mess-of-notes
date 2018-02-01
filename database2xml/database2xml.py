import psycopg2
import psycopg2.extras
import xml.dom.minidom
import sys
import os

# 读取数据库
conn = psycopg2.connect("dbname=postgis_test user=kong")
# 获取 cursor 对象
cur = conn.cursor()
# 通过 execute 来执行 SQL 语句
cur.execute('SELECT id,st_astext((ST_DumpPoints(geom)).geom) from z_levelheilongjiang;')
# print(cur.fetchall());

# 通过 fetchall 方法来讲查询结果赋值给变量 points
points = cur.fetchall();

# 声明 writeInfoToXml 函数，用来生成 osm 的 tag 标签
def writeInfoToXml(points):
    doc = xml.dom.minidom.Document()
    osm = doc.createElement('osm')
    osm.setAttribute("version","0.6")
    doc.appendChild(osm)
    for point in points:
        node = doc.createElement('node')
        node.setAttribute("id",point[0])
        node.setAttribute("lat",point[1][6:22])
        node.setAttribute("lon",point[1][23:39])
        osm.appendChild(node)

    # 打开准备好的 hlj.osm 的文件
    fo = open("hlj.osm", 'w')
    # 将写好的标签插入到 osm 文件中
    fo.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    return

writeInfoToXml(points)
