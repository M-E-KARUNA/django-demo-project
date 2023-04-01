from django.shortcuts import render,redirect
from App.models import *
from matplotlib import pyplot as plt

# Create your views here.
def login(r):
    return render(r,"App/calculator.html");
def get_data(r):
    st_objects=Student.objects.all()
    data={'student_data':st_objects}
    return render(r,"App/data.html",context=data);
def outview(r):
    st=Student.objects.all()
    data={'datas':st}
    return render(r,'App/outview.html',context=data);
def info(r,_id):
    st_data=Student.objects.get(id=_id);
    data={'data':st_data}
    return render(r,'App/info.html',context=data);
def outmaster(r):
    st=Student.objects.all()
    data={'datas':st}
    return render(r,'App/outmaster.html',context=data);
def infomaster(r,_id):
    st_data=Student.objects.get(id=_id);
    data={'data':st_data}
    return render(r,'App/infomaster.html',context=data);
def main(r):
    return render(r,"App/main.html");
def practice(r):
    return render(r,"practice.html",context={'fruits':['apple','banana','orange']});
def display_data(r):
    st_data={'data':StudentMark.objects.all()}
    mark_detail=[x[0] for x in list(StudentMark.objects.values_list('mark'))]
    plt.hist(mark_detail)
    plt.title('studentmarkplot');
    plt.savefig('Static/images/studentmarkplot.jpg');
    #fig.savefig('C:\WebDevolopment\DjangoPro\Static\images\',plot.jpg')
    return render(r,'App/stdata.html',context=st_data)
def cookie_session_management(r):
    t_count=int(r.COOKIES.get('count',0));
    s_count=int(r.session.get('count',0));
    r.session['count']=s_count+1;
    response=render(r,"App/main.html",context={'count':t_count,'s_count':s_count});
    response.set_cookie('count',t_count+1);
    return response




def student_panel(r):
    st=StudentMark.objects.all()
    return render(r,'App/studentdata.html',context={'datas':st});
def insert_data(r):
    if r.method=='POST':
        name=r.POST['name']
        mark=r.POST['mark']
        ob=StudentMark(name=name,mark=mark);
        ob.save();
        return redirect('student_panel')
    
    return render(r,'App/insert.html')
def update_data(r,id):
    if r.method=='POST':
        ob=StudentMark.objects.get(id=id)
        ob.name=r.POST["name"]
        ob.mark=r.POST['mark']
        ob.save();
        return redirect('student_panel');
    return render(r,'App/updatedata.html',context={'data':StudentMark.objects.get(id=id)})
def delete_data(r,id):
    StudentMark.objects.get(id=id).delete();
    return redirect('student_panel');
        

    
    

    
     

