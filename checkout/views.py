from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MmNj9KSG7N8mbvfp0osX4bA8yfYs6bzt5kAm4A9QQS4nAq5LDtJHTZVHE8WnR3dThzbO4z4Na7N5iKJNyM0woUc00AUrnLYJ1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

