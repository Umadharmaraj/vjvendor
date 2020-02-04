from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('vendors', views.vendors, name='vendors'),
    path('addVendor', views.add_vendor, name='add_vendor'),
    path('vendorRegister',views.vendor_register,name='vendor_register'),
    path('editVendorDetails', views.edit_vendor_details, name='edit_vendor_details'),
    path('updateVendor',views.updateVendor, name='updateVendor'),
    path('deleteVendorDetails', views.delete_vendor_details, name='delete_vendor_details'),
    path('tableInfo',views.table_info, name='table_info'),
    path('traders', views.traders, name='traders'),
    path('viewmore',views.viewmore, name="viewmore"),
    path('confirm', views.confirm, name='confirm'),


]