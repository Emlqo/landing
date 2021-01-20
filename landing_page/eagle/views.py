import sqlite3

from django.shortcuts import render

def index(request):
    #latest_question_list = Message.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'eagle/index.html')

def email(request,Email):
    print(Email)

    if request.method =='POST':

        email = request.POST.str('Email')

        print(Email,email)
        conn = sqlite3.connect('./db.sqlite3')
        cur = conn.cursor()

        sql = "insert into test (Email) values (?)"

        cur.execute(sql, [Email])
        conn.commit()
        cur.close()
        conn.close()
    return render(request, 'eagle/index.html')
