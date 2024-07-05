#created by me- sadashiv

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from .my_func import get_minecode_result
# from myproject.my_func import get_minecode_result


# Create your views here.
def index(request) :
    return render(request, 'index.html')

def analyze(request) :
    # get the text from html file
    text1 = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    params = ""
    purpose = ""
    
    if removepunc == "on" :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        
        purpose = purpose + ' Remove punctutation'
        for char in text1 :
            if char not in punctuations :
                analyzed = analyzed + char
        text1 = analyzed
        params = { 'purpose' : purpose, 'analyzed_text' : analyzed}

    
    if (fullcaps == "on") :
        analyzed = ""
        purpose = purpose + ' UPPER CASE'
        for char in text1 :
            analyzed = analyzed + char.upper()
        text1 = analyzed
        params = { 'purpose' : purpose, 'analyzed_text' : analyzed}

    if (newlineremove == "on") :
        analyzed = ""
        purpose = purpose + " Remove new line"
        for char in text1 :
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        text1 = analyzed
        params = { 'purpose' : purpose, 'analyzed_text' : analyzed}
    
    if (extraspaceremove == "on") :
        analyzed = ""
        purpose = purpose + " Remove extra space"
        for index, char in enumerate(text1) :
            if (text1[index] == ' ') and (text1[index + 1] == ' ') :
                pass
            else :
                analyzed = analyzed + char
        text1 = analyzed
        params = { 'purpose' : purpose, 'analyzed_text' : analyzed}


    return render(request, 'analyze.html' , params)

def temp1(request) :
    return HttpResponse('template1.html')


def contact_us(request) :
    return render(request, 'contact_us.html')


def search_minecode_view(request):
    return redirect('search_view_minecode') 

# def search_minecode(request):
#     minecode = request.GET.get('minecode')
#     print(minecode)
#     if minecode:
#         minecode_result = get_minecode_result(minecode)  # Get the result from the search function
#         print(minecode_result)
#     else:
#         minecode_result = "No minecode provided"
        
#     return JsonResponse({'result': minecode_result})


