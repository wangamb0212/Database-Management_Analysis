-- write your table creation sql here!
DROP TABLE IF EXISTS Coffee;
CREATE TABLE Coffee (
	Country text primary key,
	Coffee_type text NOT NULL,
	Total_domestic_consumption text NOT NULL);