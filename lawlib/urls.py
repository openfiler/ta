from django.urls import path
from lawlib import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', views.DocumentListView.as_view(), name='docs'),
    path('docs/<int:pk>', views.DocumentDetailView.as_view(), name='document-detail'),
    path('rules/', views.ProvisionListView.as_view(), name='rules'),
    path('taxreturn/', views.TaxReturnListView.as_view(), name='taxreturn'),
    path('form/<int:pk>', views.TaxReturnDetailView.as_view(), name='taxreturn-detail'),
    path('rules/<int:pk>', views.ProvisionDetailView.as_view(), name='provision-detail'),
]
