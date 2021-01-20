import sqlite3

from django.shortcuts import render

def index(request):

# ?이메일_주소=cs00327%40naver.com&평균_공지_전송_횟수=%20월%201~2회&어디에_사용하고_싶나요=%5B모임%5D%20친구모임
    if request.method =='GET':
        print("???????")
        email = request.GET.get('이메일_주소')
        avg_notice = request.GET.get('평균_공지_전송_횟수')
        where_use = request.GET.get('어디에_사용하고_싶나요')
        print(email,avg_notice,where_use)
        conn = sqlite3.connect('./db.sqlite3')
        cur = conn.cursor()

        sql = "insert into eagle_test (email,avg_notice,where_use) values (?,?,?)"

        cur.execute(sql, [email,avg_notice,where_use])
        conn.commit()
        cur.close()
        conn.close()
    return render(request, 'eagle/index.html')

