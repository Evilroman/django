from django.db import connection
from django.http import HttpResponse

def index(self):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM auth_user")
    row = cursor.fetchall()
    return HttpResponse(row)
