from scapy.all import DNS, DNSQR, IP, sr1, UDP

dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.google.co.in'))

for details in dns_req[IP]:
    for field in details:
        print(field)

answer = sr1(dns_req, verbose=0)

print(dns_req[IP].summary())
print(answer[UDP].summary())
print(answer[DNS].summary())