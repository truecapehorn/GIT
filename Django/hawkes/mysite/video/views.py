from django.shortcuts import render
from django.template.response import TemplateResponse
from video.models import Video
from django.shortcuts import get_object_or_404

 # Create your views here.

#def video(request,video_id):
def video(request):
    data=Video.objects.all()
    #data=get_object_or_404(Video, pk=video_id)
    print(data)
    return render(request,'video/index.html',{'data':data})
