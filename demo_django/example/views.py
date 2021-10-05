from django.http import HttpResponse

# Create your views here.
def special_case_2003(*args, **kwargs):
    return HttpResponse("Hello, World!", content_type='text/plain')
