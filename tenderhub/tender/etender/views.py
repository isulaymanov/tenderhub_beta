from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from etender.models import *


# Create your views here.
navigation_links = [
    {'url': 'ads', 'title': 'Объявления'},
    {'url': 'registration', 'title': 'Планы'},
    {'url': 'registration', 'title': 'Аукционы'},
    {'url': 'registration', 'title': 'Контракты'},
]
registration_links = [
        {'url': '#', 'title': 'Вход'},
        {'url': '#', 'title': 'Зарегистрироваться'},
    ]
def index(request):

    clients1 = [
        {'image': 'etender/img/skyline.png', 'alt': 'Client 1', 'title': 'Коммерческие закупки', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
        {'image': 'etender/img/skyline.png', 'alt': 'Client 2', 'title': 'Коммерческие закупки', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
        {'image': 'etender/img/skyline.png', 'alt': 'Client 3', 'title': 'Коммерческие закупки', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
        {'image': 'etender/img/skyline.png', 'alt': 'Client 4', 'title': 'Коммерческие закупки', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
    ]
    auction_images = [
        {'url': 'etender/img/auc-icon.png', 'alt': 'Image 1', 'text': 'Регистрация на E-Tender'},
        {'url': 'etender/img/auc-icon.png', 'alt': 'Image 1', 'text': 'Регистрация на E-Tender'},
        {'url': 'etender/img/auc-icon.png', 'alt': 'Image 1', 'text': 'Регистрация на E-Tender'},
        {'url': 'etender/img/auc-icon2.png', 'alt': 'Image 2', 'text': 'Регистрация на E-Tender'},
        {'url': 'etender/img/auc-icon2.png', 'alt': 'Image 2', 'text': 'Регистрация на E-Tender'},
        {'url': 'etender/img/auc-icon2.png', 'alt': 'Image 2', 'text': 'Регистрация на E-Tender'},
    ]

    tender_services = [
        {'background_image': 'etender/img/1.jpg', 'title': 'КАК РАБОТАТЬ С БАЗОЙ ГОСУДАРСТВЕННЫХ ТЕНДЕРОВ'},
        {'background_image': 'etender/img/2.jpg', 'title': 'КАК РАБОТАТЬ С БАЗОЙ ГОСУДАРСТВЕННЫХ ТЕНДЕРОВ'},
        {'background_image': 'etender/img/3.jpg', 'title': 'КАК РАБОТАТЬ С БАЗОЙ ГОСУДАРСТВЕННЫХ ТЕНДЕРОВ'},
        {'background_image': 'etender/img/4.jpg', 'title': 'КАК РАБОТАТЬ С БАЗОЙ ГОСУДАРСТВЕННЫХ ТЕНДЕРОВ'},
    ]
    useful_links = [
        {'url': '#', 'title': 'Министерство финансов Кыргызской Республики'},
        {'url': '#', 'title': 'Центральное казначейство МФ КР'},
        {'url': '#', 'title': 'Государственное агентство антимонопольного регулирования при ПКР'},
        {'url': '#', 'title': 'Министерство финансов Кыргызской Республики'},
        {'url': '#', 'title': 'Министерство финансов Кыргызской Республики'},
    ]

    links_buttons = [
        {'url': '#', 'title': 'Реестр'},
        {'url': '#', 'title': 'Документы'},
        {'url': '#', 'title': 'Справочники'},
        {'url': '#', 'title': 'Помощь'},
        {'url': '#', 'title': 'Жалобы'},
    ]

    clients = [
        {'image': 'etender/img/alfa.png', 'alt': 'Client 1'},
        {'image': 'etender/img/alfa.png', 'alt': 'Client 2'},
        {'image': 'etender/img/alfa.png', 'alt': 'Client 3'},
        {'image': 'etender/img/alfa.png', 'alt': 'Client 4'},
        {'image': 'etender/img/IUK.png', 'alt': 'Client 5'},
        {'image': 'etender/img/IUK.png', 'alt': 'Client 6'},
        {'image': 'etender/img/IUK.png', 'alt': 'Client 7'},
        {'image': 'etender/img/IUK.png', 'alt': 'Client 8'},
    ]

    context = {
        'navigation_links': navigation_links,
        'registration_links': registration_links,
        'clients1': clients1,
        'auction_images': auction_images,
        'tender_services': tender_services,
        'useful_links': useful_links,
        'links_buttons': links_buttons,
        'clients': clients,
        'user': request.user,
    }

    return render(request, 'etender/html/index.html', context)


