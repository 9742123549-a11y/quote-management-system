# quotes/urls.py
from django.urls import path
from .views import QuoteListCreateAPIView, QuoteRetrieveUpdateDestroyAPIView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view(), name='quote-list-create'),
    path('quotes/<int:pk>/', QuoteRetrieveUpdateDestroyAPIView.as_view(), name='quote-detail'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quotes.urls')),
]