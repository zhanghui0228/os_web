from django.http import HttpResponse, JsonResponse
from . import check_option


# 定义首页
def index(request):
    return HttpResponse("this is index")


# 定义检查项
def check(request):
    info = {
        "option1": check_option.local_system(),
        "option2": check_option.useagent()
    }
    return JsonResponse(info)