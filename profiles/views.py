from django.shortcuts import render

from profiles.models import Profile


def profiles_index(request):
    """
    Displays a list of all user profiles.

    Retrieves all Profile instances and renders them in the
    'profiles/profile_list.html' template.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    print(profiles_list.query)
    return render(request, 'profiles/profile_list.html', context)


def profile(request, username):
    """
    Displays a specific user profile based on the provided username.

    Retrieves the Profile instance for the given username and renders it
    in the 'profiles/profile_details.html' template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile_details.html', context)
