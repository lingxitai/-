from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import user

# Create your views here.
from .models import user

warning = ''


def index(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u, p)

        user.objects.filter()
        if u == 'root' and p == 'root1234':
            return redirect('http://127.0.0.1:8000/admin')
        else:
            warning = '输入用户名或者密码错误'
            return render(request, 'index.html', {'warning': warning})
    else:
        return render(request, 'index.html')


def add_index(request):
    user_info=user.objects.all()
    username_list = []
    for i in user_info:
        username_list.append(i.username)
    if request.method == 'GET':
        return render(request, 'add_index.html')
    elif request.method =='POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        pp=request.POST.get('password_agin')
        if p != pp:
            warning = '----警告：两次密码输入需要相同'
            return render(request, 'add_index.html',{'warning':warning})
        elif len(u.strip())>=20:
            warning = '----警告：用户名不能超过20位'
            return render(request, 'add_index.html',{'warning':warning})
        elif len(u.strip())==0:
            warning = '----警告：用户名不能为空'
            return render(request, 'add_index.html',{'warning':warning})
        elif u.endswith(' ') and u.startswith(' '):
            warning = '----警告：空格为无效字符'
            return render(request, 'add_index.html',{'warning':warning})
        elif u in username_list:
            warning = '----警告：用户名已存在'
            return render(request, 'add_index.html',{'warning':warning})
        elif len(p) <8 or len(p)>8:
            warning = '----警告：密码为8位数字或字母'
            return render(request, 'add_index.html',{'warning':warning})
        else:
            user.objects.create(username=u,password=p)
            warning = '注册成功：请用注册用户登录'
            return render(request, 'index.html',{'warning':warning})
