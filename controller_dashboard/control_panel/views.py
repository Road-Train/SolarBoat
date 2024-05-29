from django.shortcuts import render

def dashboard(request):
    return render(request, 'control_panel/dashboard.html')
