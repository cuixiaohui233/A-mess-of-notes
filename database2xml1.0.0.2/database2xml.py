import psycopg2
import psycopg2.extras
# import xml.dom.minidom
import sys
import os

# read database
conn = psycopg2.connect("dbname=postgis_test user=kong")
# get cursor
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()
# Execute the SQL statement by execute
cur.execute('SELECT gid, light_flag, z, node_id, st_astext((ST_DumpPoints(geom)).geom) from anheb;')
cur1.execute('SELECT * from arheb;')
cur2.execute('SELECT id, ways from relheb;')

# print(cur.fetchall())

# The query result is assigned to the variable points by the fetchall method
points = cur.fetchall()
ways = cur1.fetchall()
relations = cur2.fetchall()
# print (ways)
# Declare the writeInfoToXml function, which is used to generate the tag tag for OSM
def writeInfoToXml(points, ways, relations):
    fo = open("hlj.osm", 'w+')
    # Insert the written label into the OSM file
    xml = '<?xml version="1.0" encoding="utf-8"?>'
    osm = '<osm version="0.6">'
    fo.write(xml)
    fo.write(osm)

    for point in points:
        node = '<node id="'+ str(point[0]) +'" lat="'+point[4][6:-1].split(' ')[1]+'" lon="'+point[4][6:-1].split(' ')[0]+'" version="4" visible="true"/>'

        if(point[1] == '1'):
            node = node[0:-2]
            node += '><tag k="highway" v="traffic_signals"/></node>'
        fo.write(node)
    #
    for road in ways:
        ndSort = sorted(road[4], key=lambda i: int(i[1:-1].split(',')[1]))
        way = '<way id="'+str(road[1])+'" version="4" visible="true"><tag k="highway" v="'+road[2]+'"/><tag k="oneway" v="'+road[3]+'"/>'
        for n in ndSort:
            way += '<nd ref="'+n[1:-1].split(',')[0]+'"/>'
        way += '</way>'
        fo.write(way)

    for rela in relations:
        # print(rela[0])
        for r in rela[1]:
            if len(rela[1]) == 3:
                From = rela[1][0][1:-1].split(',')[1]
                To = rela[1][2][1:-1].split(',')[1]
                curor = conn.cursor()
                curor.execute(
                    'select gid from anheb where node_lid like \'%' + From + '%\' and node_lid like \'%' + To + '%\';')
                Via = curor.fetchall()
                relation = '<relation id="'+str(rela[0])+'" version="4" visible="true"><member ref="'+From+'" role="from" type="way"/><member ref="'+str(Via[0][0])+'" role="via" type="way"/><member ref="'+To+'" role="to" type="way"/>'

                deg = rela[1][2][1:-1].split(',')[2]
                if deg < 45 or deg >= 315:
                    relation += '<tag k="restriction" v="no_u_turn"/>'
                elif deg >= 45 or deg < 135:
                    relation += '<tag k="restriction" v="no_left_turn"/>'
                elif deg >= 135 or deg <= 225:
                    relation += '<tag k="restriction" v="no_straight_on"/>'
                elif deg >= 225 or deg < 315:
                    relation += '<tag k="restriction" v="no_right_on"/>'

                relation += '<tag k="type" v="restriction"/></relation>'
                fo.write(relation)
            elif len(rela[1]) == 4:
                relation = '<relation id="'+str(rela[0])+'" version="4" visible="true"><member ref="'+rela[1][0][1:-1].split(',')[1]+'" role="from" type="way"/><member ref="'+rela[1][2][1:-1].split(',')[1]+'" role="via" type="way"/><member ref="'+rela[1][3][1:-1].split(',')[1]+'" role="to" type="way"/>'
                deg = int(rela[1][2][1:-1].split(',')[2]) + int(rela[1][3][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    relation += '<tag k="restriction" v="no_u_turn"/>'
                elif deg >= 45 or deg < 135:
                    relation += '<tag k="restriction" v="no_left_turn"/>'
                elif deg >= 135 or deg <= 225:
                    relation += '<tag k="restriction" v="no_straight_on"/>'
                elif deg >= 225 or deg < 315:
                    relation += '<tag k="restriction" v="no_right_on"/>'

                relation += '<tag k="type" v="restriction"/></relation>'
                fo.write(relation)

            elif len(rela[1]) == 5:
                relation = '<relation id="' + str(rela[0]) + '" version="4" visible="true"><member ref="' + rela[1][2][1:-1].split(',')[1] + '" role="from" type="way"/><member ref="' + rela[1][3][1:-1].split(',')[1] + '" role="via" type="way"/><member ref="' + rela[1][4][1:-1].split(',')[1] + '" role="to" type="way"/>'
                deg = int(rela[1][2][1:-1].split(',')[2]) + int(rela[1][3][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    relation += '<tag k="restriction" v="no_u_turn"/>'
                elif deg >= 45 or deg < 135:
                    relation += '<tag k="restriction" v="no_left_turn"/>'
                elif deg >= 135 or deg <= 225:
                    relation += '<tag k="restriction" v="no_straight_on"/>'
                elif deg >= 225 or deg < 315:
                    relation += '<tag k="restriction" v="no_right_on"/>'

                relation += '<tag k="type" v="restriction"/></relation>'
                fo.write(relation)

            elif len(rela[1]) == 6:
                relation = '<relation id="' + str(rela[0]) + '" version="4" visible="true"><member ref="' + rela[1][2][1:-1].split(',')[1] + '" role="from" type="way"/><member ref="' + rela[1][3][1:-1].split(',')[1] + '" role="via" type="way"/><member ref="' + rela[1][4][1:-1].split(',')[1] + '" role="to" type="way"/>'
                deg = int(rela[1][2][1:-1].split(',')[2]) + int(rela[1][3][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    relation += '<tag k="restriction" v="no_u_turn"/>'
                elif deg >= 45 or deg < 135:
                    relation += '<tag k="restriction" v="no_left_turn"/>'
                elif deg >= 135 or deg <= 225:
                    relation += '<tag k="restriction" v="no_straight_on"/>'
                elif deg >= 225 or deg < 315:
                    relation += '<tag k="restriction" v="no_right_on"/>'

                relation += '<tag k="type" v="restriction"/></relation>'
                fo.write(relation)
            else:
                continue

    fo.write('</osm>')

    fo.close()

writeInfoToXml(points,ways,relations)
