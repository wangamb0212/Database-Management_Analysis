COPY staging_caers_event_product (
	created_date, report_id, event_date,
	product_type, product, product_code,
	description, patient_age, age_units,
	sex, terms, outcomes)
    FROM '/private/tmp/CAERS-Quarterly--20220930-EXCEL.csv'
    (format csv, HEADER, ENCODING 'LATIN1');