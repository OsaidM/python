from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def root(request):
    cRndm = random.randint(1, 100)
    request.session['cRnd'] = cRndm
    print(cRndm)
    
    return render(request,'index.html')

def check(request):
    request.session['result'] = "<h2 style='background-color:grey'>Please Enter A Value</h2>"
    cRndm = request.session['cRnd']
    if request.POST['guess'] == '':
        request.session['result'] = '<h2 style="background-color:#cf2a27">Please Enter A Value</h2>'
        return redirect('/')
    request.session['pRnd'] = request.POST['guess']
    pRndm = int(request.session['pRnd'])
    
    if pRndm > request.session['cRnd']:
        request.session['result'] = '<h2 style="background-color:#cf2a27">Too High</h2>'
        return redirect('/') 
    elif pRndm < request.session['cRnd']:
        request.session['result'] = '<h2 style="background-color:#cf2a27">Too Low</h2>'
        return redirect('/') 
    else:
        request.session['result'] = '<h2 style="background-color:#009e0f">' + str(request.session["cRnd"]) +' was the number!</h2>'
        return redirect('/') 