import os

from django.shortcuts import render

from django.conf import settings
from .forms import TextForm


from gtts import gTTS


language = 'en'
FILEPATH = f'{settings.MEDIA_ROOT}/speech.mp3'

# Create your views here.

def init_media(): 
    if os.path.exists(FILEPATH):
        os.remove(FILEPATH)

def convert_to_audio(text_to_convert):
    init_media()
    myobj = gTTS(text=text_to_convert, tld='co.in', lang=language, slow=False)
    myobj.save(FILEPATH)
    return True


def home(request):
    success = False
    init_media()
    if request.method == 'POST':
        text_form = TextForm(request.POST)
        text_to_convert = text_form.data.get('comment')

        if text_to_convert:
            success = convert_to_audio(text_to_convert)
            
    else:
        text_form = TextForm()    
    return render(request, 'index.html',{'form':text_form,'success':success}) 