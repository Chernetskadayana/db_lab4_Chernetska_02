
-- Функція заміняє номер кабінету в таблиці appointment з вказаним id на задане значення
create or replace procedure replace_cabinet_num(
   app_num char(20),
   new_cabin int  
)
language plpgsql    
as $$
begin
    update appointment
    set cabinet = new_cabin 
    where app_id = app_num;
end;$$;
