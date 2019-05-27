import ast
from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError

from extractor_app.models import UniqueSession
from .models import UserAnswer

from extractor_libs import question_extractor as QE


def user_session(request, sessionid):

    template_name = 'session_handler/session.html'
    time_threshold = datetime.now() - timedelta(hours=2)

    if request.method == 'GET':
        args = {}
        session_vals = UniqueSession.objects.filter(sessionid=sessionid).filter(created__gt=time_threshold)
        args['session_vals'] = session_vals

        return render(request, template_name, args)

    if request.method == 'POST':
        args = {}
        session_vals = UniqueSession.objects.filter(sessionid=sessionid).filter(created__gt=time_threshold)
        args['session_vals'] = session_vals

        if 'usersubmit' in request.POST:
            username = request.POST.get('username')
            inputted_text = request.POST.get('og_input')
            qlist = request.POST.getlist('questionforanswer')
            alist = request.POST.getlist('answerforquestion')
            sessionid = request.POST.get('sessionid')
            creationuser = request.POST.get('creationuser')
            og_list = request.POST.get('qa_list')

            actualanswerlist = []
            for list_ in ast.literal_eval(og_list):
                for q in list_[:-1]:
                    actualanswerlist.append(list_[-1])

            savelist = []
            for q, a in zip(qlist, alist):
                savelist.append([q, a])

            averagegrade = QE.AnswerEvaluation(alist, actualanswerlist).evaluate_similarity()

            try:
                instance = UserAnswer()
                instance.username = username
                instance.inputted_text = inputted_text
                instance.qalist = str(savelist)
                instance.sessionid = sessionid
                instance.creationuser = str(creationuser)
                instance.averagegrade = averagegrade
                instance.save()
            except IntegrityError:
                args['completed'] = "completed"
                return render(request, template_name, args)

            messages.success(
                request, (f'Answers submitted successfully!')
            )
            session_vals = UniqueSession.objects.filter(sessionid=sessionid).filter(created__gt=time_threshold)
            args['session_vals'] = session_vals
            args['completed'] = "completed"

            return render(request, template_name, args)

    else:
        return render(request, template_name)
