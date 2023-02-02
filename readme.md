# UDP spoofing
Simple UDP spoofing script, input is a pcap with for example an DNS Response. The script will override the dest_ip and recalculate the checksums, and will send it X times to the dest_ip. 

## Setup
`pip install -r requirements.txt`
 
 ## Usage
`./spoof.py $parameters$` 
 
 ## Parameters
 `-f, --file | input pcapfile`\
 `-c, --count | Amount of times to send the packets to the spoofed adres `\
 `-i, --interval | Interval between packets, defaults to 0.1 seconds`\
 `-d, --dest_ip | dest_ip to spoof the packets to`\

 ## Example
 For example, start a tcpdump to capture a DNS response:\
`tcpdump -i any src port 53 -w test.pcap`\
Do a DNS lookup in another terminal, to get a DNS response:\
`dig google.nl ANY`\
Close the tcpdump, and use the PCAP with dns response as input for spoof.py:\
`./spoof.py -f test.pcap -c 5 -i 0.1 -d 127.0.0.1` 
