import pyshark
from firewall_rules import BLOCKED_IPS
from state_tracking import track_connection

def packet_callback(pkt):
    try:
        # Check if the packet has an IP layer
        if hasattr(pkt, 'ip'):
            ip = pkt.ip
            # Block the packet if the source IP is in the blocked list
            if ip.src in BLOCKED_IPS:
                print(f"Blocked packet from {ip.src} to {ip.dst}")
                return  # Drop the packet

            print(f"Packet {ip.src} -> {ip.dst}, Protocol: {pkt.transport_layer}")
            
            # Track TCP/UDP connections
            if hasattr(pkt, 'tcp'):
                tcp = pkt.tcp
                track_connection(ip.src, ip.dst, tcp.srcport, tcp.dstport)
            elif hasattr(pkt, 'udp'):
                udp = pkt.udp
                track_connection(ip.src, ip.dst, udp.srcport, udp.dstport)
    except Exception as e:
        print(f"Error processing packet: {e}")

def main(interface='en0'):
    # Start live capture using pyshark
    cap = pyshark.LiveCapture(interface=interface)
    print(f"Started capturing on interface {interface}...")

    for pkt in cap.sniff_continuously():
        packet_callback(pkt)

if __name__ == '__main__':
    interface = 'en0'  # Specify your network interface
    main(interface)
