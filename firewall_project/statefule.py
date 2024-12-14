class StatefulInspection:
    def __init__(self):
        self.active_connections = set()

    def is_valid(self, packet):
        if "TCP" in packet:
            src = packet["IP"].src
            dst = packet["IP"].dst
            sport = packet["TCP"].sport
            dport = packet["TCP"].dport

            connection = (src, sport, dst, dport)
            reverse_connection = (dst, dport, src, sport)

            if connection in self.active_connections or reverse_connection in self.active_connections:
                return True
            elif packet["TCP"].flags == "S":  # SYN flag
                self.active_connections.add(connection)
                return True
        return False
