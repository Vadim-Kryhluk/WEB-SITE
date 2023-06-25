from django.urls import path

from .views import *

urlpatterns = [
    path('', WebHome.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('about_shop/', AboutShop.as_view(), name='about_shop'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('contacts/', OurContacts.as_view(), name='contacts'),
    path('pay/', pay_page, name='pay_page'),  #<slug:pay_slug>/
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', UserProfile.as_view(), name='user_profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('template_for_web/', template, name='template'),
    path('category/<slug:cat_slug>', WebCategory.as_view(), name='category'),

]