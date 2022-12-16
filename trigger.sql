-- Тригер спрацьовує після вставлення нового рядка в Appointment
-- Додає в таблицю app_audit, дату, час вставлення, ім'я користувача

SELECT user from appointment;

DROP TABLE IF EXISTS app_audit;
CREATE TABLE app_audit(
	id SERIAL PRIMARY KEY,
	insert_time time,
	insert_date date,
	user_name varchar(50) NOT NULL
);

CREATE OR REPLACE FUNCTION app_audit() RETURNS trigger 
LANGUAGE 'plpgsql'
AS $$
BEGIN
 	INSERT INTO app_audit(insert_time, insert_date, user_name)
		VALUES(current_time, current_date, user);
	RETURN NULL;
END;
$$ ;


DROP TRIGGER IF EXISTS app_insert_details ON appointment;

CREATE TRIGGER app_insert_details 
AFTER INSERT ON appointment
FOR EACH ROW EXECUTE FUNCTION app_audit();
