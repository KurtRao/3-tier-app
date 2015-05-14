# Create your views here.
import subprocess
from django.http import HttpResponse

def view(request):
    p=subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
    p.wait()
    content = p.stdout.read()
    ret = "<html><head></head><body><p>" + content + "</p></body></html>"
    return HttpResponse(ret)
