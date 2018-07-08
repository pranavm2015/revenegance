from django.shortcuts import render
from .models import user
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home (request) :
	if 'email' in request.session:
		if request.method == 'POST' :
			try:
				del request.session['email']
			except:
				pass
			return render(request, 'home.html', {})
			    
		return render(request, 'dash.html', {})
	
	else:
		if request.method == 'POST':
			print(request.POST)
			form = request.POST
			if 'email' in form :
				context = { "message":"" }
				try :
					save  = user.objects.get(email=form['email'])
				except :
					context["message"] = "Email doesn't exist"
					return render(request, 'home.html', context)

				if form['password'] == save.password :
					request.session['email'] = save.email
					return render(request, 'dash.html', context)
				context["message"] = "Incorrect  Password"
				return render(request, 'home.html', context)

		if request.method == 'GET':
			return render(request, 'home.html', {})


