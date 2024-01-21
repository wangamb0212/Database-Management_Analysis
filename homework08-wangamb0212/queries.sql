--Create View
DROP VIEW IF EXISTS olympic_view;
CREATE OR REPLACE VIEW olympic_view AS
SELECT COALESCE(region, 'Singapore') AS region, a.event, a.medal, a.year, a.height FROM athlete_event AS a
LEFT OUTER JOIN noc_region ON a.noc = noc_region.noc
WHERE medal IS NOT NULL;
-- write the task number and description followed by the query

WITH top_fencing_events AS (
  SELECT region, event, COUNT(*) AS gold_medals,
    RANK() OVER (PARTITION BY event ORDER BY COUNT(*) DESC) AS rank
  FROM olympic_view
  WHERE medal = 'Gold' AND event LIKE 'Fencing%'
  GROUP BY region, event
)
SELECT region, event, gold_medals, rank
FROM top_fencing_events
WHERE rank <= 3
ORDER BY event, rank;

-- Using Aggregate Functions as Window Functions
SELECT region, year, medal, count(*) AS c,
sum(count(*)) over (partition by region, medal ORDER BY year)
FROM olympic_view
GROUP BY region, year, medal
ORDER BY region, year, medal;

--Use the Window Function, lag()
SELECT event, year, height,
lag(height, 1) over (PARTITION BY event ORDER BY year) AS previous_height
FROM olympic_view
WHERE medal = 'Gold' AND event LIKE '%Pole Vault' AND height IS NOT NULL
GROUP BY event, year, height
ORDER BY event, year, height DESC;