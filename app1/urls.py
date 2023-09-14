from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("",views.index),
    path("about/",views.about),
    path('contact/',views.contact),
    path('blog/',views.blog),
    path('shop/',views.shop),
    path('updatecart/',views.updatecart),
    path('cart/',views.cart),
    path('addcart/',views.addcart),
    path('checkout/',views.checkout),
    path('wish/',views.wishlist),
    path('product/',views.product),
    path('baudio/',views.baudio),
    path('bgallery/',views.bgallery),
    path('bimage/',views.bimage),
    path('bvideo/',views.bvideo),
    path('bsidebar/',views.bright),
    path('login/',views.logint),
    path('register/',views.register),
    #admin
    path('admin-index/',views.ind),
    path("base/",views.base),
    path("form/",views.form),
    path("product/",views.product),
    path("addpro/",views.addprod),
    path('admin-login/',views.admin_login),
    path('prod-update/',views.prod_update),
    path('prod_delete/',views.prod_delete),
    path('modal/',views.prod_modal)
]
