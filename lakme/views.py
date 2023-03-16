from django.shortcuts import render

# Create your views here.
def beauty(request):
    d={'p1':'compact poweder','p2':'lip shades','p3':'eye shades'}
    return render(request,'beauty.html',context=d)
def lipsticks(request):
    d={'l1':'stawberry liplove','l2':'orange matt lipstic','l3':'lavender lipgel'}
    return render(request,'beauty.html',context=d)