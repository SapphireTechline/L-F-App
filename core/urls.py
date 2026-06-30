from django.urls import path
from core.views  import *

urlpatterns=[
   path('',  index ,name="homepage"),
   path("login" ,login_view,name="login"),
   path("register", register,name="register" ),
   path("logout", signout, name="signout"),
   path('submit' ,submit_item ,name='submit_page'),
   path('items',all_item,name='all_item_page'),
   path('my_posts', my_posts, name='my_posts'),
   path('delete/<id>/', delete_item, name='delete_item'),

] 