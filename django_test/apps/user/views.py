from django.shortcuts import render
from django.views import View
from user.models import UserInfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class UserList(View):
    """
    用户列表展示
    """
    def get(self, request):
        return render(request, 'user/user_list.html')


class UserQuery(View):
    """
    用户信息查询
    """

    def post(self, request):
        user_list = UserInfo.objects.get_queryset().order_by('id')
        data = dict()
        data_items = []
        for item in user_list:
            user_dict = {"username": item.username, "age": item.age, "sex": item.sex, "mobile": item.mobile,
                         "address": item.address}
            data_items.append(user_dict)
        data.__setitem__("data", data_items)
        data.__setitem__("code", 0)
        data.__setitem__("msg", "")
        data.__setitem__("count", len(user_list))
        return JsonResponse(data)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserQuery, self).dispatch(*args, **kwargs)