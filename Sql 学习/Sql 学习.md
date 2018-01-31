### 1.声明一个 sql 语句
  SELECT *
  FROM
  数据表
  WHERE 限制条件</br>
### 2.ORDER BY 排序
### 3.JOIN
  用于根据两个或多个表中的列之间的关系，从这些表中查询数据。
  SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
  FROM Persons
  INNER JOIN Orders
  ON Persons.Id_P = Orders.Id_P
  ORDER BY Persons.LastName</br>
### 4.JOIN: 如果表中有至少一个匹配，则返回行
  LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
  RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
  FULL JOIN: 只要其中一个表中存在匹配，就返回行
  INNER JOIN: 在表中存在至少一个匹配时，INNER JOIN 关键字返回行。INNER JOIN 与 JOIN 是相同的。</br>
### 5.UNION
  UNION 操作符用于合并两个或多个 SELECT 语句的结果集。</br>
  请注意，UNION 内部的 SELECT</br> 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。</br>
  `SELECT column_name(s) FROM table_name1
  UNION
  SELECT column_name(s) FROM table_name2`  
  例子：</br>
  下面的例子中使用的原始表:</br>
  Employees_China:</br>
  
  | E_ID |	E_Name |
  | ----- | -----: |
  | 01 |	Zhang, Hua |
  | 02 |	Wang, Wei |
  | 03 |	Carter, Thomas |
  |04 |	Yang, Ming |
  
  Employees_USA:</br>
  
  | E_ID |	E_Name |
  | ---- | ---- |
  | 01	| Adams, John |
  | 02	| Bush, George |
  | 03	| Carter, Thomas |
  | 04	| Gates, Bill |
  
  使用UNION命令</br>
  列出所有在中国和美国的不同的雇员名：</br>
  
  `SELECT E_Name FROM Employees_China
  UNION
  SELECT E_Name FROM Employees_USA`
  
  得出的结果：</br>
  
  |E_Name|
  |----|
  |Zhang, Hua|
  |Wang, Wei|
  |Carter, Thomas|
  |Yang, Ming|
  |Adams, John|
  |Bush, George|
  |Gates, Bill|
  
  这个命令无法列出在中国和美国的所有雇员。在上面的例子中，我们有两个名字相同的雇员，他们当中只有一个人被列出来了。UNION 命令只会选取不同的值。</br>
  
  而使用 UNION ALL 就可以：</br>
  
  `SELECT E_Name FROM Employees_China
  UNION
  SELECT E_Name FROM Employees_USA`
  
  得出的结果：</br>
  
  |E_Name|
  |----|
  |Zhang, Hua|
  |Wang, Wei|
  |Carter, Thomas|
  |Yang, Ming|
  |Adams, John|
  |Bush, George|
  |Carter, Thomas|
  |Gates, Bill|

### 6.TOP 子句
  TOP 子句用于规定要返回的记录的数目。</br>
  对于拥有数千条记录的大型表来说，TOP 子句是非常有用的。</br>
  注释：并非所有的数据库系统都支持 TOP 子句。</br>
  例子：</br>
  原始的表：</br>
  Persons 表:
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1|	Adams	|John|	Oxford Street|	London|
  |2|	Bush|	George|	Fifth Avenue|	New York|
  |3|	Carter|	Thomas|	Changan Street|	Beijing|
  |4|	Obama	Barack|	Pennsylvania Avenue|	Washington|
  
  使用 TOP 去的表的前两项：</br>
  
  `SELECT TOP 2 * FROM Persons`
  
  得出的结果：
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1|Adams|	John	|Oxford Street	|London|
  |2|	Bush|	George|	Fifth Avenue|	New York|

  现在，我们希望从上面的 "Persons" 表中选取 50% 的记录。</br>
  我们可以使用下面的 SELECT 语句：</br>
  
  `SELECT TOP 50 PERCENT * FROM Persons`

  得到的结果：
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1	|Adams	|ohn	|Oxford Street	|London
  |2	|Bush	|George	|Fifth Avenue	|New York
  
