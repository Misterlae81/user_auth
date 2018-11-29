from django.conf.urls import url, include
from basic_app import views

app_name = 'basic_app'
urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^test_file/$',views.test_file,name='test_file'),
    url(r'^register/$',views.register,name='register'),
    #url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/$',views.special,name='special'),
    url(r'^user_login/$',views.user_login,name='user_login')
]
