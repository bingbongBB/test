from django.shortcuts import render
from django.http import HttpResponse
from sampleapp.models import Sample
# Create your views here.
def sayhello(request):
    return HttpResponse("hi")
def templateHello(request):
    return render(request,'HelloTemplate.html',locals())#透過locals()將要傳輸的資料打包成dict格式
    #並投過render將變數傳送給template
def post_test(request):
    data=request.POST.get('data')
    print(data)
    return render(request,'HelloTemplate.html',locals())