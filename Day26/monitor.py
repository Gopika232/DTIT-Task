import logging
import time

logging.basicConfig(filename="performance.log",level=logging.INFO)
def monitor_model():
    accuracy = 0.95
    response_time = 0.03
    logging.info("Model Accuracy: %s Response Time: %s seconds", accuracy,response_time)
while True:
    monitor_model()
    print("Model performance logged")
    time.sleep(10)