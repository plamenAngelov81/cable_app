from django.urls import path, include

from cable_app.users.views import AccountRegisterView, AccountLogin, AccountLogOut, AccountDetailsView, \
    AccountEditView, AccountDeleteView

urlpatterns = [
    path('profile/', include([
        path('register/', AccountRegisterView.as_view(), name='account register'),
        path('login/', AccountLogin.as_view(), name='account login'),
        path('logout/', AccountLogOut.as_view(), name='account logout'),
        path('<int:pk>/', AccountDetailsView.as_view(), name='account details'),
        path('edit/<int:pk>/', AccountEditView.as_view(), name='account edit'),
        path('delete/<int:pk>/', AccountDeleteView.as_view(), name='account delete'),
    ])),
]
