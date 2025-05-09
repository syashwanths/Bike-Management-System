from django.urls import path
from viewsapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Allcompanies.as_view(),name='list'),
    path('<int:pk>',views.CompanyDetail.as_view(),name='detail'),
    path('create',views.Addcompany.as_view(),name='create'),
    path('edit/<int:pk>',views.EditCompany.as_view(),name='edit'),
    path('delete/<int:pk>',views.DeleteCompany.as_view(),name='delete'),
    path('emi/<int:id>',views.EmiCalulator,name='emi')
    
] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)