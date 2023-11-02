from django.urls import path 
from .  import views

app_label = 'product'

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='get_list_create_product'),
    path('<int:pk>', views.ProductDetail.as_view(), name='detail_product'),

    # a crud in one view
    # path('', views.ProductCRUD.as_view()),
    # path('<int:pk>', views.ProductCRUD.as_view()),
]
