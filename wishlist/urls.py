from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_in_xml
from wishlist.views import show_wishlist_in_json 
from wishlist.views import show_data_json 
from wishlist.views import show_data_xml
#TUTORIAL 3
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user 

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_in_xml, name='show_wishlist_in_xml'),
    path('json/', show_wishlist_in_json, name='show_wishlist_in_json'),
    path('json/<int:id>', show_data_json, name='show_data_json'), 
    path('xml/<int:id>', show_data_xml, name='show_data_xml'),
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),

]