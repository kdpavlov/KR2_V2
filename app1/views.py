from django.shortcuts import render, redirect
from .models import StudyRecord
from .forms import StudyRecordForm
from django.db.models import Avg,Max,Min,Sum
from app2.models import Page
# Create your views here.

def study_records(request):
    if request.method == 'POST':
        form = StudyRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_records')
    else:
        form = StudyRecordForm()

    min_score = request.GET.get('min_score')
    sort_by = request.GET.get('sort_by', 'date')
    records = StudyRecord.objects.all()
    if min_score:
        try:
            min_score_int = int(min_score)
            records = records.filter(score__gte=min_score_int)
        except ValueError:
            min_score_int = None
    if sort_by in ['name', 'course', 'score', 'date']:
        if sort_by == 'score':
            records = records.order_by(f'-{sort_by}')
        else:
            records = records.order_by(sort_by)

    avg_score = records.aggregate(Avg('score'))['score__avg']

    pages = Page.objects.all()

    stats = records.aggregate(
        avg_score=Avg('score'),
        max_score=Max('score'),
        min_score=Min('score'),
        sum_score=Sum('score')
    )
    context = {
        'form': form,
        'records': records,
        'avg_score': avg_score,
        'min_score': min_score,
        'sort_by': sort_by,
        'pages': pages,
        'stats': stats
    }
    return render(request, 'app1/study_records.html', context)

