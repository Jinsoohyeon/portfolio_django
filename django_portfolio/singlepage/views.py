from msilib.schema import ListView
from select import select
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Memo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import Mailform, MemoForm
from django.views.generic import UpdateView, DetailView, ListView

# Create your views here.

def landing(request):
    mail_form = Mailform
    if request.method == 'POST':
        message_form = Mailform(request.POST)
        if message_form.is_valid():
            message_form.save()
    return render(request, 'singlepage/landing.html', {'mail_form' : mail_form})



def aboutMe(request):
    return render(request, 'singlepage/aboutme.html')

def memo(request):
    memo_form = MemoForm
    memos = Memo.objects.all()
    return render(request, 'singlepage/memo_form.html', {'memo_form' : memo_form, 'memos' : memos})


def new_memo(request):
    if request.user.is_authenticated:
        # form = Memo.objects.get
        # print("프린트: ",form)

        if request.method == 'POST':
            memo_form = MemoForm(request.POST)
            if memo_form.is_valid():
                memo = memo_form.save(commit=False)
                memo.author = request.user
                memo.save()
                return redirect('/memo_form/')                
        else:
            return redirect('/memo_form/')
    else:
        raise PermissionDenied

class MemoUpdate(LoginRequiredMixin, UpdateView):
    model = Memo
    form_class = MemoForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(MemoUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def delete_memo(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    print("프린트 :", memo)
    if request.user.is_authenticated and request.user == memo.author:
        memo.delete()
        return redirect('/memo_form/')
    else:
        raise PermissionDenied

# def update_memo(request, pk):
#     if request.method == 'POST':
#         memo = Memo.objects.filter(pk=pk)
#         memo.update('content')
#         return redirect('/memo_/')
#     else:
#         return redirect('/memo/')

# class MemoDetail(DetailView):
#     model = Memo
#     def get_context_data(self, **kwargs):
#         context = super(MemoDetail, self).get_context_data()
#         context['memo_form'] = MemoForm
#         return context
