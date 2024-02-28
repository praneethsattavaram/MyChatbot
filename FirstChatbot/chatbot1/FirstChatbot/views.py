from django.shortcuts import render
from django.http import JsonResponse
import openai

from django.contrib import auth

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = message,
        max_tokens = 150,
        n=1,
        stop = None,
        temperature = 0.7,
    )
    answer = response.choice[0].text.strip()
    return answer

# Create your views here.
def FirstChatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            pass
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html',{'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)

