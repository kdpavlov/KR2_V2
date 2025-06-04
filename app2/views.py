from django.shortcuts import render, get_object_or_404
from .models import Page, Student, Management, Program, Person
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
def my_page(request):
    person = Person.objects.first()
    return render(request, 'app2/mypage.html', {'person': person})

def program_page(request):
    program = Program.objects.first()
    return render(request, 'app2/program.html', {'program': program})

def management_view(request):
    management = Management.objects.first()
    context = {'management': management,}
    return render(request, 'app2/management_page.html', context)