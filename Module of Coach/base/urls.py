from django.urls import path
from .views import ModuleList,ModuleDetail,ModuleCreate,ModuleUpdate,ModuleDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('',ModuleList.as_view(),name='modules'),
    path('module/<int:pk>/',ModuleDetail.as_view(),name="module"),
    path('module-create/',ModuleCreate.as_view(),name='module-create'),
    path('module-update/<int:pk>/',ModuleUpdate.as_view(),name='module-update'),
    path('module-delete/<int:pk>/',ModuleDelete.as_view(),name='module-delete'),
]
