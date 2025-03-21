CREATE TABLE ontario_covid_vaccine_data (
    record_date DATE,
    phu_id NUMBER(10),
    phu_name VARCHAR2(100),
    age_group VARCHAR2(50),
    at_least_one_dose_cumulative NUMBER(10),
    second_dose_cumulative NUMBER(10),
    fully_vaccinated_cumulative NUMBER(10),
    third_dose_cumulative NUMBER(10),
    total_population NUMBER(10),
    percent_at_least_one_dose NUMBER(5,2),
    percent_fully_vaccinated NUMBER(5,2),
    percent_3doses NUMBER(5,2)
);
