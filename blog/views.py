from dataclasses import dataclass

from django.http import HttpResponse
from django.shortcuts import render
import random

@dataclass
class Students:
    first_name: str
    last_name: str
    phone: str
    payed: bool

st1 = Students("ALi", "Aliyev", "+998947892424", True)
st2 = Students("G'ani", "G'aniyev", "+998931234567", False)
st3 = Students("Vali", "Valiyev", "+998904567890", True)
st4 = Students("Eshmat", "Eshmatov", "+998881082121", True)

students = [st1, st2, st3, st4]

def home(request):
    a = random.randint(1, 100)
    b = random.randint(101, 1000)
    c = a + b

    context = {
        'a': a,
        'b': b,
        'c': c,
        'students': students
    }

    return render(request, template_name='blog/base.html', context=context)
