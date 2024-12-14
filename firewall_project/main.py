from scapy.all import sniff, conf
from packet_sniffer import PacketSniffer
from rule_manager import RuleManager
from statefule import StatefulInspection
from blocked_traffic import BlockedTrafficLogger
from logger import FirewallLogger

# Enable pcap support in Scapy
conf.use_pcap = True

# Initialize components
logger = FirewallLogger()
rule_manager = RuleManager()
stateful_inspection = StatefulInspection()
blocked_logger = BlockedTrafficLogger()

def process_packet(packet):
    if rule_manager.should_block(packet) or not stateful_inspection.is_valid(packet):
        blocked_logger.log(packet)
    else:
        logger.log(f"Allowed packet: {packet.summary()}")

def main():
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()