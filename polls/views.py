# from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

from django.urls import reverse

from django.shortcuts import render, get_object_or_404
# or
from django.template import loader

from django.views import generic

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#     # 1-Pretty dumb output
#     # output = ', '.join(['%i: %s' % (idx, q.question_text) for idx, q in enumerate(latest_question_list)])
#     # output = ', '.join('%i: %s' % (q.id, q.question_text) for q in latest_question_list)
#     # return HttpResponse(output)
#
#     # 2-The traditional way
#     # template = loader.get_template('polls/index.djt')
#     # The context is passed to the template
#     # Dict mapping template var names <-> Python objects
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#
#     # Alternatively, w/out explicitly loading the template:
#     return render(request, 'polls/index.djt', context)

class IndexView(generic.ListView):
    # By default: <app>/<modelName>_list.html
    template_name = 'polls/index.djt'
    # By default: <modelName>_list (question_list)
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 5 puplished questions"""
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     # Dumb way...:
#     # return HttpResponse("You're looking at question %s." % question_id)
#
#     # Alternatively:
#     try:
#         q = Question.objects.get(pk=question_id)
#
#     except Question.DoesNotExist:
#         raise Http404("Hey Dude, question %i does not exist!" % question_id)
#
#     return render(request, 'polls/detail.djt', {'question': q})
#
#     # Quicker way:
#     # question = get_object_or_404(Question, pk=question_id)
#     # return render(request, 'polls/detail.djt', {'question': q})


class DetailView(generic.DetailView):
    model = Question
    # By default: <app>/<modelName>_detail.html
    template_name = 'polls/detail.djt'


# def results(request, question_id):
#     # Dummy implementation...
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.djt', { 'question': q })


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.djt'


def vote(request, question_id):
    # Dumb implementation...
    # return HttpResponse("You're voting on question %s." % question_id)

    q = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        # Display the question voting form ... w/ an err msg!
        return render(request, 'polls/detail.djt', {
            'question': q, 
            'error_msg': "You didn't select a (valid) choice!"
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # /!\ ALWAYS return an HttpResponseRedirect after successfully dealing w/ POST data
        # This prevents data from being posted twice if a user hits the "Back" btn
        return HttpResponseRedirect(reverse('polls:results', args=(q.id, )))





