1.安装Postgis
  首先安装 PosgreSQL
  
  `brew install postgres`
  
  默认情况下会安装在 `/usr/local/var/postgres` 目录下
  
  然后安装postgis
  
  `brew install postgis`
2.启动 PosgreSQL
  `pg_ctl -D /usr/local/var/postgres start`
  （在本机上是`pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`）
  检查一下 postgres 是否启动成功
  `export PGDATA='/usr/local/var/postgres'`
  `pg_ctl status`
  如果你看到：
  ![IMAGE](resources/698A56F561A68248AD5151A6D2ED5AA1.jpg =587x36)
  证明成功！！
3.新建一个数据库
  如果是新安装的，那我们需要初始化
  `initdb /usr/local/var/postgres`
  然后我们创建一个数据库，我们叫postgis_test
  `createdb postgis_test`
  我们将使用psql命令行实用程序连接到我们刚刚创建的数据库：
  如果我们成功连接的话，那么会看到如下结果
  `psql postgis_test`
  ![IMAGE](resources/008E4DD77D55C858714EA276FF3FFDDC.jpg =218x77)
  要启用PostGIS，请执行以下命令：
  `CREATE EXTENSION postgis;`
  你会看到：
  ![IMAGE](resources/A0B303A84D49D00A9773450848956FFD.jpg =306x59)
  我们来看看是否有PostGIS支持：
  `SELECT PostGIS_Version();`
  如果你要退出的话：
  `\q`
  
4.shp2pgsql向postgresql导入shape数据
  1. 准备好Shape文件（不仅仅是.shp文件，还要有其他相关数据文件，包括.shx、.prj、.dbf文件）。
  2. 使用命令将Shape数据转换为*.sql文件:
  `shp2pgsql -s 3857 -c -W "GBK" xxx.shp>xxx.sql`
  3.向数据库导入使用Shape数据生成的.sql文件
  `psql -d shp2pgsqldemo -U 当前用户 -f /tmp/shp/生成好的.sql文件 -W`
  4.不出意外，可以在数据库中看到导入的.shp文件