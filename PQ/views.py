from django.shortcuts import render

def BASE(request):
    return render(request,'pages/accueil.html')
def contact_view(request):
    return render(request, 'pages/contact.html')

def inscription_view(request):
    return render(request, 'pages/inscription.html')


def connexion_view(request):
    return render(request, 'pages/connexion.html')



def validsim_view(request):
    return render(request, 'pages/validation_sim.html')


def dashbord_u_view(request):
    return render(request, 'pages/user_dashboard.html')

def dashbord_a_view(request):
    return render(request, 'pages/admin_dashboard.html')