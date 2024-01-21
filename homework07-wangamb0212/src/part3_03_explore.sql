-- create a view without duplicate rows
CREATE OR REPLACE VIEW d_caers_event_product AS
SELECT
  report_id,
  created_date,
  event_date,
  product_type,
  product,
  product_code,
  description,
  patient_age,
  age_units,
  sex,
  terms,
  outcomes
FROM (
  SELECT DISTINCT
    report_id,
    created_date,
    event_date,
    product_type,
    product,
    product_code,
    description,
    patient_age,
    age_units,
    sex,
    terms,
    outcomes
  FROM
    staging_caers_event_product
) subquery;
-- 1. try to see if other columns are functionally dependent on report_id
SELECT
  report_id,
  COUNT(*) AS c
FROM (
  SELECT
    report_id,
    MAX(created_date) AS created_date,
    MAX(event_date) AS event_date,
    MAX(patient_age) AS patient_age,
    MAX(age_units) AS age_units,
    MAX(sex) AS sex,
    MAX(terms) AS terms,
    MAX(outcomes) AS outcomes
  FROM
    d_caers_event_product
  GROUP BY
    report_id
) pcd
GROUP BY
  report_id
ORDER BY
  c DESC
LIMIT 5;

"100011"	1
"100013"	1
"100018"	1
"100019"	1
"100008"	1
-- those columns are  functionally dependent on report_id.

-- 2. determine whether product_code is functionally dependent on product

SELECT
  product,
  COUNT(DISTINCT product_code) AS c
FROM
  d_caers_event_product
GROUP BY
  product
ORDER BY
  c DESC
LIMIT 5;

"EXEMPTION 4"	40
"SALAD"	5
"JUICE"	4
"DAILY HARVEST SMOOTHIES"	4
"JIF PEANUT BUTTER"	4

--product_code is not functionally dependent on product beacuse there are count larger than 1.


-- 3. determine whether description is functionally dependent on product_code
SELECT
  product_code,
  COUNT(DISTINCT description) AS c
FROM
  d_caers_event_product
GROUP BY
  product_code
ORDER BY
  c DESC
LIMIT 5;

"03"	1
"04"	1
"05"	1
"07"	1
"02"	1

-- There are counts larger than 1, indicating that outcomes is not functionally dependent on terms.

-- 4.determine whether or not report_id + product + product_code + product_type is unique

SELECT
  report_id,
  product,
  product_code,
  product_type,
  COUNT(*) AS c
FROM
  d_caers_event_product
GROUP BY
  report_id,
  product,
  product_code,
  product_type
ORDER BY
  c DESC
LIMIT 5;

"145102"	"PHILADELPHIA REGULAR CREAM CHEESE SPREAD SALMON FLAVORED"	"12"	"SUSPECT"	1
"155837"	"COQ10"	"54"	"CONCOMITANT"	1
"141022"	"GROUPER"	"16"	"SUSPECT"	1
"122232"	"NESTLE'S TOLL HOUSE WALNUT CHOC CHIP COOKIE"	"03"	"SUSPECT"	1
"151942"	"FLINTSTONES COMPLETE"	"54"	"SUSPECT"	1

--All counts are equal to 1 , this combination can be the proper primary key.