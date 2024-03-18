from django.urls import path
from . import views
app_name='registerapp'


urlpatterns = [
      path('sign_in/', views.sign_in,name='sign_in'),
      path('login/', views.login,name='login'),
      path('logout/',views.logout,name='logout'),
      path('profile/', views.view_profile, name='view_profile')
#       path('edit_profile/', views.edit_profile, name='edit_profile'),
]