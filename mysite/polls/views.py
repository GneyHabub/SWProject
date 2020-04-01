from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import CustomUserCreationForm
from .models import Choice, Question, Poll, CustomUser

from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import StaffLoginForm, StudentLoginForm


def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_student:
                    return HttpResponse('Unavailable for students ')
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('polls:personal_page', args=(user.id,)))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = StaffLoginForm()
    return render(request, 'Login/staff_form_login.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if not user.is_student:
                    return HttpResponse('This is only for students')
                if user.is_active:
                    login(request, user)
                    # todo handle if no such poll exists
                    return HttpResponseRedirect(reverse('polls:detail', args=(cd['poll_id'],)))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = StudentLoginForm()
    return render(request, 'Login/student_form_login.html', {'form': form})


class PersonalPage(generic.DeleteView):
    model = CustomUser
    template_name = 'home_page/home_page.html'


# for staff self-creation of accounts
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Login/staff_form_login.html'


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published polls."""

        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/default_poll.html'
    # template_name = 'polls/def_poll_tr.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


def thank_you(request):
    # model = Poll
    template = 'polls/thank_you_page.html'
    context = {}
    return render(request, template, context)


# todo -throw errors is some questions are not answered
def vote_poll(request, poll_id):
   try:
       post_data = dict(request.POST.lists())
       post_data.pop('csrfmiddlewaretoken')
       questions = list(post_data.keys())

       for q in questions:
           quest = get_object_or_404(Question, id=q)
           if quest.type == 2:
               if post_data.get(q)[0] != "":
                    c = Choice(question=quest, choice_text=post_data.get(q)[0], votes=1)
                    c.save()
               post_data.pop(q)

       interested = list(post_data.values())
       print(f"Selected choice   {interested}")
   except (KeyError, Choice.DoesNotExist):
       # Redisplay the question voting form.
       return render(request, 'polls/detail.html', {
           # 'question': poll.poll_name,
           'error_message': "You didn't select a choice.",
       })
   else:
       inter = []
       for sublist in interested:
           sublist = [int(item) for item in sublist]
           inter += sublist

       for ch in inter:
           choice = get_object_or_404(Choice, id=ch)
           print(choice.id, "  ", choice.question, "  ", choice.choice_text)
           choice.votes += 1
           choice.save()
       # Always return an HttpResponseRedirect after successfully dealing
       # with POST data. This prevents data from being posted twice if a
       # user hits the Back button.
       return HttpResponseRedirect(reverse('polls:thank_you_page'))
