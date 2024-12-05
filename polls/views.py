from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from .models import Question,Choice
from django.template import loader
from django.db.models import F

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html',{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice =  question.choice_set.get(pk = request.POST['choice'])
        print(selected_choice,'ss')
    except(KeyError,Choice.DoesNotExist):
        return render(request, 'polls/details.html',{
            'question':question, 
            'error_message':"No key selected!"
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args =(question_id,)))
    

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html',{'question':question})
    
