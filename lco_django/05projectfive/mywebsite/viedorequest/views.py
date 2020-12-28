from django.shortcuts import render , redirect
from .models import Video
from .forms import VideoFrom


def index(request):
    videos =  Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request,'viedorequest/index.html', context )

def vrform(request):
    if request.method == 'POST':
        form = VideoFrom(request.POST)

        if form.is_vaild():
            new_req = Video(videotitle =request.POST['videoname'],
            videodesc = request.POST['videodesc'])
            new_req.save()
            return redirect('index')
    else:
        form  = VideoFrom()

    # context = {'form'. form}

    return render(request,'viedorequest/vrform.html')
 