from django.conf.urls import url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'payee', views.PayeeViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'customer_account', views.CustomerAccountViewSet)
router.register(r'fund_transfer', views.FundTransferViewSet)


urlpatterns = router.urls
urlpatterns += [
    url(r'^same_bank_add_payee_form$', views.same_bank_add_payee_form, name='same_bank_add_payee_form'),
    url(r'^same_bank_fund_transfer_form$', views.same_bank_fund_transfer, name='same_bank_fund_transfer_form'),
    url(r'^same_bank_fund_transfer_list$', views.same_bank_fund_transfer_list, name='same_bank_fund_transfer_list'),
    url(r'^other_bank_add_payee_form$', views.other_bank_add_payee_form, name='other_bank_add_payee_form'),
    url(r'^other_bank_fund_transfer_form$', views.other_bank_fund_transfer, name='other_bank_fund_transfer_form'),
    url(r'^other_bank_fund_transfer_list$', views.other_bank_fund_transfer_list, name='other_bank_fund_transfer_list'),
]
