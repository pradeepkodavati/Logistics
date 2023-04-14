from logisticsapp import views
from django.urls import path

from logisticsapp.views import MyPasswordResetView





urlpatterns = [
    path("register/", views.register, name="register"),  # <-- added
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("forgotpassowrd/", views.MyPasswordResetView.as_view(), name="forgotpassword"),
    path('home/', views.routeLogistics_list, name='home'),
    path('<int:pk>/', views.routeLogistics_detail, name='routeLogistics_detail'),
    path('create/', views.routeLogistics_create, name='routeLogistics_create'),
    path('<int:pk>/update/', views.routeLogistics_update, name='routeLogistics_update'),
    path('<int:pk>/delete/', views.routeLogistics_delete, name='routeLogistics_delete'),
    # path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]