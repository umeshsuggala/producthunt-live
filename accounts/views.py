from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib import auth
# Create your views here.
def signup(req):
	if req.method=='POST':
		pwd=req.POST['pwd']
		cpwd=req.POST['cpwd']
		uname=req.POST['uname']
		try:
			if pwd==cpwd:
				user=User.objects.get(username=uname)
				return render(req,'signup.html',{'error':'username already taken'})
			else:
				return render(req,'signup.html',{'error':'password not matched'})

		except User.DoesNotExist:
			if pwd==cpwd:
				user=User.objects.create_user(uname,password=pwd)
				auth.login(req,user)
				return redirect('login')
			else:
				return render(req,'signup.html',{'error':'password not matched'})
	return render(req,'signup.html')
		





	


	# Create your views here.
def login(req):
	if req.method=='POST':
		uname=req.POST['uname']
		pwd=req.POST['pwd']
		user=auth.authenticate(username=uname,password=pwd)
		if user is not None:
			auth.login(req,user)
			return redirect('home')
		else:
			return render(req,'login.html',{'error':'username and password not matched'})
	

	return render(req,'login.html')
	

	# Create your views here.
def logout(req):
	if req.method=='POST':
		auth.logout(req)
		return redirect('home')



	return render(req,'products/home.html')
	