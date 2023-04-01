from django.shortcuts import render
# Create your views here.
def student_login(r):
    return render(r,'AttedenceStatistics/logindata.html')
def student_detail(r):
    roll=r.POST['roll']
    pass  


