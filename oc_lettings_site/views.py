from django.shortcuts import render

"""
Views for handling requests in the main app project.
"""


def index(request):
    """
    Renders the homepage with 'index.html'.
    """
    return render(request, 'index.html')


def trigger_error(request):
    """
    Triggers a test 500 error for testing purposes.
    """
    raise Exception("This is a test 500 error !")
