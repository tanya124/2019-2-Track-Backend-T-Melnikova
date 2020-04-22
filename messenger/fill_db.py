from factory import Sequence, Faker
from datetime import datetime
import psycopg2
import psycopg2.extras
#from db_config import DB_NAME, USER, HOST, PASSWORD
import random

DB_NAME='tanya_m_db'
USER='tanya_m'
PASSWORD='123'
HOST='0.0.0.0'

def populate():
    connection = psycopg2.connect(f"dbname={DB_NAME} user={USER} host={HOST} password={PASSWORD}")
    cursor = connection.cursor()

    print("populate users")
    for i in range(100):
        print(i)
        id = i + 100
        username = 'test_user_{0}'.format(i)
        password = 'password12345'
        is_superuser = False
        is_staff = False
        is_active = True
        nick = 'test_user_nick_{0}'.format(i)
        email = 'test_user_nick_{0}@mail.ru'.format(i)
        first_name = 'first_name'
        last_name = 'last_name'
        date_joined = datetime.now()

        cursor.execute('INSERT INTO users_user (id, password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, nick) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, nick))
    connection.commit()

    print("populate chats")
    for i in range(100):
        print(i)
        id = i + 100
        is_group_chat = True
        topic = 'topic_{0}'.format(i)
        last_message = str(Faker('text'))

        cursor.execute('INSERT INTO chats_chat (id, is_group_chat, topic, last_message) VALUES (%s, %s, %s, %s)', (id, is_group_chat, topic, last_message))
    connection.commit()

    print("populate members")
    for i in range(100):
        print(i)
        id = i + 100
        new_messages = False
        chat_id = 101
        user_id = i + 100

        cursor.execute('INSERT INTO users_member (id, new_messages, chat_id, user_id) VALUES (%s, %s, %s, %s)',
                       (id, new_messages, chat_id, user_id))
    connection.commit()

    print("populate messages")
    for i in range(1000):
        print(i)
        id = i + 100
        chat_id = 101
        user_id = random.randint(100, 199)
        content = str(Faker('text'))
        added_at = datetime.now()

        cursor.execute('INSERT INTO chats_message (id, content, added_at, chat_id, user_id) VALUES (%s, %s, %s, %s, %s)',
                       (id, content, added_at, chat_id, user_id))
    connection.commit()


    print("done")
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    populate()