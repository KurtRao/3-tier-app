import uuid
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

print get_mac_address()

import subprocess
p=subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
p.wait()
content = p.stdout.read()
print content
