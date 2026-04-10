from scapy.all import rdpcap
from collections import Counter

# Load the pcap file
packets = rdpcap("24bce5420.pcapng")

# Number of packets
print("Number of packets:", len(packets))

src_ips = set()
dst_ips = set()
protocols = []

for pkt in packets:
    if pkt.haslayer("IP"):
        src_ips.add(pkt["IP"].src)
        dst_ips.add(pkt["IP"].dst)
        protocols.append(pkt["IP"].proto)

print("Number of Source IPs:", len(src_ips))
print("Number of Destination IPs:", len(dst_ips))
print("Number of Protocols used:", len(set(protocols)))

print("\nNumber of packets under every protocol:")
protocol_count = Counter(protocols)
for proto, count in protocol_count.items():
    print(f"Protocol {proto}: {count}")
