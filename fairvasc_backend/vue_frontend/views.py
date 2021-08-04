from django.shortcuts import render

# Create your views here.
def vueHomePage(request):
	return render(request, 'vue_frontend/vue_app.html')
