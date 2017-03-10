from django.http import HttpResponse, Http404
from django.shortcuts import render
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    raw_sql = 'select * from webshop_product where id=' + product_id
    raw_querySet = Product.objects.raw(raw_sql)
    for obj in raw_querySet:
        return render(request, 'webshop/product_view.html', {'product':obj})
        #HttpResponse("{}".format(raw_querySet))
    raise Http404("Product does not exist")

def available_products(request):
    raw_sql = 'select * from webshop_product where quantity>0'
    raw_querySet = Product.objects.raw(raw_sql)
    return render(request, 'webshop/product_list.html', {'products':raw_querySet})
    #HttpResponse("View not implemented!")
