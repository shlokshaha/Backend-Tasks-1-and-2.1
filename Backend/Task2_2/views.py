from django.shortcuts import render

def signup(request):
    if request.method=='POST':
        info=request.POST
        
    return render(request, 'Task2_2/signup.html')
