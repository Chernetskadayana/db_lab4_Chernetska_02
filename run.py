import psycopg2
username = 'chernetskadaiana'
password = 'playmarket'
database = 'Hospital Administration(l4)'
host = 'localhost'
port = '5432'

query_function_1 = '''
select * from patient;
'''
query_function_2 = '''
select clean_patient(); 
'''
query_function_3 = '''
select * FROM patient 
   WHERE patient.p_id IN 
      (SELECT patient.p_id from patient left join appointment using(p_id) where appointment.p_id is NULL);
'''


query_trigger = '''

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()
    cur.execute(query_function_1)
    p_id = []
    p_name = []
    gender = []
    age = []
    for row in cur:
        p_id.append(row[0])
        p_name.append(row[1])
        gender.append(row[2])
        age.append(row[3])
    print('\n----------------------------------------- FUNCTION --------------------------------------')
    print('Видалення пацієнтів, що не мають призначень до лікаря')
    print('\nПочаткова таблиця: ')

    for i in range(len(p_id)):
        print(p_id[i], p_name[i], gender[i], age[i], sep='  ')

    print('\nПацієнти, що не мають призначень:')

    p_id.clear()
    p_name.clear()
    gender.clear()
    age.clear()

    cur.execute(query_function_3)

    for row in cur:
        p_id.append(row[0])
        p_name.append(row[1])
        gender.append(row[2])
        age.append(row[3])

    for i in range(len(p_id)):
        print(p_id[i], p_name[i], gender[i], age[i], sep='  ')

    print('\nКінцева таблиця:')
    p_id.clear()
    p_name.clear()
    gender.clear()
    age.clear()

    cur.execute(query_function_2)
    cur.execute(query_function_1)

    for row in cur:
        p_id.append(row[0])
        p_name.append(row[1])
        gender.append(row[2])
        age.append(row[3])
    for i in range(len(p_id)):
        print(p_id[i], p_name[i], gender[i], age[i], sep='  ')

    print('\n----------------------------------------- PROCEDURE --------------------------------------')
    print('Заміняє номеру кабінету в таблиці appointment за вказаним id на задане значення')

    cur.execute('select * from appointment;')

    app_id = []
    d_id = []
    pat_id = []
    a_date = []
    cabinet = []

    for row in cur:
        app_id.append(row[0])
        d_id.append(row[1])
        pat_id.append(row[2])
        a_date.append(row[3])
        cabinet.append(row[4])

    print('\nПочаткова таблиця: ')

    for i in range(len(pat_id)):
        print(app_id[i], d_id[i], pat_id[i], a_date[i], cabinet[i], sep='  ')

    i_d = '81873900'
    new_cabinet = 21

    print("\nЗадані значення: '{}', {}".format(i_d, new_cabinet))
    cur.execute("call replace_cabinet_num('{}', {});".format(i_d, new_cabinet))

    app_id = []
    d_id = []
    pat_id = []
    a_date = []
    cabinet = []

    cur.execute('select * from appointment;')

    for row in cur:
        app_id.append(row[0])
        d_id.append(row[1])
        pat_id.append(row[2])
        a_date.append(row[3])
        cabinet.append(row[4])

    print('\nКінцева таблиця:')

    for i in range(len(pat_id)):
        print(app_id[i], d_id[i], pat_id[i], a_date[i], cabinet[i], sep='  ')

    print('\n----------------------------------------- TRIGGER --------------------------------------')
    print("Додає в таблицю app_audit, дату, час вставлення, ім'я користувача. "
          "\nСпрацьовує після insert в таблицю Appointment")

    cur.execute('select * from appointment;')

    app_id = []
    d_id = []
    pat_id = []
    a_date = []
    cabinet = []

    for row in cur:
        app_id.append(row[0])
        d_id.append(row[1])
        pat_id.append(row[2])
        a_date.append(row[3])
        cabinet.append(row[4])

    print('\nТаблиця Appointment: ')

    for i in range(len(pat_id)):
        print(app_id[i], d_id[i], pat_id[i], a_date[i], cabinet[i], sep='  ')

    a_id = []
    insert_time = []
    insert_date = []
    user_name = []

    cur.execute("INSERT INTO Appointment(app_id, d_id, p_id, a_date, cabinet) "
                "VALUES('123855', '89608', '35476317', current_date, 21);")

    cur.execute('select * from app_audit;')
    for row in cur:
        a_id.append(row[0])
        insert_time.append(row[1])
        insert_date.append(row[2])
        user_name.append(row[3])

    print('\nТаблиця App_audit: ')
    for i in range(len(a_id)):
        print(a_id[i], insert_time[i], insert_date[i], user_name[i], sep='  ')
