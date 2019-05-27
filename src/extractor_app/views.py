from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.crypto import get_random_string

from .forms import InputForm, FileForm
from .models import Questions, UniqueSession
from session_handler.models import UserAnswer

from extractor_libs import question_extractor as QE


class HomeView(TemplateView):
    template_name = 'extractor/index.html'

    def get(self, request):
        args = {}

        if request.user.is_authenticated:
            postdata = Questions.objects.filter(user=request.user).order_by('-created')
            args['postdata'] = postdata
            sessiondata = UniqueSession.objects.filter(user=request.user).order_by('-created')
            args['sessiondata'] = sessiondata
            usersessiondata = UserAnswer.objects.filter(creationuser=str(request.user)).order_by('averagegrade')
            args['usersessiondata'] = usersessiondata

        args['inputform'] = InputForm()
        return render(request, self.template_name, args)

    def post(self, request):
        args = {}

        if request.user.is_authenticated:
            postdata = Questions.objects.filter(user=request.user).order_by('-created')
            args['postdata'] = postdata
            sessiondata = UniqueSession.objects.filter(user=request.user).order_by('-created')
            args['sessiondata'] = sessiondata
            usersessiondata = UserAnswer.objects.filter(creationuser=str(request.user)).order_by('username')
            args['usersessiondata'] = usersessiondata

        args['inputform'] = InputForm()

        if request.method == 'POST':
            # File Input
            if 'fileinput' in request.POST:
                form = FileForm(request.POST, request.FILES)

                if form.is_valid():
                    input_ = request.FILES['my_uploaded_file'] \
                            .read().decode("utf-8", "strict") \
                            .replace('\n', ' ')
                    input_ = input_.strip()
                    args.update(
                        QE.RequestParser(request).initial_question_request(str(input_))
                    )

                return render(request, self.template_name, args)

            # Text Input
            if 'textinput' in request.POST:
                form = InputForm(request.POST)

                if form.is_valid():
                    input_ = form.cleaned_data['post']
                    args.update(
                        QE.RequestParser(request).initial_question_request(str(input_))
                    )

                return render(request, self.template_name, args)

            # Selected list without download
            if 'selectedchecks' in request.POST:
                self.save_questions(request, args)

                if request.user.is_authenticated:
                    postdata = Questions.objects.filter(user=request.user).order_by('-created')
                    args['postdata'] = postdata
                    sessiondata = UniqueSession.objects.filter(user=request.user).order_by('-created')
                    args['sessiondata'] = sessiondata
                    usersessiondata = UserAnswer.objects.filter(creationuser=str(request.user)).order_by('username')
                    args['usersessiondata'] = usersessiondata

                args['inputform'] = InputForm()

                messages.success(
                    request, (f'Selected questions saved successfully!')
                )
                return render(request, self.template_name, args)

            # Selected save with download
            if 'toDownload' in request.POST or 'downloadSession' in request.POST:
                self.save_questions(request, args)

                postdata = Questions.objects.filter(user=request.user).order_by('-created')
                args['postdata'] = postdata
                sessiondata = UniqueSession.objects.filter(user=request.user).order_by('-created')
                args['sessiondata'] = sessiondata
                usersessiondata = UserAnswer.objects.filter(creationuser=str(request.user)).order_by('username')
                args['usersessiondata'] = usersessiondata

                args['toDownload'] = 'downloadfile'
                args['inputform'] = InputForm()

                if 'toDownload' in request.POST:
                    messages.success(
                        request, (f'Selected questions downloaded and saved successfully!')
                    )
                else:
                    messages.success(
                        request, (f'Selected questions downloaded successfully!')
                    )

                return render(request, self.template_name, args)

            if 'createsession' in request.POST:
                qa_list_name, final_list, input_ = QE.RequestParser(request).selection_parsing()
                sessionid = str(get_random_string(length=20))

                try:
                    instance = UniqueSession()
                    instance.list_title = qa_list_name
                    instance.inputted_text = input_
                    instance.qa_list = str(final_list)
                    instance.sessionid = sessionid
                    instance.user = request.user
                    instance.save()

                    return redirect('/session/' + sessionid)
                except IntegrityError:
                    postdata = Questions.objects.filter(user=request.user).order_by('-created')
                    args['postdata'] = postdata
                    sessiondata = UniqueSession.objects.filter(user=request.user).order_by('-created')
                    args['sessiondata'] = sessiondata
                    usersessiondata = UserAnswer.objects.filter(creationuser=str(request.user)).order_by('username')
                    args['usersessiondata'] = usersessiondata
                    return render(request, self.template_name, args)

        messages.error(
            request, (f'Something bad happened, oops.')
        )
        return redirect('/')

    def save_questions(self, request, args):
        qa_list_name, final_list, input_ = QE.RequestParser(request).selection_parsing()

        try:
            instance = Questions()
            instance.list_title = qa_list_name
            instance.inputted_text = input_
            instance.qa_list = str(final_list)
            instance.user = request.user
            instance.save()
        except IntegrityError:
            return render(request, self.template_name, args)


def handler404(request):
    return render(request, 'extractor/404.html', status=404)


def handler500(request):
    return render(request, 'extractor/404.html', status=500)
