from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'wall_app/index.html')



def show(self, post_data):
    if 'id' in request.session:
        messages = Message.objects.all().order_by('-id')
        comments = Comment.objects.all()
        this_user = User.objects.get(id = request.session['id'])
        context={
            'messages': messages,
            'comments': comments,
            'user': this_user
        }
        return render(request, 'wall_app/index.html', context)
    else:
        return redirect('/')

# we finished the show root continue the video at 01:03:33