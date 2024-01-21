# Overview
1. Name / Title: Coffee_domestic_consumption.csv
2. Link to Data: https://www.kaggle.com/datasets/michals22/coffee-dataset
3. Source / Origin: 
    * Author or Creator: Michał Sikora
    * Publication Date: 2022/12/10
    * Publisher: Kaggle
    * Version or Data Accessed: 2023/02/13
4. License: CC0: Public Domain
5. Can You Use this Data Set for Your Intended Use Case? Yes

* Format: csv
* Size: 24kb
* Number of Records: 55 rows

* Field/Column 1: Country, Str
* Field/Column 2: Coffee type, Str
* Field/Column 3-23: Year, int
* Field/Column 24: Total_domestic_consumption, int

For the followinf step in sql, I do not need the columns by single year. Like 1996/97. I want to drop it so that it will be easier to load in pgadmin
so the converted dataset is named coffee.csv.
with 

* Field/Column 1: Country, Str
* Field/Column 2: Coffee type, Str
* Field/Column 24: Total_domestic_consumption, int


NOTICE:  table "coffee" does not exist, skipping
CREATE TABLE

Query returned successfully in 54 msec.

# Table Design



Country: text, this can be used as primary key because it does not have null and it is all unique value.
Coffee type: text
Total_domestic_consumption: numeric

# Import
I first had:
ERROR:  could not open file "/Users/amber/Desktop/GitHub/amber_dma/homework06-wangamb0212/coffee.csv" for reading: Permission denied
HINT:  COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy.
SQL state: 42501
I fixed it with open /tmp in command line. I opened up the tmp folder and copied the csv I am working with into that folder.
Then, Query returned successfully in 139 msec.

# Database Information
show all database
SELECT datname FROM pg_database;
"postgres"
"homework06"
"template1"
"template0"

show all tables in homework06 database

SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';
"Coffee"
"coffee"


-- describe the table coffee
\d coffee
                       Table "public.coffee"
           Column           | Type | Collation | Nullable | Default 
----------------------------+------+-----------+----------+---------
 country                    | text |           | not null | 
 coffee_type                | text |           | not null | 
 total_domestic_consumption | text |           | not null | 

# Query Results
###1. the total number of rows in the database
SELECT sum(reltuples) FROM pg_class WHERE relkind='r';
"sum"
21090
```

```
### 2. show the first 15 rows, but only display 3 columns (id, manufacturer, and rating)
SELECT coffee.country, coffee.Coffee_type, coffee.Total_domestic_consumption
FROM coffee
LIMIT 15;

"country"	"coffee_type"	"total_domestic_consumption"
"Angola"	"Robusta/Arabica"	"46500000"
"Bolivia (Plurinational State of)"	"Arabica"	"75180000"
"Brazil"	"Arabica/Robusta"	"27824700000"
"Burundi"	"Arabica/Robusta"	"3412020"
"Ecuador"	"Arabica/Robusta"	"381540000"
"Indonesia"	"Robusta/Arabica"	"4920480000"
"Madagascar"	"Robusta"	"588705960"
"Malawi"	"Arabica"	"2340000"
"Papua New Guinea"	"Arabica/Robusta"	"3608400"
"Paraguay"	"Arabica"	"35100000"
"Peru"	"Arabica"	"402000000"
"Rwanda"	"Arabica"	"2139960"
"Timor-Leste"	"Arabica"	"294000"
"Zimbabwe"	"Arabica"	"8595960"
"Congo"	"Robusta"	"5360040"
```

```
### 3. do the same as above, but chose a column (rating) to sort on, and sort in descending order
SELECT coffee.country, coffee.coffee_type, coffee.Total_domestic_consumption FROM coffee ORDER BY coffee.Total_domestic_consumption desc LIMIT 15
             country              |   coffee_type   | total_domestic_consumption 
----------------------------------+-----------------+----------------------------
 Ghana                            | Robusta         | 9970800
 Zambia                           | Arabica         | 991920
 Kenya                            | Arabica         | 95190000
 Guyana                           | Robusta         | 9203040
 Guinea                           | Robusta         | 86730000
 Liberia                          | Robusta         | 8640000
 Zimbabwe                         | Arabica         | 8595960
 Tanzania                         | Arabica/Robusta | 76425060
 Bolivia (Plurinational State of) | Arabica         | 75180000
 Nigeria                          | Robusta         | 70740000
 Costa Rica                       | Arabica         | 665335200
 Dominican Republic               | Arabica/Robusta | 642823380
 Haiti                            | Arabica         | 600600000
 Guatemala                        | Arabica/Robusta | 590880000
 Madagascar                       | Robusta         | 588705960
