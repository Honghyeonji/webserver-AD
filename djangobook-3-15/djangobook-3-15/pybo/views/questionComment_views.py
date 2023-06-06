from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question, Answer, Comment

def index(request):
    page=request.GET.get('page', '1')
    so = request.GET.get('so', 'recent')
    qs = request.GET.get('qs', '')

    if qs != '':
        if so == 'recommend':
            questionComment_list = Comment.objects.filter(Q(question = qs)).annotate(num_voter = Count('voter')).order_by('-num_voter', '-create_date')
        else:
            questionComment_list = Comment.objects.filter(Q(question = qs)).order_by('-create_date')

    paginator = Paginator(questionComment_list, 10)
    page_obj = paginator.get_page(page)

    context = {'': page_obj, 'page': page, 'so':so, 'qs': qs}
    return render(request, 'pybo/question_detail.html', context) 