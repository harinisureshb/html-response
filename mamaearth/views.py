from django.shortcuts import render

# Create your views here.
def face(request):
    d={'face1':'vitamin c facewash','face2':'vitamin c rice face wash'}
    return render(request,'normal.html',context=d)
def mamaearth_creams(request):
    d={'c1':'vitamin c daily glow cream','c2':'neem acne cream','c3':'vitamin c turmeric cream'}
    return render(request,'normal.html',context=d)