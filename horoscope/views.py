from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.template.loader import render_to_string


zodiac_dict = {
    'aries': { 'description':'Feel like you`re tripping over your own tongue? That`s not surprising, considering the constant flow of verbosity that`s spilling forth from you right now. Go ahead and enjoy your extreme eloquence -- everyone else is.',
                'type': 'fire',
                'day_start': 80,
                'day_finish': 111,},
    'taurus': { 'description':'Stay in the now rather than trying to jump forward into the future. You`ll do best when you focus your attention on all the immediate details that require your assistance. Remember that, no matter how tempting it is to start booking yourself weeks in advance.',
                'type': 'earth',
                'types': 'earth',
                'day_start': 112,
                'day_finish': 142,},
    'gemini': {'description':'From you, a wink and a smile go beyond a thousand words -- they`re practically an entire romantic saga. Your flirty energy livens things up wherever you go right now, so make sure that as many people as possible can appreciate your fabulous self.',
                'type': 'air',
                'day_start': 143,
                'day_finish': 173,},
    'cancer': {'description':'For the first time in a very long time, you`re listening only to one authority -- yourself. This is especially true regarding a social matter. You`ve been worried far too long about doing the right thing. Now it`s time to do right by you.',
                'type': 'water',
                'day_start': 174,
                'day_finish': 204,},
    'leo':{'description':'You may feel ready to move into a decisive new leadership role, but the stars say to let things gestate for a little while longer before you make your big move. Try talking things over with your boon companions and hear what they have to say.',
                'type': 'fire',
                'day_start': 205,
                'day_finish': 234,},

    'virgo':{'description':'Don`t try to do more than you can comfortably handle -- and make sure you`re very clear about your limits if others try to ask you to take more on. When possible, lighten your load rather than add more to it.',
                'type': 'earth',
                'day_start': 235,
                'day_finish': 267,},
    'libra':{'description':'You love watching this new scenario unfold in your life, but suddenly watching it isn`t enough. You want -- no, you need -- to take action, but you`re not sure which way to turn. Take a moment and look before you leap.',
                'type': 'air',
                'day_start': 268,
                'day_finish':  297,},
    'scorpio':{'description':'Minor details could become major mistakes if they`re left unchecked, but fortunately, there`s plenty of time to check everything. Not only will this ensure your enterprise will go swimmingly, but it`ll give you some much-needed peace of mind.',
                'type': 'water',
                'day_start': 298,
                'day_finish': 327,},
    'sagittarius':{'description':'Having this much activity going on around you can be somewhat unsettling, but don`t sulk. Just because something seems out of sync doesn`t mean it`ll be that way permanently. Wait it out and you`ll feel things start to jell.',
                'type': 'fire',
                'day_start': 328,
                'day_finish': 357,},
    'capricorn':{'description':'Put the kibosh on anyone who`s absolutely determined to make sure even the smallest things go haywire. With a little extra care, you can defuse this live wire before they make life any more difficult than it is.',
                'type': 'earth',
                'day_start': 358,   
                'day_finish': 365+20,},
    'aquarius':{'description':'Taking other people`s opinions into consideration is usually the last item on your list of priorities, and that goes double when it comes to a very new and very exciting person in your life.',
                'type': 'air',
                'day_start': 21,
                'day_finish': 50,},
    'pisces':{'description':'Learn to deal with ambiguity by letting it exist, rather than trying to make it go away. If you act too rapidly, you might just find that the solution becomes a much larger problem than the original situation.',
                'type': 'water',
                'day_start': 51,
                'day_finish': 80,},
}


def info_about_horoscope(request, sign_zodiac):
    if sign_zodiac in zodiac_dict :
        return render(request, "horoscope/info_zodiac.html", context={"sign":sign_zodiac, "zodiac":zodiac_dict[sign_zodiac]['description']})
    elif sign_zodiac=='type':
        inf=''
        for sign_zodiac in zodiac_dict:
            if zodiac_dict[sign_zodiac]['type'] in inf:
                continue
            else:
                redirect_path=reverse("type_horoscope", args=[zodiac_dict[sign_zodiac]['type']])
                inf += f"<li><a href='{redirect_path}'>{zodiac_dict[sign_zodiac]['type'].capitalize()}</a></li>"
        return HttpResponse(f"<h2>{inf}</h2>")
    else:
        return HttpResponse("No such sign")
    
def info_about_horoscope_number(request, sign:int):
    if sign > len(list(zodiac_dict)) or sign < 0:
        return HttpResponse("No such sign number ")
    else:
        redirect_url =reverse("horoscope_name", args=(list(zodiac_dict)[sign-1],))
        return HttpResponseRedirect(redirect_url)

def index(request):
    zodiacs = list(zodiac_dict)
    

    return render(request, "horoscope/index.html", context={"zodiacs":zodiacs})




def type_of_horoscope(request, type):
    zodiacs=''
    for sign in zodiac_dict:
        if zodiac_dict[sign]['type'] == type:
            redirect_path =reverse("horoscope_name", args=[sign])   
            zodiacs += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    return HttpResponse(f"<h2>{zodiacs}</h2>")

def month_day_horoscope(request, month, day):
    date = int(datetime(2022, month, day).strftime('%j')) 
    for sign in zodiac_dict:
        if date<= zodiac_dict[sign]['day_finish'] and date>= zodiac_dict[sign]['day_start']:
            redirect_path =reverse("horoscope_name", args=[sign])
            return HttpResponse(f"<h2><a href='{redirect_path}'>{sign.title()}</a></h2>")





