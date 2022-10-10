from audioop import reverse
from django.http import HttpResponseRedirect
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from cart.utils import get_or_create_cart
from .models import ShippingAddres
from .forms import ShippingAddressForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from cart.utils import get_or_create_cart
from orders.utils import get_or_create_order
# Create your views here.


class ShippingAddressListview(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ShippingAddres
    template_name = 'shipping_addresses/shipping_addresses.html'
    
    def get_queryset(self):
        return ShippingAddres.objects.filter(user=self.request.user).order_by('-default')

class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = ShippingAddres
    form_class = ShippingAddressForm
    template_name = 'shipping_addresses/update.html'
    success_message = 'Direccion Actualizada exitosamente'

    def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('cart:cart')
        
        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)
            
class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddres
    template_name = 'shipping_addresses/delete.html'
    success_url = reverse_lazy('shipping_addresses:shipping_addresses')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_addresses:shipping_addresses')
        
        if request.user.id != self.get_object().user_id:
            return redirect('cart:cart')
        
        if self.get_object().has_orders():
            return redirect('shipping_addresses:shipping_addresses')
     
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)
        
@login_required(login_url='login')   
def create(request):
    form = ShippingAddressForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not request.user.has_shipping_address()
        
        shipping_address.save()
        
        if request.GET.get('next'):
            if request.GET['next'] == reverse('orders:address'):
                cart = get_or_create_cart(request)
                order = get_or_create_order(cart, request)
                
                order.update_shipping_address(shipping_address)
                
                return HttpResponseRedirect(request.GET['next'])
        
        messages.success(request, 'Direccion creada exitosamente')
        return redirect('shipping_addresses:shipping_addresses')
    
    return render(request, 'shipping_addresses/create.html', {
        'form':form
    })

@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddres, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('cart:cart')

    if request.user.has_shipping_address():
        request.user.shipping_address.update_default()

    shipping_address.update_default(True)

    return redirect('shipping_addresses:shipping_addresses')