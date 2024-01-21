-- 1.. the total number of rows in the database
SELECT sum(reltuples) FROM pg_class WHERE relkind='r';
---2. show the first 15 rows, but only display 3 columns (id, manufacturer, and rating)
SELECT coffee.country, coffee.Coffee_type, coffee.Total_domestic_consumption
FROM coffee
LIMIT 15;
---3. do the same as above, but chose a column (rating) to sort on, and sort in descending order
SELECT coffee.country, coffee.coffee_type, coffee.Total_domestic_consumption FROM coffee ORDER BY coffee.Total_domestic_consumption desc LIMIT 15
---4. add a new column called description without a default value
ALTER TABLE coffee ADD COLUMN description text;
---5. set the value of that new column as 'data from kaggle'
UPDATE coffee SET description = 'data from Kaggle';
---6. show only the unique (non duplicates) of the rating column
SELECT DISTINCT total_domestic_consumption FROM coffee;
---7. group rows together by the coffee type column and use an aggregate function to calculate the average consumption
SELECT coffee_type, AVG(total_domestic_consumption::numeric) AS avg_consumption
FROM coffee
GROUP BY coffee_type;
---8. now, using the same grouping query, filter the query results by only selecting avg_consumption  with more than 500000000 counts
SELECT coffee_type, AVG(total_domestic_consumption::numeric) AS avg_consumption
FROM coffee
GROUP BY coffee_type
Having AVG(total_domestic_consumption::numeric) > 500000000;
---9. show all country that total_consumption  higher than 500000000
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
---10. show  country that consumes Arabica  that total_consumption  higher than 500000000

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
---11. show  country that consumes  Robusta  that total_consumption  higher than 500000000

SELECT country, total_domestic_consumption
FROM coffee
WHERE coffee_type = ' Robusta' AND (total_domestic_consumption::numeric)  > 500000000;
```
 country | total_domestic_consumption 
---------+----------------------------
(0 rows)


```
---12.show  country that consumes  Robusta/Arabica   that total_consumption  higher than 500000000
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
