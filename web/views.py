from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime
# csrf_exempt is small code and it say this function dos'nt need csrf
# and it dosn't need a proper standrad form and anyone can call it
# crf dr vaqe ye code ke hr formi ke submit mishe oon khodo dre khbr mide code in bood oonm mige are in code bood
#  va in baes mishe ke kasi ntone bedone rftn be form codi ro sumbit kone
@csrf_exempt
def submit_expense(request):
    """ user submit expense """
    print('we are here')
    print('******************************')
    print(request.POST)
    print('******************************')
    # TODO: validate date user might be fake, token might be fake , amount might be fake
    this_token = request.POST['token']
    # yani useri ke tokenesh(object tokenesh) data i az jense token dre
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(
        user = this_user,
        amount=request.POST['amount'],
        text = request.POST['text'],
        date = date
    )

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """ user submit income """
    print('we are in income')
    print('******************************')
    print(request.POST)
    print('******************************')
    # TODO: validate date user might be fake, token might be fake , amount might be fake
    this_token = request.POST['token']
    # yani useri ke tokenesh(object tokenesh) data i az jense token dre
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(
        user = this_user,
        amount=request.POST['amount'],
        text = request.POST['text'],
        date = date
    )

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
