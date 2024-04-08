
# interface/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login



def index(request):
    
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
             user_login(request,user)
             return dashboard(request)
        else:
             messages.error(request,"Invalid Credentials.")
             return render(request, 'login.html')
        # return dashboard(request)
    
def dashboard(request):
    # Dummy student names (Replace with actual data retrieval from database)
        students = ['Student 1', 'Student 2', 'Student 3']

        # Dummy student information (Replace with actual data retrieval from database)
        student_info = {
            'student_name': 'NA',
            'btech': 'NA',
            'gate_score': 'NA',
            'gate_subject': 'NA',
            'year_of_passing': 'NA',
            'currently_employed': 'NA',
            'company_name': 'NA'
        }

        # Dummy panel members (Replace with actual data retrieval from database)
        panel_members = ['Panel Member 1', 'Panel Member 2', 'Panel Member 3']
        return render(request,'dashboard.html', {'students': students, 'student_info': student_info, 'panel_members': panel_members})

def logout(request):
    return render(request,'login.html')