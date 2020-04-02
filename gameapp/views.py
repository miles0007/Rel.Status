from django.shortcuts import render,redirect
from gameapp.models import cls
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def add(request):
    return render(request,'start.html')
@csrf_exempt
def sec(request):
    global opt
    if request.method == "POST":
        name = request.POST['f_name']
        second = request.POST['s_name']
        html_f = request.POST['f_name']
        html_s = request.POST['s_name']
        name = name.replace(" ", "")
        second = second.replace(" ", "")
        name = name.lower()
        second = second.lower()



        for i in name:
            for j in second:
                if i == j:
                    name = name.replace(i, "", 1)
                    second = second.replace(i, "", 1)
                    break
        char = len(name + second)

        if char > 0:
            opt = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

            while len(opt) > 1:
                count = (char % len(opt)) - 1
                if count >= 0:
                    left = opt[:count]
                    right = opt[count + 1:]
                    opt = right + left
                else:
                    opt = opt[:len(opt) - 1]
            opt = opt[0]

        else:
            opt = 'none'
        a = cls(name1=html_f,name2=html_s,result=opt)
        a.save()
    return render(request,'result.html',{'opt':opt})


