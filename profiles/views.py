from django.shortcuts import render

from profiles.models import Profile


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    print(profiles_list.query)
    return render(request, 'profiles/profile_list.html', context)


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile_details.html', context)
