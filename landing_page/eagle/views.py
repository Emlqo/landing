from django.shortcuts import render

def index(request):
    #latest_question_list = Message.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'eagle/suri.html')