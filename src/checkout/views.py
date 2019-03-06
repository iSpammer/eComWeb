from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# Login_required is used for enforcing login to view this page
@login_required
def checkout(request):
	context = {}
	template = 'checkout.html'
	return render(request, template, context)