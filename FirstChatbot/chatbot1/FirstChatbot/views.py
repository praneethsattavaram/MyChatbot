from django.shortcuts import render
from django.http import JsonResponse
import openai

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