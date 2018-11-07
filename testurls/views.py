from django.http import HttpResponse

def index(request):
    return HttpResponse('index')

def articlelist(request):
    return HttpResponse('articlelist')

# 传过来的参数都是字符串类型

def articleyeara(request, a):
#  参数a 可为任意合法字符串
    return HttpResponse(a + '年文章列表')

def articlemonthb(request,a, b):
#  参数a, b  可为任意合法字符串, 按url 顺序赋值
    return HttpResponse(a + b + '月文章列表')

def articlecontent(request, id):
    # 该参数year 必须 固定为year
    return HttpResponse('id 为' + id + '的文章内容文章列表')

def articlepagelist(request, num, page):
    return HttpResponse('第' + page + '页,共获取到' + num + '文章')

def articlelabel(request, label):
    return HttpResponse('标签为' + label + '文章列表')
