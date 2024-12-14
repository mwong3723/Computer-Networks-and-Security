class RuleManager:
    def __init__(self):
        self.rules = {"block_ips": [], "block_ports": []}

    def add_ip_rule(self, ip):
        self.rules["block_ips"].append(ip)

    def add_port_rule(self, port):
        self.rules["block_ports"].append(port)

    def should_block(self, packet):
        ip = packet["IP"].src if "IP" in packet else None
        port = packet["TCP"].sport if "TCP" in packet else None

        if ip in self.rules["block_ips"] or port in self.rules["block_ports"]:
            return True
        return False