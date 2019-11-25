truncate = """
                TRUNCATE Patient CASCADE;
                TRUNCATE Employee CASCADE;
                TRUNCATE Stationary_patient CASCADE;
                TRUNCATE Guest CASCADE;
                TRUNCATE Make_an_appointment CASCADE;
                TRUNCATE Optional_treatment CASCADE;
                TRUNCATE Get_optional_treatment CASCADE;
                TRUNCATE Visit CASCADE;
                TRUNCATE Notice_board CASCADE;
                TRUNCATE Stuff_schedule CASCADE;
                TRUNCATE Hospital_equipment CASCADE;
                TRUNCATE Medical_history CASCADE;
                TRUNCATE Donate CASCADE;
                TRUNCATE Conclude_agreement CASCADE;
                TRUNCATE Control CASCADE;
           """


query1 = """    SELECT d.Name, d.Surname  FROM Employee as d INNER JOIN  Make_an_appointment as m
                 ON m.E_ID = d.E_ID and m.P_ID = 'INPUT' and m.Date::DATE = (SELECT MAX(m.Date::DATE) as da FROM Employee as d INNER JOIN  Make_an_appointment as m
                 ON m.E_ID = d.E_ID and m.P_ID = 'INPUT') 
                 WHERE
                 d.type = 'Doctor'
                 and ((d.surname LIKE 'L%' or d.surname LIKE 'M%' ) and (d.name NOT LIKE 'L%' and d.name NOT LIKE 'M%'))
                 or ((d.name LIKE 'L%' or d.name LIKE 'M%') and (d.surname NOT LIKE 'L%' and d.surname NOT LIKE 'M%'));
         """

query2 = """    SELECT employee.e_id, app.date, count(*), (CAST(count(*) as FLOAT)/52), dow as app_avg \
                        FROM Employee, (SELECT *, to_char(date, 'day') as dow FROM make_an_appointment) AS app WHERE employee.e_id=app.e_id AND \
                        app.date > current_date - interval '365 days'\
                        GROUP BY Employee.e_id, app.date, dow\
                        ORDER BY Employee.e_id, dow, app.Date
         """

query3 = """     SELECT p.p_id, p.name, p.surname FROM
                    (SELECT num_app_week.p_id, COUNT(num_app_week.week) as w_count,
                    SUM(num_app_week.p_count) as all_patients FROM 
                    (--Selecting patients and number of their appointments for last 4 weeks
                    SELECT apps.p_id, COUNT(apps.p_id) as p_count, apps.week FROM 
                    ( --Selecting appointments for last 4 weeks
                    SELECT a.p_id, date_part('week', a.date) as week FROM make_an_appointment as a, patient as p
                    WHERE date_part('week', a.date) > date_part('week', current_date ) - 5 
                    AND date_part('week', a.date) < date_part('week', current_date ) 
                    AND a.p_id = p.p_id) as apps 
                    GROUP BY apps.p_id, apps.week
                    HAVING COUNT(apps.p_id) >= 2) as num_app_week
                    GROUP BY num_app_week.p_id
                    HAVING COUNT(num_app_week.p_count) = 4) as res, patient as p
                        WHERE res.p_id = p.p_id
         """
query4 = """
                SELECT SUM(T.cnt) as Amount
                    FROM
                    (SELECT COUNT(p.P_id)*200 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
                      ON m.P_ID = P.P_ID 
                      WHERE 
                      Date > current_date - interval '1 month'
                      GROUP By M.P_ID, P.dob
                      HAVING Count(M.P_ID)<3 and EXTRACT(YEAR from AGE(P.dob))<50
                     UNION ALL
                     SELECT COUNT(p.P_id)*400 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
                      ON m.P_ID = P.P_ID 
                      WHERE 
                      Date > current_date - interval '1 month'
                      GROUP By M.P_ID, P.dob
                      HAVING Count(M.P_ID)<3 and EXTRACT(YEAR from AGE(P.dob))>49
                     UNION ALL
                     SELECT COUNT(p.P_id)*500 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
                      ON m.P_ID = P.P_ID 
                      WHERE 
                      Date > current_date - interval '1 month'
                      GROUP By M.P_ID, P.dob
                      HAVING Count(M.P_ID)>2 and EXTRACT(YEAR from AGE(P.dob))>49
                     UNION ALL
                     SELECT COUNT(p.P_id)*250 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
                      ON m.P_ID = P.P_ID 
                      WHERE 
                      Date > current_date - interval '1 month'
                      GROUP By M.P_ID, P.dob
                      HAVING Count(M.P_ID)>2 and EXTRACT(YEAR from AGE(P.dob))<50
                     ) as T
         """
query5 = """    SELECT e.e_id,e.Name,e.Surname FROM
                    (SELECT num_app_year.e_id, COUNT(num_app_year.d_year) as y_count, SUM(num_app_year.p_count) as all_patients FROM 
                    (SELECT apps.e_id, COUNT(apps.p_id) as p_count, apps.d_year FROM 
                    (SELECT a.p_id, a.e_id, date_part('year', a.date) as d_year FROM make_an_appointment as a, employee as e
                    WHERE 
                    date_part('year', a.date) > date_part('year', current_date) - 2 -- How many years
                    AND a.e_id = e.e_id AND e.type = 'Doctor') as apps 
                    GROUP BY apps.e_id, apps.d_year
                    HAVING COUNT(apps.e_id) >= 1) as num_app_year
                    GROUP BY num_app_year.e_id
                    HAVING COUNT(num_app_year.p_count) >= 2 -- Equal to how many years
                    AND SUM(num_app_year.p_count) > 2 -- Num of all patients per this period of time
                    ) as res, employee as e
                    WHERE res.e_id = e.e_id
         """  
query = """    SELECT * FROM CROSSTAB(
                'select e_id, app_count, day_w from (SELECT apps.e_id, COUNT(apps.p_id) as app_count, apps.day_w as day_w FROM
                (SELECT a.p_id, a.e_id, to_char(a.date, ''day'') as day_w FROM make_an_appointment as a, employee as e
                WHERE a.e_id = e.e_id AND e.type = ''Doctor'' AND a.date > current_date - interval ''1 year'') as apps
                 GROUP BY apps.e_id, apps.day_w)') as new_table(e_id varchar, monday int, tuesday int, wednesday int,
                                    thursday int, friday int, saturday int, sunday int)
         """    
