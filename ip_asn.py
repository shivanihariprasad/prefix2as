import _pyipmeta 
import argparse
import json
# parser = argparse.ArgumentParser()
# parser.add_argument('-i', dest = 'ips_file', default = '', help = 'Please enter the file name of the ips file')
# args = parser.parse_args()


ipm = _pyipmeta.IpMeta()

# print("Getting/enabling pfx2as provider (using included test data)")
prov = ipm.get_provider_by_name("pfx2as")
print(ipm.enable_provider(prov, "-f https://publicdata.caida.org/datasets/routing/routeviews-prefix2as/2025/01/routeviews-rv2-20250114-2000.pfx2as.gz"))
print()

# Create list of ips from test file 
ips = []
with open("ips.txt", "r") as f:
    for line in f:
        line = line.strip()
        ips.append(line)


# Map between ipv4 addresses and origin asns
ip2asn = {}
for ip in ips:
    if ipm.lookup(ip):
        (res,) =  ipm.lookup(ip)
        if res.get('asns'):
            ip2asn[ip] = res.get('asns')[-1]

 
#print(ip2asn)

with open('ipstoasn.json', 'w') as f:
    json.dump(ip2asn, f, indent=4)