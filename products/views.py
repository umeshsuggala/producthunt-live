from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(req):
	product=Product.objects
	return render(req,'products/home.html',{'products':product})

@login_required(login_url='login')
def create(req):
	if req.method=='POST':
		if req.POST['title'] and req.POST['body'] and req.FILES['icon'] and req.FILES['image'] and req.POST['url']:
			product=Product()
			product.title=req.POST['title']
			product.body=req.POST['body']
			
			if req.POST['url'].startswith('http://') or req.POST['url'].startswith('https://'):
				product.url=req.POST['url']
			else:
				product.url='http://'+req.POST['url']

			product.icon=req.FILES['icon']
			product.image=req.FILES['image']
			product.pub_date=timezone.datetime.now()
			product.hunter = req.user
			product.save()
			return redirect('/products/'+str(product.id))

		else:
			return render(req,'products/create.html',{'error':'something is missing'})
	else:
		return render(req,'products/create.html')
	return render(req,'products/create.html')
def detail(req,product_id):
	product=get_object_or_404(Product,pk=product_id)
	return render(req,'products/detail.html',{'product':product})
@login_required(login_url='login')
def upvote(req,product_id):
	if req.method=='POST':
		product=get_object_or_404(Product,pk=product_id)
		product.votes+=1
		product.save()
		return redirect('/products/'+str(product.id))
