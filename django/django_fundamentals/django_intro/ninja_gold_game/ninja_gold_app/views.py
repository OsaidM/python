from django.shortcuts import render,redirect
import random
# Create your views here.
def root(request):
    
    return render(request,'index.html')

def process_money(request):
    farm = request.POST.get('farm')
    cave = request.POST.get('cave')
    house = request.POST.get('house')
    casino = request.POST.get('casino')
    request.session['fgold'] += request.session['frmedgold'] 
    
    request.session['frmedgold'] = 0
    if farm == 'farm':
        cRndm = random.randint(10, 20)
        request.session['frmedgold'] += cRndm
        return redirect('/') 
    elif cave == 'cave':
        cRndm = random.randint(5, 10)
        request.session['frmedgold'] += cRndm
        return redirect('/') 
    elif house == 'house':
        cRndm = random.randint(2, 5)
        request.session['frmedgold'] += cRndm
        return redirect('/') 
    elif casino == 'casino':
        cRndm = random.randint(-50, 50)
        request.session['frmedgold'] += cRndm
        return redirect('/') 
    return redirect('/')