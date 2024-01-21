-- write your COPY statement to import a csv here
Copy Coffee (Country,Coffee_type,Total_domestic_consumption)
FROM '/private/tmp/coffee.csv'
CSV HEADER DELIMITER ',' NULL AS '';