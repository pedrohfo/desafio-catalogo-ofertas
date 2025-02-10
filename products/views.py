from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()

    # Apply filters
    frete_gratis = request.GET.get('frete_gratis')
    tipo_entrega = request.GET.get('tipo_entrega')
    sort_by = request.GET.get('sort_by')

    if frete_gratis == 'true':
        products = products.filter(frete_gratis=True)
    if tipo_entrega == 'Full':
        products = products.filter(tipo_entrega='Full')

    # Apply sorting
    if sort_by == 'high_price':
        products = products.order_by('-preco')
    elif sort_by == 'low_price':
        products = products.order_by('preco')
    elif sort_by == 'high_discount':
        products = products.order_by('-percentual_desconto')

    return render(request, 'products/product_list.html', {'products': products})