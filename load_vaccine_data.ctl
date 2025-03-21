LOAD DATA
INFILE 'vaccines_by_age_phu_cleaned.csv'
INTO TABLE ONTARIO_COVID_VACCINE_DATA
APPEND
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
  record_date DATE "YYYY-MM-DD",
  phu_id,
  phu_name,
  age_group,
  at_least_one_dose_cumulative,
  second_dose_cumulative,
  fully_vaccinated_cumulative,
  third_dose_cumulative,
  total_population,
  percent_at_least_one_dose,
  percent_fully_vaccinated,
  percent_3doses
)
