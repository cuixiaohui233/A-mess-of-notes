import psycopg2
import psycopg2.extras
import xml.dom.minidom
import sys
import os

# read database
conn = psycopg2.connect("dbname=postgis_test user=kong")
# get cursor
cur = conn.cursor()
# Execute the SQL statement by execute
cur.execute('SELECT gid, light_flag, z, node_id, st_astext((ST_DumpPoints(geom)).geom) from anheb;')
# print(cur.fetchall())

# The query result is assigned to the variable points by the fetchall method
points = cur.fetchall()
# print (points)
# Declare the writeInfoToXml function, which is used to generate the tag tag for OSM
def writeInfoToXml(points):
    doc = xml.dom.minidom.Document()
    osm = doc.createElement('osm')
    osm.setAttribute("version","0.6")
    doc.appendChild(osm)
    for point in points:
        node = doc.createElement('node')
        node.setAttribute("version","4")
        node.setAttribute("visible","true")
        node.setAttribute("id",str(point[0]))
        node.setAttribute("lat",point[4][6:22])
        node.setAttribute("lon",point[4][23:39])
        if(point[1] == '1'):
            tag = doc.createElement('tag')
            tag.setAttribute("k","highway")
            tag.setAttribute("v","traffic_signals")
            node.appendChild(tag)
        osm.appendChild(node)

    # open hlj.osm file
    fo = open("hlj.osm", 'w')
    # Insert the written label into the OSM file
    fo.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    return

writeInfoToXml(points)
