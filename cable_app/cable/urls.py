from django.urls import path, include

from cable_app.cable.views import index, CableCreate, CableDetailsView, CableEditView, CableDeleteView, order_cable, \
    EditOrderView

urlpatterns = [
    path('', index, name='index'),
    path('create/', CableCreate.as_view(), name='create cable'),
    path('cable/', include([
        path('details/<int:pk>/', CableDetailsView.as_view(), name='cable details'),
        path('edit/<int:pk>/', CableEditView.as_view(), name='cable edit'),
        path('delete/<int:pk>/', CableDeleteView.as_view(), name='cable delete'),
        path('<int:pk>/order/', order_cable, name='cable order'),
    ])),
    path('confirm-order/<int:pk>', EditOrderView.as_view(), name='confirm order')
]
