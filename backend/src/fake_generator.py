import json

import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# Initialize Faker to generate random data
fake = Faker()


# Function to generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())


# Connect to the database
def get_db_connection():
    return psycopg2.connect(
        dbname="ediss7db",  # your database name
        user="postgres",  # your username
        password="postgres",  # your password
        host="localhost",  # your host, e.g., 'localhost'
        port="5436"  # your port, typically 5432
    )


# Insert random data for the `user_info` table
def generate_user_info(cursor, num_rows):
    for _ in range(num_rows):
        username = fake.user_name()
        password = fake.password()
        user_status = random.choice([0, 1, 2])  # Example user statuses
        user_type = random.choice([1, 2])  # Example user types
        language = random.choice(['EN', 'ES', 'FR', 'DE', 'IT'])
        is_active = random.choice([True, False])
        description = fake.text(max_nb_chars=255)

        query = """
        INSERT INTO ewallet.user_info (username, password, user_status, user_type, language, is_active, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, user_status, user_type, language, is_active, description))


# Insert random data for the `product_info` table
def generate_product_info(cursor, num_rows):
    for _ in range(num_rows):
        name = fake.word()
        description = fake.text(max_nb_chars=255)
        tag = fake.word()
        purchase_flow = {'step1': fake.word(), 'step2': fake.word()}  # Example JSON
        params = {'param1': random.randint(1, 100), 'param2': random.choice([True, False])}  # Example JSON
        is_debt = random.choice([True, False])
        is_active = random.choice([True, False])

        query = """
        INSERT INTO ewallet.product_info (name, description, tag, purchase_flow, params, is_debt, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query,
                       (name, description, tag, json.dumps(purchase_flow), json.dumps(params), is_debt, is_active))


# Insert random data for the `payment_order` table
def generate_payment_order(cursor, num_rows):
    for _ in range(num_rows):
        order_uuid = generate_uuid()
        user_id = random.randint(1, 1000)  # Assuming you have 1000 users
        target_user_id = random.randint(1, 1000) if random.choice([True, False]) else None
        amount = round(random.uniform(10.0, 5000.0), 2)
        currency_code = random.choice(['USD', 'EUR', 'GBP', 'AZN'])
        additional_fee = round(random.uniform(0.0, 100.0), 2)
        order_type = random.choice([1, 2])  # Example order types
        order_status = random.choice([1, 2])  # Example order statuses
        order_additional_data = {"data": fake.text()}  # Example JSON
        order_details = {"details": fake.text()}  # Example JSON
        payment_channel = random.choice([1, 2, 3])  # Example payment channels
        is_auto_payment = random.choice([True, False])

        query = """
        INSERT INTO ewallet.payment_order (order_uuid, user_id, target_user_id, amount, currency_code, additional_fee,
                                            order_type, order_status, order_additional_data, order_details, payment_channel, 
                                            is_auto_payment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (order_uuid, user_id, target_user_id, amount, currency_code, additional_fee, order_type,
                               order_status, json.dumps(order_additional_data), json.dumps(order_details),
                               payment_channel, is_auto_payment))


# Insert random data for the `wallet_info` table
def generate_wallet_info(cursor, num_rows):
    for _ in range(num_rows):
        user_id = random.randint(1, 1000)
        available_amount = round(random.uniform(0.0, 10000.0), 2)
        currency_code = random.choice(['USD', 'EUR', 'GBP', 'AZN'])
        wallet_status = random.choice([1, 2])  # Example wallet statuses
        is_active = random.choice([True, False])

        query = """
        INSERT INTO ewallet.wallet_info (user_id, available_amount, currency_code, wallet_status, is_active)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, available_amount, currency_code, wallet_status, is_active))


# Insert random data for the `wallet_transaction` table
def generate_wallet_transaction(cursor, num_rows):
    for _ in range(num_rows):
        user_id = random.randint(1, 1000)
        transfer_wallet_id = random.randint(1, 1000)
        txn_amount = round(random.uniform(1.0, 1000.0), 2)
        final_available_amount = round(random.uniform(0.0, 10000.0), 2)
        currency_code = random.choice(['USD', 'EUR', 'GBP', 'AZN'])
        txn_type = random.choice([1, 2])  # Example transaction types
        txn_direction = random.choice(['I', 'O'])  # 'I' for income, 'O' for outgoing
        txn_status = random.choice([1, 2])  # Example txn statuses
        order_id = random.randint(1, 1000)  # Assuming you have 1000 orders

        query = """
        INSERT INTO ewallet.wallet_transaction (user_id, transfer_wallet_id, txn_amount, final_available_amount, 
                                                 currency_code, txn_type, txn_direction, txn_status, order_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, transfer_wallet_id, txn_amount, final_available_amount, currency_code,
                               txn_type, txn_direction, txn_status, order_id))


# Main function to generate data and insert it into the database
def generate_data(num_rows):
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Generate and insert data into each table
    generate_user_info(cursor, num_rows)
    generate_product_info(cursor, num_rows)
    generate_payment_order(cursor, num_rows)
    generate_wallet_info(cursor, num_rows)
    generate_wallet_transaction(cursor, num_rows)

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Successfully inserted {num_rows} rows of data into the database.")


generate_data(5000)