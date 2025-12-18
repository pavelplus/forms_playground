from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import TestForm



def index(request):

    data = {
        'username': 'фывпваоапыоал',
        'password': 'qwerty',
        'password2': '',
        'age': 20,
        'sex': None,
        'contact_type': None,
        'about': 'Люблю оливье',
        'autologin': True,
        'token': 'DkjhfHJhlfaAF987afh3hkjhf',
    }

    form = TestForm(data=data)

    form.add_error(None, 'Ошибка формы №1')
    form.add_error(None, 'Ошибка формы №2')

    if form.is_valid():
        if form.cleaned_data['password'] != form.cleaned_data['password2']:
            form.add_error(form.fields['password2'], 'Пароли должны совпадать!')

    # for (prop, val) in form.fields['username'].__dict__.items():
    #     print(f'{prop} = {type(val)} {val}')

    my_form = TestForm(data=data, prefix='mf')
    
    my_form.add_error(None, 'Ошибка формы №1')
    my_form.add_error(None, 'Ошибка формы №2')


    context = {
        'form': form,
        'my_form': my_form,
    }
    return TemplateResponse(request, 'main/index.html', context)