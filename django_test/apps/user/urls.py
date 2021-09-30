from django.urls import path
from user.views import UserList, UserQuery

app_name = 'user'

urlpatterns = [
    # 用户列表展示
    path('list/', UserList.as_view(), name="user_list"),
    # 用户相关数据查询
    path('query/', UserQuery.as_view(), name="user_query"),
]

