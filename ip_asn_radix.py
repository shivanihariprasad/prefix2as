import radix
import gzip

rtree = radix.Radix()
with gzip.open('/home/c4du/caida-ipv4-20250201-0000.pfx2as.gz ', 'rt') as f:
    for line in f:
        data = line.strip().split()
        rnode = rtree.add(data[0]+'/'+data[1])
        rnode.data['ASN'] = data[2]

def prefix_lookup(p):
    rnode = rtree.search_best(p)
    if rnode is not None:
        return rnode.data['ASN']
    else:
        return 'noasn'