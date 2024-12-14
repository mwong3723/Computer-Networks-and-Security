class FirewallLogger:
    def __init__(self, log_file="firewall.log"):
        self.log_file = log_file
        with open(self.log_file, "w") as f:
            f.write("Firewall Log\n")

    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(f"{message}\n")