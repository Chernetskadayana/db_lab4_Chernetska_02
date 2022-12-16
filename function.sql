-- Видалити з таблиці Patient пацієнтів, яких немає в Appointment, 
-- тобто в яких не заплановано відвідин лікаря

DROP FUNCTION IF EXISTS clean_patient();
CREATE OR REPLACE FUNCTION clean_patient() RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN 
   DELETE FROM patient 
   WHERE patient.p_id IN 
      (SELECT patient.p_id from patient left join appointment using(p_id) where appointment.p_id is NULL);
END;
$$; 