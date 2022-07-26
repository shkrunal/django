from django.conf import settings
from django.urls import path
from gbc.views import bodyskin,logout, home, price,productall,products,proview,productdelete,women,men,accessory,cosmetics,cart,about,minus,plus,delete,add_to_cart
from django.conf.urls.static import static
urlpatterns = [
    path("",home,name='home'),
    path("women/",women,name='women'),
    path("men/",men,name='men'),
    path("products/",products,name='product'),
    path("proall/",productall,name='productall'),
    path('logout/',logout,name='logout'),
    path("proview/<int:abc>/",proview,name='proview'),
    path('pd/<int:id>/',productdelete,name='productdelete'),

    path("accessory/",accessory,name='accessory'),
    path("cosmetics/",cosmetics,name='cosmetics'),
    path("body&skin/",bodyskin,name='body'),
    path("cart",cart,name='cart'),
    path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),
    path("about/",about,name='about'),
    
    path('minus/<int:id>',minus,name='minus'),
    path('plus/<int:id>',plus,name='plus'),
    path('price/<int:id>',price,name='price'),
    path('delete/<int:id>',delete,name='delete'),
    # path('cal/',calculator,name='cal')
    # path('register/',register,name='register')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)