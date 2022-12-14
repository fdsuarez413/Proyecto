from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        if request.POST.get('stripeToken'):

            if not request.user.has_customer():
                request.user.create_customer_id()
    
    return render(request, 'billing_profiles/create.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })