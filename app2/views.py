from django.shortcuts import render, get_object_or_404
from .models import Page, Student
# Create your views here.
def page_detail(request, id):
    page = get_object_or_404(Page, pk=id)
    pages = Page.objects.all()
    return render(request, 'app2/page_detail.html', {'page': page,
                                                     'pages': pages})
def students_list(request):
    students = Student.objects.all()

    search = request.GET.get('search')
    if search:
        students = students.filter(full_name__icontains=search)
    pages = Page.objects.all()
    students = students.order_by('-score')

    return render(request, 'app2/students_list.html', {'students': students, 'search': search, 'pages': pages,})

