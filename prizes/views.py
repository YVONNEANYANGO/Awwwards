from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import  Http404,HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.
def welcome(request):
    return render(request, 'project.html')
    
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
            
        return render(request, 'project.html', {"prizes":prizes,"letterForm":form})
    

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project":project})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'profile_user': username})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})