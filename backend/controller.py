import json
import pika
import eventlet
from flask import Flask
from flask_socketio import SocketIO

eventlet.monkey_patch()  # Makes WebSockets work efficiently

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

RABBITMQ_HOST = "localhost"
RABBITMQ_USER = "guest"
RABBITMQ_PASS = "guest"
RESPONSE_QUEUE = "responses"


def rabbitmq_listener():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=6480, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue=RESPONSE_QUEUE)  # Ensure queue exists

    def callback(ch, method, properties, body):
        message = json.loads(body)



        socketio.emit(f"response", sql_result)

    channel.basic_consume(queue=SQL_RESULTS_QUEUE, on_message_callback=callback, auto_ack=True)

    print("Listening for SQL results in RabbitMQ...")
    channel.start_consuming()


eventlet.spawn(rabbitmq_listener)