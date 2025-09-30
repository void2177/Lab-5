def is_valid_part(part):
    part = str(part)
    if len(part) > 1 and part[0] == "0":
        print("Invalid!")
        return False
    else:
        part=int(part)
        if part >= 0:
             if part < 256:
                 print("Valid!")
                 return True
        else:
                print("Invalid!")
                return False
##is_valid_part("1")

def is_valid_ip(ip):
    iplist = ip.split(".")
    if len(iplist) != 4:
        print("Invalid!")
        return False
    else:
        for i in iplist:
          is_valid_part(i)

## is_valid_ip("01.168.127.12")