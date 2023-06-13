from django.urls import path

from store.views import marketplace, search_view, main_page,user_login,user_detail,to_login_html,signup,to_Recharge_html,to_mian,change_User,delete_User
from store.views import settings,to_sign_up,main_page_already_login,to_user_detail,logout,upload,to_upload_html,buy_someting,Recharge,sale,get_uuid,to_order_management
from store.views import backstage_login,backstage_user_login,backstage_user_detail,backstage_already_login,to_Product_Management,change_Product,delete_Product,to_User_Management
#CategoryList
urlpatterns = [
    path('', main_page, name="main-page"),
    path('marketplace/', marketplace, name='marketplace'),
    path('search/', search_view, name="search"),
    path('user_login',user_login,name='user_login'),
    path('user_detail/',user_detail,name='user_detail'),
    path('to_login_html/',to_login_html,name='to_login_html'),
    path('signup/',signup,name='signup'),
    path('settings/',settings,name='settings'),
    path('to_sign_up/',to_sign_up,name='to_sign_up'),
    path('main_page_already_login/',main_page_already_login,name='main_page_already_login'),
    path('to_user_detail/',to_user_detail,name='to_user_detail'),
    path('logout/',logout,name='logout'),
    path('upload/',upload,name='upload'),
    path('to_upload_html/',to_upload_html,name='to_upload_html'),
    path('buy_someting/',buy_someting,name='buy_someting'),
    path('Recharge/',Recharge,name='Recharge'),
    path('to_Recharge_html/',to_Recharge_html,name='to_Recharge_html'),
    path('sale/',sale,name='sale'),
    path('to_mian/',to_mian,name='to_mian'),
    path('marketplace/<str:uuid>/',get_uuid,name='get_uuid'),
    path('backstage_login/',backstage_login,name='backstage_login'),
    path('backstage_user_login/',backstage_user_login,name='backstage_user_login'),
    path('backstage_user_detail/',backstage_user_detail,name='backstage_user_detail'),
    path('backstage_already_login/',backstage_already_login,name='backstage_already_login'),
    path('to_Product_Management/',to_Product_Management,name='to_Product_Management'),
    path('change_Product/',change_Product,name='change_Product'),
    path('delete_Product/',delete_Product,name='delete_Product'),
    path('to_User_Management/',to_User_Management,name='to_User_Management'),
    path('change_User/',change_User,name='change_User'),
    path('delete_User/',delete_User,name='delete_User'),
    path('to_order_management/',to_order_management,name='to_order_management'),
]
