import psycopg2
import psycopg2.extras
import xml.dom.minidom
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
# print (relations[0])
# Declare the writeInfoToXml function, which is used to generate the tag tag for OSM
def writeInfoToXml(points, ways, relations):
    doc = xml.dom.minidom.Document()
    osm = doc.createElement('osm')
    osm.setAttribute("version","0.6")
    doc.appendChild(osm)
    for point in points:
        node = doc.createElement('node')
        node.setAttribute("version","4")
        node.setAttribute("visible","true")
        node.setAttribute("id",str(point[0]))
        LonLat = point[4][6:-1].split(' ')
        node.setAttribute("lon",LonLat[0])
        node.setAttribute("lat",LonLat[1])
        if(point[1] == '1'):
            tag = doc.createElement('tag')
            tag.setAttribute("k","highway")
            tag.setAttribute("v","traffic_signals")
            node.appendChild(tag)
        osm.appendChild(node)

    for road in ways:
        way = doc.createElement('way')
        way.setAttribute("id",str(road[1]))
        way.setAttribute("version","4")
        way.setAttribute("visible","true")
        wayTag1 = doc.createElement('tag')
        wayTag2 = doc.createElement('tag')
        wayTag1.setAttribute("k","highway")
        wayTag1.setAttribute("v",road[2])
        wayTag2.setAttribute("k","oneway")
        wayTag2.setAttribute("v",road[3])
        way.appendChild(wayTag1)
        way.appendChild(wayTag2)


        ndSort = sorted(road[4], key=lambda i: int(i[1:-1].split(',')[1]))
        for n in ndSort:
            nd = doc.createElement('nd')
            nd.setAttribute('ref', n[1:-1].split(',')[0])
            way.appendChild(nd)
        osm.appendChild(way)

    for rela in relations:
        for r in rela[1]:
            if len(rela[1]) == 3:
                relation = doc.createElement('relation')
                member1 = doc.createElement('member')
                member2 = doc.createElement('member')
                member3 = doc.createElement('member')
                tag1 = doc.createElement('tag')
                tag2 = doc.createElement('tag')

                relation.setAttribute("id",str(rela[0]))
                relation.setAttribute("visible","true")
                relation.setAttribute("version","4")

                member1.setAttribute('type',"way")
                From = rela[1][0][1:-1].split(',')[1]
                To = rela[1][2][1:-1].split(',')[1]
                member1.setAttribute('ref',From)
                member1.setAttribute('role',"from")
                curor = conn.cursor()
                curor.execute('select node_id from anheb where node_lid like \'%' + From + '%\' and node_lid like \'%' + To + '%\';')
                Via = curor.fetchall()
                member2.setAttribute('type', "node")
                member2.setAttribute('ref',Via[0][0])
                member2.setAttribute('role', "via")

                member3.setAttribute('type', "way")
                member3.setAttribute('ref',To)
                member3.setAttribute('role', "to")

                tag1.setAttribute("k","restriction")
                deg = rela[1][2][1:-1].split(',')[2]
                if deg < 45 or deg >= 315:
                    tag1.setAttribute("v","no_u_turn")
                elif deg >=45 or deg < 135:
                    tag1.setAttribute("v", "no_left_turn")
                elif deg >= 135 or deg <= 225:
                    tag1.setAttribute("v", "no_straight_on")
                elif deg >= 225 or deg < 315:
                    tag1.setAttribute("v", "no_right_on")
                tag2.setAttribute("k","type")
                tag2.setAttribute("v","restriction")
                relation.appendChild(member1)
                relation.appendChild(member2)
                relation.appendChild(member3)
                relation.appendChild(tag1)
                relation.appendChild(tag2)
            elif len(rela[1]) == 4:
                relation = doc.createElement('relation')
                member1 = doc.createElement('member')
                member2 = doc.createElement('member')
                member3 = doc.createElement('member')
                tag1 = doc.createElement('tag')
                tag2 = doc.createElement('tag')
                relation.setAttribute("id",str(rela[0]))
                relation.setAttribute("version","4")
                relation.setAttribute("visible","true")

                member1.setAttribute('type', "way")
                member1.setAttribute('ref', rela[1][0][1:-1].split(',')[1])
                member1.setAttribute('role', "from")

                member2.setAttribute('type', "way")
                member2.setAttribute('ref', rela[1][2][1:-1].split(',')[1])
                member2.setAttribute('role', "via")

                member3.setAttribute('type', "way")
                member3.setAttribute('ref', rela[1][3][1:-1].split(',')[1])
                member3.setAttribute('role', "to")

                tag1.setAttribute("k", "restriction")
                # print(int(rela[1][2][1:-1].split(',')[2]),int(rela[1][3][1:-1].split(',')[2]))
                deg = int(rela[1][2][1:-1].split(',')[2]) + int(rela[1][3][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    tag1.setAttribute("v", "no_u_turn")
                elif deg >= 45 or deg < 135:
                    tag1.setAttribute("v", "no_left_turn")
                elif deg >= 135 or deg <= 225:
                    tag1.setAttribute("v", "no_straight_on")
                elif deg >= 225 or deg < 315:
                    tag1.setAttribute("v", "no_right_on")

                tag2.setAttribute("k", "type")
                tag2.setAttribute("v", "restriction")

                relation.appendChild(member1)
                relation.appendChild(member2)
                relation.appendChild(member3)
                relation.appendChild(tag1)
                relation.appendChild(tag2)
            elif len(rela[1]) == 5:
                relation = doc.createElement('relation')
                member1 = doc.createElement('member')
                member2 = doc.createElement('member')
                member3 = doc.createElement('member')
                tag1 = doc.createElement('tag')
                tag2 = doc.createElement('tag')

                relation.setAttribute("id",str(rela[0]))
                relation.setAttribute("version","4")
                relation.setAttribute("visible","true")

                member1.setAttribute('type', "way")
                member1.setAttribute('ref', rela[1][2][1:-1].split(',')[1])
                member1.setAttribute('role', "from")

                member2.setAttribute('type', "way")
                member2.setAttribute('ref', rela[1][3][1:-1].split(',')[1])
                member2.setAttribute('role', "via")

                member3.setAttribute('type', "way")
                member3.setAttribute('ref', rela[1][4][1:-1].split(',')[1])
                member3.setAttribute('role', "to")

                tag1.setAttribute("k", "restriction")
                deg = int(rela[1][3][1:-1].split(',')[2]) + int(rela[1][4][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    tag1.setAttribute("v", "no_u_turn")
                elif deg >= 45 or deg < 135:
                    tag1.setAttribute("v", "no_left_turn")
                elif deg >= 135 or deg <= 225:
                    tag1.setAttribute("v", "no_straight_on")
                elif deg >= 225 or deg < 315:
                    tag1.setAttribute("v", "no_right_on")

                tag2.setAttribute("k", "type")
                tag2.setAttribute("v", "restriction")
                relation.appendChild(member1)
                relation.appendChild(member2)
                relation.appendChild(member3)
                relation.appendChild(tag1)
                relation.appendChild(tag2)
            elif len(rela[1]) == 6:
                relation = doc.createElement('relation')
                member1 = doc.createElement('member')
                member2 = doc.createElement('member')
                member3 = doc.createElement('member')
                tag1 = doc.createElement('tag')
                tag2 = doc.createElement('tag')

                relation.setAttribute("id",str(rela[0]))
                relation.setAttribute("version","4")
                relation.setAttribute("visible","true")

                member1.setAttribute('type', "way")
                member1.setAttribute('ref', rela[1][2][1:-1].split(',')[1])
                member1.setAttribute('role', "from")

                member2.setAttribute('type', "way")
                member2.setAttribute('ref', rela[1][3][1:-1].split(',')[1])
                member2.setAttribute('role', "via")

                member3.setAttribute('type', "way")
                member3.setAttribute('ref', rela[1][4][1:-1].split(',')[1])
                member3.setAttribute('role', "to")

                tag1.setAttribute("k", "restriction")
                deg = int(rela[1][3][1:-1].split(',')[2]) + int(rela[1][4][1:-1].split(',')[2]) - 180
                if deg < 45 or deg >= 315:
                    tag1.setAttribute("v", "no_u_turn")
                elif deg >= 45 or deg < 135:
                    tag1.setAttribute("v", "no_left_turn")
                elif deg >= 135 or deg <= 225:
                    tag1.setAttribute("v", "no_straight_on")
                elif deg >= 225 or deg < 315:
                    tag1.setAttribute("v", "no_right_on")

                tag2.setAttribute("k", "type")
                tag2.setAttribute("v", "restriction")

                relation.appendChild(member1)
                relation.appendChild(member2)
                relation.appendChild(member3)
                relation.appendChild(tag1)
                relation.appendChild(tag2)
            else:
                continue
        osm.appendChild(relation)

    # open hlj.osm file
    fo = open("hlj.osm", 'w')
    # Insert the written label into the OSM file
    fo.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    fo.close()
    return

writeInfoToXml(points,ways,relations)
