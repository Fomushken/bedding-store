from django.urls import path
from . import views


urlpatterns = [
    path('', views.AerienHome.as_view(), name='home'),
    path('contacts/', views.AerienContacts.as_view(), name='contacts'),
    path('catalog/<slug:category_slug>', views.AerienCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', views.ShowProduct.as_view(), name='show_product'),
    path('reviews/<slug:product_slug>', views.ProductReview.as_view(), name='reviews'),
    path('reviews/<slug:product_slug>/create', views.ProductsReviewCreate.as_view(), name='create_review')
]
