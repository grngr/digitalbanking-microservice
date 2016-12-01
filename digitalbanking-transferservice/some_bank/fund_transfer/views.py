from rest_framework import viewsets
from .serializers import PayeeSerializer, CustomerSerializer, CustomerAccountSerializer, FundTransferSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .models import Payee, Customer, CustomerAccount, FundTransfer


class PayeeViewSet(viewsets.ModelViewSet):
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAccountViewSet(viewsets.ModelViewSet):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer


class FundTransferViewSet(viewsets.ModelViewSet):
    queryset = FundTransfer.objects.all()
    serializer_class = FundTransferSerializer


# Create your views here.

@login_required
def same_bank_add_payee_form(request):
    # return HttpResponse("same_bank_add_payee_form")
    return render(request, 'fund_transfer/same_bank_add_payee_form.html')


@login_required
def same_bank_fund_transfer_list(request):
    # return HttpResponse("same_bank_fund_transfer_list")
    # payee_list = Payee.objects.all()
    payee_list = Payee.objects.filter(bank_code = '1234')
    return render(request, 'fund_transfer/same_bank_fund_transfer_list.html', {'payee_list': payee_list})


@login_required
def same_bank_fund_transfer(request):
    # return HttpResponse("same_bank_fund_transfer_form")
    return render(request, 'fund_transfer/same_bank_fund_transfer_form.html')


@login_required
def other_bank_add_payee_form(request):
    # return HttpResponse("other_bank_add_payee_form")
    return render(request, 'fund_transfer/other_bank_add_payee_form.html')


@login_required
def other_bank_fund_transfer(request):
    # return HttpResponse("other_bank_fund_transfer_form")
    # payee_list = Payee.objects.payee_for_customer(request.customer)
    # payee_list = Payee.objects.payee_for_customer(1)
    payee_list = Payee.objects.all()
    return render(request, 'fund_transfer/other_bank_fund_transfer_form.html', {'payee_list': payee_list})


@login_required
def other_bank_fund_transfer_list(request):
    # return HttpResponse("other_bank_fund_transfer_list")
    # payee_list = Payee.objects.all()
    payee_list = Payee.objects.exclude(bank_code='1234')
    return render(request, 'fund_transfer/other_bank_fund_transfer_list.html', {'payee_list': payee_list})
