from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt


@login_required
def show_product_page(request):
    return render(request,'itemdata.html')

