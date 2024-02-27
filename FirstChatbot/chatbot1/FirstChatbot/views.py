from django.shortcuts import render

# Create your views here.
def FirstChatbot(request):
    return render(request, 'chatbot.html')