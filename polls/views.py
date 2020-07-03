# from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render, get_object_or_404
# or
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join(['%i: %s' % (idx, q.question_text) for idx, q in enumerate(latest_question_list)])
    # output = ', '.join('%i: %s' % (q.id, q.question_text) for q in latest_question_list)
    # return HttpResponse(output)

    template = loader.get_template('polls/index.djt')
    # The context is passed to the template
    # Dict mapping template var names <-> Python objects
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))
    # Alternatively, w/out explicitly loading the template:
    # return render(request, 'polls/index.djt', context)


def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Hey Dude, question %i does not exist!" % question_id)

    return render(request, 'polls/detail.djt', {'question': q})

    # Quicker way:
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.djt', {'question': q})

    # Alternatively:
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)





