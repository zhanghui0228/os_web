from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import check_option
from . import check_site



# 定义首页
def index(request):
    local_system = check_option.useagent()
    local_port = check_option.local_service()
    return render(request, 'index.html',{'local_system': local_system, 'local_port': local_port})


# 定义检查项
def check(request):
    info = {
        "option1": check_option.local_system(),
        "option2": check_option.useagent(),
        "option3": check_option.local_disk(),
        "option4": check_option.local_service()
    }
    return JsonResponse(info)


# 定义test
def test(request):
    info = check_site.healthy()
    return HttpResponse(info)