from django.shortcuts import render

from lettings.models import Letting


def lettings_index(request):
    """
    Renders a list of all lettings.

    Retrieves all Letting instances and renders them in the
    'lettings/letting_list.html' template.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/letting_list.html', context)


def letting(request, letting_id):
    """
    Renders details of a specific letting.
    Retrieves the Letting instance identified by the letting_id and renders
    it in the 'lettings/letting_details.html' template.
    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to display.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting_details.html', context)
