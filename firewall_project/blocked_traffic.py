import logging

class BlockedTrafficLogger:
    def __init__(self, log_file="blocked_traffic.log"):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

    def log(self, packet):
        logging.info(f"Blocked packet: {packet.summary()}")
