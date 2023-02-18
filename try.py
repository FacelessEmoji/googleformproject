import requests
import random

GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLScayD17B-_stBh2w6YxG1_I7BVrsg9BCt0IH0SN9RWDou1K_g'

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform'

gender = ['Мужской', 'Женский']
yon = ['Да', 'Нет']
age = ['18-25', '26-35']
occupation = ['Работающий', 'Безработный']
family_status = ['Свободен/свободна', 'В отношениях']
children = ['Нет', '1 ребёнок']
inheritance = ['Да, знаю', 'Слышал(а), но не знаю', 'Нет, не знаю']
diseases = ['Синдром Дауна', 'Фенилкетонурия', 'Спинально-мышечная атрофия', 'Заячья губа/волчья пасть', 'Другие']
#mof = ['От матери', 'От обоих родителей']
mof = ['От отца', 'От матери', 'От обоих родителей', 'Не зависит от родителей']
momn = ['Можно', 'Нельзя']
for i in range(7):
    form_data = {'entry.1047661290': gender[1],
                  # 'entry.708070029': random.choice(age),
                  'entry.708070029': age[0],
                  # 'entry.869473543': {'Студент', random.choice(occupation)},
                  'entry.869473543': {'Студент', random.choice(occupation)},
                  'entry.2104404530': random.choice(family_status),
                  # 'entry.1068334741': random.choice(children),
                  'entry.1068334741': children[0],
                  # 'entry.812524607': random.choice(inheritance),
                  'entry.812524607': random.choice(inheritance),
                  'entry.1965140426': yon[1],
                  'entry.1379215305': {random.choice(diseases), random.choice(diseases), random.choice(diseases)},
                  'entry.352115378': yon[1],
                  'entry.1438848940': yon[1],
                  'entry.747856010': random.choice(yon),
                  'entry.515397275': yon[1],
                  'entry.749830451': random.choice(mof),
                  'entry.1264077439': momn[1],
                  'entry.1074013426': random.choice(momn)
                  }
    # form_data2 = {'entry.1047661290': random.choice(gender),
    #               # 'entry.708070029': random.choice(age),
    #               'entry.708070029': age[0],
    #               # 'entry.869473543': {'Студент', random.choice(occupation)},
    #               'entry.869473543': {'Студент', occupation[1]},
    #               'entry.2104404530': random.choice(family_status),
    #               # 'entry.1068334741': random.choice(children),
    #               'entry.1068334741': children[0],
    #               # 'entry.812524607': random.choice(inheritance),
    #               'entry.812524607': inheritance[0],
    #               'entry.1965140426': random.choice(yon),
    #               'entry.352115378': random.choice(yon),
    #               'entry.1438848940': random.choice(yon),
    #               'entry.747856010': random.choice(yon),
    #               'entry.515397275': random.choice(yon),
    #               'entry.749830451': random.choice(mof),
    #               'entry.1264077439': random.choice(momn),
    #               'entry.1074013426': random.choice(momn)
    #               }
    # mas = [form_data1, form_data2]
    # form_data = random.choice(mas)
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(urlResponse, data=form_data, headers=user_agent)
