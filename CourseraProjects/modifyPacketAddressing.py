from scapy.all import *                      #import scapy
pkts = rdpcap("intro-wireshark-trace1.pcap") #load packet capture file
ct = 0
for pkt in pkts:                              # iterate a loop with if
    if Ether in pkt:                               # check if packet includes Ether
        pkt.src = '11:11:11:11:11:11'     # change source address of item to 11:11:11:11:11:11
        pkt.dst = '22:22:22:22:22:22'     # change destination address to 22:22:22:22:22:22
        ct += 1                         #count number of changed packets
              
print(ct) # print number of changed packets
        