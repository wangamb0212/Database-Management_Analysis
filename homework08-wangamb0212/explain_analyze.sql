-- TODO: use explain / analyze, create an index

--Drop an existing index:
drop index if exists athlete_event_name_idx;

--write a query to find all rows that contain the athlete Michael Fred Phelps, II (use the name column)
SELECT * FROM athlete_event WHERE name = 'Michael Fred Phelps, II';

--Using EXPLAIN ANALYZE
EXPLAIN ANALYZE SELECT * FROM athlete_event WHERE name = 'Michael Fred Phelps, II';
"Gather  (cost=1000.00..8213.36 rows=3 width=137) (actual time=18.885..25.384 rows=30 loops=1)"
"  Workers Planned: 2"
"  Workers Launched: 2"
"  ->  Parallel Seq Scan on athlete_event  (cost=0.00..7213.06 rows=1 width=137) (actual time=15.874..18.802 rows=10 loops=3)"
"        Filter: (name = 'Michael Fred Phelps, II'::text)"
"        Rows Removed by Filter: 90362"
"Planning Time: 0.078 ms"
"Execution Time: 25.406 ms"
-- Add an index
CREATE INDEX athlete_event_name ON athlete_event (name);
--Verifying improved performance:
EXPLAIN ANALYZE SELECT * FROM athlete_event WHERE name = 'Michael Fred Phelps, II';
"Index Scan using athlete_event_name on athlete_event  (cost=0.42..16.44 rows=3 width=137) (actual time=0.734..0.741 rows=30 loops=1)"
"  Index Cond: (name = 'Michael Fred Phelps, II'::text)"
"Planning Time: 15.469 ms"
"Execution Time: 0.775 ms"

--Ignoring an index:
SELECT * FROM athlete_event WHERE name ILIKE 'michael%fred%';