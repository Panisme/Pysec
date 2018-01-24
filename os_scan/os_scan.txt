#!/usr/bin/env python
import nmap
import sys
###############

def main():
    if len(sys.argv) !=2:
        print 'Usage:python  %s  {IP} '%sys.argv[0]
        sys.exit()
    IP=sys.argv[1]
    print 'IP:%s for OS scanning ......'%IP
    nm=nmap.PortScanner()
    nm.scan(hosts=IP,arguments='-O')
    if nm.has_host(IP):
        result=nm[IP]['osmatch'][0]
        print result['name']
    else:
        print 'NO message'

##############
if __name__=="__main__":
    main()   
