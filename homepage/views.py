from django.shortcuts import render

def index(request):
    return render(request, 'web/songzi/watersunEnglish.html')

def photoandfishEnglish(request):
    return render(request, 'web/songzi/photoandfishEnglish.html')

def friends(request):
    return render(request, 'web/songzi/friends.html')

def myselfEnglish(request):
    return render(request, 'web/songzi/myselfEnglish.html')

def watersun(request):
    return render(request, 'web/songzi/watersun.html')

def chen(request):
    return render(request, 'web/chen/zhiyang-chen.html')

def chen(request):
    return render(request, 'web/chen/zhiyang-chen.html')
