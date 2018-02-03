from django.http import HttpResponse

def index(request):
    return HttpResponse(out("file"))

def out(path):
    with open(path) as f:
	content = f.read()
	return content