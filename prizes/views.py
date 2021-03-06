from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import  Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Project


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    print (projects)

    return render(request, 'project.html', {"projects":projects})
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()

            send_welcome_email(name,email)
            
            HttpResponseRedirect('')
        else:
            form = NewsLetterForm()
            
        return render(request, 'project.html', {"projects":projects, "letterForm":form})
    

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project":project})

def profile(request,profile_id):
    
    profile= Profile.get_profile(profile_id)

    return render(request, 'profile.html' , {"profile":profile })



def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})