from django.urls import path, include
from . import views

urlpatterns = [
    path('causes/', views.CauseView, name='cause'),
    path('projects/<slug>/', views.project_donate, name='projectdonate'),
    path('causes/<slug>/', views.causes_donate, name='causesdonate'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process-paypal/', views.process_paypal, name='process_paypal'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled,
         name='payment_cancelled'),
    path('transaction/', views.save_transaction, name='transaction'),
    path('', views.donate_view, name='donate'),
]
