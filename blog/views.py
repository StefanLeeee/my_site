from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return render(request,'blog/index.html')
#     # return HttpResponse("Hello")
from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models
# Create your views here.

user_list = []


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        talk = request.POST.get('talk')
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, talk=talk)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'blog/index.html', {'data': user_list})