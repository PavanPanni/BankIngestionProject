import logging
import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

SERVICE_BUS_CONNECTION = os.getenv("SERVICE_BUS_CONNECTION_STR")
QUEUE_NAME = os.getenv("QUEUE_NAME")

def main(event: func.EventGridEvent):
    logging.info("Event Grid Trigger received event")

    data = event.get_json()
    blob_url = data.get("url")

    if not blob_url:
        logging.error("Blob URL missing in the event data")
        return

    logging.info(f"New Blob Created: {blob_url}")

    try:
        client = ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION)
        sender = client.get_queue_sender(QUEUE_NAME)
        with sender:
            sender.send_messages(ServiceBusMessage(blob_url))
        logging.info("Message sent to Service Bus queue")
    except Exception as e:
        logging.error(f"Service Bus Error: {e}")
