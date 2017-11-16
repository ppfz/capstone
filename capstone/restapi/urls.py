from .views import*
from django.conf.urls import url

urlpatterns = [
    url(r'^menu/',menu_list2),
    url(r'^order_item/',order_item),	   
    url(r'^admin/', admin.site.urls),
    url(r'^menus/(\w+)',menu_list),
    url(r'^menu_item/(\w+)',menu_item),
    url(r'^create_order/',new_order),
    url(r'^resturant/(\w+)',get_res_info),
    url(r'^pay/',pay),
]
