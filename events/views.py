from django.http import HttpResponse

def home(request):
    return HttpResponse("Online Event Registration System")

def demo_eval(request):
    value = request.GET.get("value", "1+1")
    result = eval(value)
    return HttpResponse(str(result))