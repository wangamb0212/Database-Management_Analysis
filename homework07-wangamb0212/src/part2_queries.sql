
-- 1. Show the possible values of the year column in the country_stats table sorted by most recent year first
SELECT DISTINCT year FROM country_stats ORDER BY year DESC

-- 2. Show the names of the first 5 countries in the database when sorted in alphabetical order by name.
SELECT name FROM countries ORDER BY name LIMIT 5

-- 3. Adjust the previous query to show both the country name and the gdp from 2018, but this time show the top 5 countries by gdp.
SELECT name, gdp FROM countries 
	INNER JOIN country_stats ON countries.country_id = country_stats.country_id 
	WHERE year = 2018 ORDER BY gdp DESC LIMIT 5
	
-- 4. How many countries are associated with each region id?
SELECT region_id, COUNT(*) AS country_count
FROM countries
WHERE region_id IN (
  SELECT region_id FROM regions
)
GROUP BY region_id
ORDER BY country_count DESC;

-- 5. What is the average area of countries in each region id?
SELECT
  region_id,
  ROUND(avg_area) AS avg_area
FROM (
  SELECT
    countries.region_id,
    AVG(countries.area) AS avg_area
  FROM
    countries
    INNER JOIN regions ON countries.region_id = regions.region_id
    INNER JOIN region_areas ON regions.name = region_areas.region_name
  GROUP BY
    countries.region_id
) subquery
ORDER BY
  avg_area;

	
-- 6. Use the same query as above, but only show the groups with an average country area less than 1000
SELECT
  countries.region_id,
  ROUND(AVG(countries.area)) AS avg_area
FROM
  regions
  INNER JOIN countries ON countries.region_id = regions.region_id
  INNER JOIN region_areas ON regions.name = region_areas.region_name
GROUP BY
  countries.region_id
HAVING
  ROUND(AVG(countries.area)) < 1000
ORDER BY
  avg_area;

-- 7. Create a report displaying the name and population of every continent in the database from the year 2018 in millions
SELECT
  name,
  ROUND(tot_pop / 1000000.0, 2) AS tot_pop
FROM (
  SELECT continents.name,
    SUM(country_stats.population) AS tot_pop
  FROM
    continents
    INNER JOIN regions ON continents.continent_id = regions.continent_id
    INNER JOIN countries ON regions.region_id = countries.region_id
    INNER JOIN country_stats ON countries.country_id = country_stats.country_id
  WHERE
    country_stats.year = 2018
  GROUP BY
    continents.name
) subquery
ORDER BY
  tot_pop DESC;

-- 8. List the names of all of the countries that do not have a language
SELECT name FROM countries
WHERE country_id NOT IN (
  SELECT country_id FROM country_languages
)


-- 9. Show the country name and number of associated languages of the top 10 countries with most languages
SELECT
  name,
  lang_count
FROM (
  SELECT
    countries.name,
    COUNT(country_languages.country_id) AS lang_count
  FROM
    countries
    LEFT OUTER JOIN country_languages ON countries.country_id = country_languages.country_id
  GROUP BY
    countries.name
  ORDER BY
    lang_count DESC,
    countries.name
  LIMIT 10
) subquery


-- 10. Repeat your previous query, but display a comma separated list of spoken languages rather than a count
SELECT
  countries.name,
  STRING_AGG(languages.language, ', ') AS spoken_languages
FROM
  countries
  LEFT OUTER JOIN country_languages ON countries.country_id = country_languages.country_id
  LEFT OUTER JOIN languages ON country_languages.language_id = languages.language_id
GROUP BY
  countries.name
ORDER BY
  countries.name;

-- 11. What's the average number of languages in every country in a region in the dataset? 
SELECT
  regions.name,
  ROUND(AVG(language_counts.lang_count), 1) AS avg_lang_count_per_country
FROM (
  SELECT
    countries.region_id,
    COUNT(country_languages) AS lang_count
  FROM
    countries
    LEFT OUTER JOIN country_languages ON countries.country_id = country_languages.country_id
  GROUP BY
    countries.region_id, countries.name
) language_counts
INNER JOIN
  regions ON language_counts.region_id = regions.region_id
GROUP BY
  regions.name
ORDER BY
  avg_lang_count_per_country DESC;


-- 12. Show the country name and its "national day" for the country with the most recent national day and the country with the oldest national day
SELECT
  countries.name,
  countries.national_day
FROM
  countries
  JOIN (
    SELECT
      MAX(national_day) AS max_national_day,
      MIN(national_day) AS min_national_day
    FROM
      countries
  ) national_days
  ON countries.national_day IN (national_days.max_national_day, national_days.min_national_day);
