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

query1 = """    SELECT d.E_ID, d.Name, d.Surname  FROM Employee as d INNER JOIN  Make_an_appointment as m
                 ON m.E_ID = d.E_ID and m.P_ID = 'INPUT' and m.Date::DATE = (SELECT MAX(m.Date::DATE) as da FROM Employee as d INNER JOIN  Make_an_appointment as m
                 ON m.E_ID = d.E_ID and m.P_ID = 'INPUT') 
                 WHERE
                 d.type = 'Doctor'
                 and ((d.surname LIKE 'L%' or d.surname LIKE 'M%' ) and (d.name NOT LIKE 'L%' and d.name NOT LIKE 'M%'))
                 or ((d.name LIKE 'L%' or d.name LIKE 'M%') and (d.surname NOT LIKE 'L%' and d.surname NOT LIKE 'M%'));
         """
         
query2 = """
            (SELECT apps.e_id, apps.name, apps.surname, COUNT(apps.p_id) as app_count, CAST(COUNT(apps.p_id) as float)/52 as app_count_avg, apps.day_w, CAST(EXTRACT(HOUR from apps.date) as int) as time_slot FROM
            (SELECT a.p_id, a.e_id, e.name, e.surname, to_char(a.date, 'day') as day_w, a.date as date FROM make_an_appointment as a, employee as e
              WHERE a.e_id = e.e_id AND e.type = 'Doctor' AND a.date > current_date - interval '1 year') as apps
              GROUP BY apps.e_id, apps.day_w, time_slot, apps.name, apps.surname
              ORDER BY apps.e_id, apps.day_w,time_slot)
         """   

query3 = """   SELECT p.p_id FROM
                (
                  SELECT num_app_year.p_id, COUNT(num_app_year.week) as w_count, SUM(num_app_year.p_count) as all_patients FROM 
                    (
                      SELECT apps.p_id, COUNT(apps.p_id) as p_count, apps.week FROM 
                          (
                          SELECT a.p_id, date_part('week', a.date) as week FROM make_an_appointment as a, patient as p
                              WHERE date_part('month', a.date) = date_part('month', current_date ) -1   
                              AND a.p_id = p.p_id )
                             as apps 
                        GROUP BY apps.p_id, apps.week
                        HAVING COUNT(apps.p_id) >= 2
                    ) as num_app_year
                  GROUP BY num_app_year.p_id
                  HAVING COUNT(num_app_year.week) = 5
                ) as res, patient as p
                WHERE res.p_id = p.p_id
         """
query4 = """SELECT SUM(CASE
                WHEN
                 num<3 and age<50
                 THEN num*200
                 WHEN
                 num<3 and age>=50
                 THEN num*400
                 WHEN
                 num>=3 and age<50
                 THEN num *250
                 WHEN
                 num>=3 and age>=50
                 THEN num*500
                 ELSE 0
                 END) as amount
                    FROM (SELECT P.P_ID as ID, COUNT(P.P_ID) as num 
                        FROM patient as p INNER JOIN  Make_an_appointment as m
                        ON m.P_ID = P.P_ID 
                        WHERE
                        Date > current_date - interval '1 month'
                        GROUP BY ID)as patients
                        INNER JOIN
                        (SELECT patient.P_ID as ID, EXTRACT(YEAR from AGE(patient.dob)) as age
                            FROM patient
                            GROUP BY ID) as p_db
                        ON p_db.ID = patients.ID    
        """
query5 = """    SELECT e.e_id,e.Name,e.Surname FROM
                    (SELECT num_app_year.e_id, COUNT(num_app_year.d_year) as y_count, SUM(num_app_year.p_count) as all_patients FROM 
                    (SELECT apps.e_id, COUNT(apps.p_id) as p_count, apps.d_year FROM 
                    (SELECT a.p_id, a.e_id, date_part('year', a.date) as d_year FROM make_an_appointment as a, employee as e
                    WHERE 
                    date_part('year', a.date) > date_part('year', current_date) - 10
                    AND a.e_id = e.e_id AND e.type = 'Doctor') as apps 
                    GROUP BY apps.e_id, apps.d_year
                    HAVING COUNT(apps.e_id) >= 5) as num_app_year
                    GROUP BY num_app_year.e_id
                    HAVING COUNT(num_app_year.d_year) = 10 
                    AND SUM(num_app_year.p_count) >= 100
                    ) as res, employee as e
                    WHERE res.e_id = e.e_id
         """  
