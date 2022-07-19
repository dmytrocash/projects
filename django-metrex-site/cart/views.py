# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from products.models import Product
# from django.db.models import Sum
# from .forms import OrderForm

# def index(request):
# 	template = loader.get_template('cart/cart.html')

# 	ids = request.session.get('goods', list())
# 	goods = Product.objects.filter(id__in = ids)
# 	sum = goods.aggregate(Sum('price')).get('price__sum')
# 	context = {
# 		'goods': goods,
# 		'sum': sum,
#         'form': OrderForm()
# 	}

# 	return HttpResponse(template.render(context))

# def add(request):
# 	id = int(request.GET['id'])

# 	if not 'goods' in request.session:
# 		request.session['goods'] = [id]
# 		return(HttpResponse())

# 	ids_set = set(request.session['goods'])
# 	ids_set.add(id)
# 	request.session['goods'] = list(ids_set)

# 	return HttpResponse()

# def remove(request):
# 	id = int(request.GET['id'])

# 	saved_list = request.session['goods'];
# 	saved_list.remove(id)
# 	request.session['goods'] = saved_list;

# 	return HttpResponse()


# import json

# def chosenIds(request):
# 	ids_list = list()
# 	if 'goods' in request.session:
# 		ids_list = request.session['goods']

# 	json_ids = json.dumps(ids_list)
# 	response = HttpResponse(json_ids)
# 	response['Content-Type'] = "application/json"
# 	return response

# def removeAll(request):
# 	request.session.clear()
# 	return(HttpResponse())

# from django.http import HttpResponseRedirect
# from .models import Order

# def handler(request):
# 	order = Order(
# 		client_name = request.GET['client_name'],
# 		phone = request.GET['phone'],
# 	)
# 	order.save()

# 	for id in request.session['goods']:
# 		print(id)
# 		order.goods_ids.add(id)

# 	request.session.clear()
# 	return HttpResponseRedirect('/cart/thanks/')


# def thanks(request):
# 	template = loader.get_template('cart/thanks.html')
# 	return HttpResponse(template.render());

