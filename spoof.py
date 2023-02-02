#!/usr/bin/env python3

import os
import sys
import argparse
from scapy.all import *

def main():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--file', '-f', help="input pcap file")
    parser.add_argument('--count', '-c', type=int, default=5, help="Amount of times to send the packets to the spoofed adres")
    parser.add_argument('--interval', '-i', type=float, default=0.1, help="interval between packets, defaults to 0.1 seconds")
    parser.add_argument('--dest_ip', '-d', default='127.0.0.1', help="dest_ip to spoof the packets to")
    params = parser.parse_args()    

    #Read input pcap
    pkts = rdpcap(params.file)
    
    #Change IP, and remove checksum so scapy recalc it, otherwise we get a bad checksum
    for p in pkts:
        p[IP].dst = params.dest_ip
        del p.chksum
        del p[UDP].chksum

    #and lets send the packets
    count = 0
    while (count < params.count):
        try:
            for p in pkts:
                sendp(p)
        except Exception as e:
            sys.stderr.write('Error: {0}'.format(e))
            sys.exit(1)
        count +=1
        time.sleep(params.interval)

if __name__ == '__main__':
    main()

    