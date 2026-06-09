import logging
from datetime import datetime


# Configure logging

logging.basicConfig(
    filename="attendance.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def mark_attendance(name):

    time = datetime.now()

    message = (
        f"{name} marked present at {time}"
    )

    logging.info(message)

    print(message)



mark_attendance("Gopika")