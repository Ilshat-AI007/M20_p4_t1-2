from django.shortcuts import render
from django.http import HttpResponse
def song_view(request, lang='ru'):
    if lang == 'ru':
        return_string = "Пусть бегут неуклюже пешеходы по лужам."
    elif lang == 'fr':
        return_string = "Que les piétons maladroits courent dans les flaques."
    elif lang == 'de':
        return_string = "Mögen die ungeschickten Fußgänger durch Pfützen laufen."
    elif lang == 'es':
        return_string = "Dejen que los peatones torpes corran por los charcos."

    return HttpResponse(return_string)

