from django.contrib import messages
from re import template
from django.shortcuts import render, redirect
from .forms import NewUserForm, NewHobbyForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

from .models import Hobby, Likes


@login_required(login_url='/accounts/login/')
def index(request):
    user_hobbies = set(map(lambda x: x[1], Hobby.objects.filter(
        user=request.user).values_list()))
    match_ids = set(map(lambda x: x[3], Hobby.objects.filter(
        hobby_name__in=user_hobbies).exclude(user=request.user).values_list()))
    match_users = User.objects.filter(id__in=match_ids)
    context = {
        'match_users': match_users,
    }
    return render(request, 'hobbifyapp/index.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    hobbies = Hobby.objects.filter(user=user_id)[::1]
    context = {
        "match_user": User.objects.get(id=user_id),
        "hobbies": hobbies,
        "liked": Likes.objects.filter(liker=request.user, likee=User.objects.get(id=user_id)).exists()
    }
    return render(request, 'hobbifyapp/profile.html', context=context)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/profile/{}".format(user.id))
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def add_hobby(request):
    if request.method == "POST":
        form = NewHobbyForm(request.POST)
        if form.is_valid():
            hobby = form.save(commit=False)
            hobby.user = request.user
            hobby.save()
            messages.success(request, "Hobby added.")
            return redirect("/profile/{}".format(request.user.id))
    form = NewHobbyForm()
    return render(request=request, template_name="hobbifyapp/add_hobby.html", context={"add_hobby_form": form})


@login_required(login_url='/accounts/login/')
def likes(request):
    match_ids = Likes.objects.filter(
        likee=request.user.id).values_list('liker')
    liked_by = User.objects.filter(id__in=match_ids)

    if not liked_by:
        return HttpResponse('Sorry No one likes you.')
    context = {
        'match_users': liked_by,
        'likepage': True
    }
    return render(request, 'hobbifyapp/index.html', context)


@login_required(login_url='/accounts/login/')
def like(request, user_id):
    try:
        Likes.objects.get(liker=User.objects.get(
            id=request.user.id), likee=User.objects.get(id=user_id)).delete()
    except:
        l = Likes(liker=User.objects.get(id=request.user.id),
                  likee=User.objects.get(id=user_id))
        l.save()
    response = redirect(index)
    return response