### 7.LIKE 操作符
  LIKE 操作符用于在 WHERE 子句中搜索列中的指定模式。</br>
  例子：</br>
  原始的表：</br>
  Persons 表:
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1|	Adams	| John|	Oxford Street|	London|
  |2|	Bush	| George	|Fifth Avenue|	New York|
  |3|	Carter	| Thomas	|Changan Street|	Beijing|
  
  现在，我们希望从上面的 "Persons" 表中选取居住在以 "N" 开始的城市里的人</br>：
  我们可以使用下面的 SELECT 语句：</br>
  
  `SELECT * FROM Persons
  WHERE City LIKE 'N%'`
  
  `note:"%" 可用于定义通配符（模式中缺少的字母）。`
  
  得到的结果：
  
  |Id|	LastName	|FirstName	|Address|	City|
  |----|----|----|----|----|----|
  |2|	Adams	|John|	Oxford Street|	London|
  
  
  接下来，我们希望从 "Persons" 表中选取居住在以 "g" 结尾的城市里的人：</br>
  我们可以使用下面的 SELECT 语句：</br>
  
  `SELECT * FROM Persons
  WHERE City LIKE '%g'`
  
  得到的结果：
  
  |Id|	LastName	|FirstName	|Address|	City|
  |----|----|----|----|----|----|
  |3|	Carter	|Thomas	|Changan Street|	Beijing|
  
  
  接下来，我们希望从 "Persons" 表中选取居住在包含 "lon" 的城市里的人：</br>
  我们可以使用下面的 SELECT 语句：</br>

  `SELECT * FROM Persons
  WHERE City LIKE '%lon%'`
  
  得到的结果：
  
  |Id|	LastName	|FirstName	|Address|	City|
  |----|----|----|----|----|----|
  |1|	Adams	|John|	Oxford Street|	London|
  
  
  通过使用 NOT 关键字，我们可以从 "Persons" 表中选取居住在不包含 "lon" 的城市里的人：</br>
  我们可以使用下面的 SELECT 语句：</br>
  
  `SELECT * FROM Persons
  WHERE City NOT LIKE '%lon%'`
  
  得到的结果：
  
  |Id|	LastName	|FirstName	|Address|	City|
  |----|----|----|----|----|----|
  |2|	Bush	|George	|Fifth Avenue|	New York|
  |3|	Carter	|Thomas	|Changan Street|	Beijing|
  
### 8.SQL通配符
  在搜索数据库中的数据时，SQL 通配符可以替代一个或多个字符。</br>
  SQL 通配符必须与 LIKE 运算符一起使用。</br>
  在 SQL 中，可使用以下通配符：
  
  |通配符|	描述|
  |----|----|----
  |%	|替代一个或多个字符|
  |_|	仅替代一个字符|
  |[charlist]	|字符列中的任何单一字符
  |[^charlist]或者[!charlist]|不在字符列中的任何单一字符
  
### 9.in操作符：
  IN 操作符允许我们在 WHERE 子句中规定多个值。</br>
  
  例子：</br>
  原始的表：</br>
  Persons 表:
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1|	Adams	|John|	Oxford Street|	London|
  |2|	Bush|	George|	Fifth Avenue|	New York|
  |3|	Carter|	Thomas|	Changan Street|	Beijing|
  |4|	Obama	Barack|	Pennsylvania Avenue|	Washington|
  
  现在，我们希望从上表中选取姓氏为 Adams 和 Carter 的人：</br>
  我们可以使用下面的 SELECT 语句：</br>
  
  `SELECT * FROM Persons
  WHERE LastName IN ('Adams','Carter')`
  
  结果集：
  
  |Id|	LastName|	FirstName|	Address|	City|
  |----|----|----|----|----|
  |1|	Adams|	John|	Oxford| Street|	London|
  |3|Carter	|Thomas|	Changan |Street	|Beijing|

