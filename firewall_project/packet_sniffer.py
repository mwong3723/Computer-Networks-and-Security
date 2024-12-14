from scapy.all import sniff

class PacketSniffer:
    def __init__(self):
        self.packets = []

    def capture_packets(self, count=10):
        self.packets = sniff(count=count)
        return self.packets