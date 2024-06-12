from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from chapter.models import Chapter
from sciencechapter.models import ScienceChapter
from mathchapter.models import MathChapter
from login.models import Login
from django.contrib.auth.decorators import login_required
from myapp.models import Todo
import sys, subprocess
from LLAMA_MODEL_FYP.model2 import send_answer 


def login(request):
    data={}
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        data={
            'username': uname,
            'password': pwd
        }
        url = "/?username={}&password={}".format(data['username'],data['password'])
        try:
            info = Login.objects.get(username=uname, password=pwd)
            return redirect(url)
        except Login.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'login.html',data)

def home(request):
    return render(request,'index.html')

@login_required
def profile(request):
    user = get_object_or_404(Login, username='abi')
    context = {
        'user': user,
    }
    return render(request,'profile.html',context)

def games(request):
    return render(request,'games.html')

def geminiai(request):
    return render(request, 'geminiai.html')

def mathlearning(request):
    chaptersData = MathChapter.objects.all()
    data = {
        'chaptersData':chaptersData,
    }
    return render(request,'mathindex.html',data)

def mathchaplearning(request, chapter ):
    template_name = f"math{chapter}.html"
    
    return render(request, template_name)

def sciencechaplearning(request, chapter ):
    template_name = f"science{chapter}.html"
    
    return render(request, template_name)

def tryingaritm(request, chapter):
    return render(request,'adaptivetest.html')

def test(request, chapter):
    if request.method == 'POST':
        todos = Todo.objects.using('other_db').all()
        correct_answers = {}
        user_answers = {}
        topics = {}
        all_topics = []

        for todo in todos:
            correct_answers[todo.id] = todo.c_answer
            user_answers[todo.id] = int(request.POST.get('c_answer_' + str(todo.id)))
            topics[todo.id] = todo.topic

        for question_id, correct_answer in correct_answers.items():
            user_answer = user_answers.get(question_id)
            if user_answer == correct_answer:
                print(f"Question {question_id}: Correct!")
            else:
                print(f"Question {question_id}: Incorrect. Correct answer: {correct_answer}. Your answer: {user_answer}")
                all_topics.append('What is '+topics.get(question_id)+" ?")
        print(all_topics)
        total_questions = len(todos)
        print(total_questions)
        wrong = len(all_topics)
        percentage = (wrong/total_questions) * 100
        score = min(max(round(percentage/20),0),5)
        send_answer(score,all_topics)
        return redirect('home')

    else:
        todos = Todo.objects.using('other_db').all()
        return render(request, 'test2.html', {'todos': todos})

def subtopiclearn(request, chapter):
    return render(request,'subtopiclearn.html')

def sciencelearning(request):
    chaptersData = ScienceChapter.objects.all()
    data = {
        'chaptersData':chaptersData,
    }
    return render(request,'scienceindex.html',data)
