# from scapy.all import conf
# conf.use_pcap = True
# print(f"PCAP active: {conf.use_pcap}")

# from scapy.all import conf
# from scapy.all import sniff
# print(conf.ifaces)
# packets = sniff(prn=process_packet, iface="en0", store=False)
# packets.summary()

from scapy.arch.pcapdnet import PcapDnetDevice
print(PcapDnetDevice.is_available())