(15 rows)
```

```
### 4. add a new column called description without a default value
ALTER TABLE coffee ADD COLUMN description text;
ALTER TABLE
```

```
### 5. set the value of that new column as 'data from kaggle'
UPDATE 55
```

```
### 6. show only the unique (non duplicates) of the rating column
SELECT DISTINCT total_domestic_consumption FROM coffee;
 total_domestic_consumption 
----------------------------
 294000
 35100000
 381540000
 46500000
 2386067999
 284816400
 359880000
 410260140
 2093460000
 1123140
 27824700000
 157980000
 2536776384
 417242040
 642823380
 8595960
 58300020
 4536540000
 4920480000
 1248600000
 299700300
 8640000
 9203040
 18688020
 24794400
 121620000
 76425060
 600600000
 588705960
 70740000
 471850680
 9970800
 991920
 122916960

```

```
### 7. group rows together by the coffee type column and use an aggregate function to calculate the average consumption
SELECT coffee_type, AVG(total_domestic_consumption::numeric) AS avg_consumption
FROM coffee
GROUP BY coffee_type;
```
   coffee_type   |    avg_consumption    
-----------------+-----------------------
 Arabica         |    599235246.50000000
 Robusta/Arabica |   1388369568.00000000
 Arabica/Robusta |   4089131107.50000000
 Robusta         | 93789676.000000000000
(4 rows)
```
### 8. now, using the same grouping query, filter the query results by only selecting avg_consumption  with more than 500000000 counts
SELECT coffee_type, AVG(total_domestic_consumption::numeric) AS avg_consumption
FROM coffee
GROUP BY coffee_type
Having AVG(total_domestic_consumption::numeric) > 500000000;
   coffee_type   |   avg_consumption   
-----------------+---------------------
 Arabica         |  599235246.50000000
 Robusta/Arabica | 1388369568.00000000
 Arabica/Robusta | 4089131107.50000000
(3 rows)
```

```
### 9. show all country that total_consumption  higher than 500000000
SELECT country, total_domestic_consumption
FROM coffee
WHERE (total_domestic_consumption::numeric) > 500000000;
```
      country       | total_domestic_consumption 
--------------------+----------------------------
 Brazil             | 27824700000
 Indonesia          | 4920480000
 Madagascar         | 588705960
 Dominican Republic | 642823380
 Haiti              | 600600000
 Philippines        | 2807280000
 Colombia           | 2536776384
 Costa Rica         | 665335200
 Ethiopia           | 4536540000
 Guatemala          | 590880000
 India              | 2093460000
 Mexico             | 3189660000
 Thailand           | 1248600000
 Venezuela          | 2386067999
 Viet Nam           | 1920928320
(15 rows)


```
### 10. show  country that consumes Arabica  that total_consumption  higher than 500000000

SELECT country, total_domestic_consumption
FROM coffee
WHERE coffee_type = 'Arabica' AND (total_domestic_consumption::numeric)  > 500000000;
```
  country   | total_domestic_consumption 
------------+----------------------------
 Haiti      | 600600000
 Colombia   | 2536776384
 Costa Rica | 665335200
 Ethiopia   | 4536540000
 Venezuela  | 2386067999
(5 rows)

```
### 11. show  country that consumes  Robusta  that total_consumption  higher than 500000000

SELECT country, total_domestic_consumption
FROM coffee
WHERE coffee_type = ' Robusta' AND (total_domestic_consumption::numeric)  > 500000000;
```
 country | total_domestic_consumption 
---------+----------------------------
(0 rows)


```
### 12.show  country that consumes  Robusta/Arabica   that total_consumption  higher than 500000000
SELECT country, total_domestic_consumption
FROM coffee
WHERE coffee_type LIKE '%Robusta/Arabica%' AND (total_domestic_consumption::numeric) > 500000000;

```
   country   | total_domestic_consumption 
-------------+----------------------------
 Indonesia   | 4920480000
 Philippines | 2807280000
 India       | 2093460000
 Thailand    | 1248600000
 Viet Nam    | 1920928320
(5 rows)