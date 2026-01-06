def about_us(request):
    return render(request, 'about-us.html')

def our_services(request):
    return render(request, 'our-services.html')


from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404 
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
import uuid
from .models import *
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
def contact_us(request):
    return render(request, 'contact-us.html')

def reg(request):
 
    return render(request, 'register.html')
                  
def register_view(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email') 
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        voter_id=request.POST.get('voter_id')
        myfile = request.FILES['id_proof']
        fs = FileSystemStorage()    
        filename = fs.save(myfile.name, myfile)
        if register.objects.filter(voter_id=voter_id).exists():
            return render(request,'register.html',{'msg':'Voter ID already exists'})
        ins=register(name=name,email=email,phone=phone,password=password,id_proof=filename, voter_id=voter_id)
        ins.save()
        return  render(request,'register.html',{'msg':'Registered Successfully'})


def login(request):
    return render(request, 'login.html')

def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
         request.session['admin'] = 'admin'
         return render(request,'index.html')

    elif register.objects.filter(email=email,password=password).exists():
        users=register.objects.get(email=email,password=password)
        if users.status != 'accepted':
            return render(request, 'login.html', {'message':'Your registration is not yet accepted by the election commission'})
        request.session['uid']=users.id
        return render(request,'index.html')
    

    elif election_commission.objects.filter(email=email,password=password).exists():
        wrk=election_commission.objects.get(email=email,password=password)
        request.session['wid']=wrk.id
        return render(request,'index.html')
    else:
         return render(request, 'login.html', {'message':'Invalid Email or Password'})
    


def logout_view(request):
    # Clear session
    request.session.flush()
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


def viewuser(request):
    users=register.objects.all()
    print("Users:", users)
    return render(request,'viewregister.html',{'users':users})

def update_status(request, user_id, status):
    if not request.session.get('wid'):
        return redirect('login')
    user = register.objects.get(id=user_id)
    user.status = status
    user.save()
    return redirect('viewuser')

def update_voterlist_status(request, voterlist_id, status):
    if not request.session.get('wid'):
        return redirect('login')
    vl = voterlist.objects.get(id=voterlist_id)
    vl.status = status
    vl.save()
    return redirect('view_voterlist')

def add_staff(request):
    if not request.session.get('admin'):
        return redirect('login')
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        print("\nData:", staff_id, name, email, password, phone)
        ins = election_commission(staff_id=staff_id, name=name, email=email, password=password, phone=phone)
        ins.save()
        return render(request, 'add_staff.html', {'msg': 'Staff Added Successfully'})
    return render(request, 'add_staff.html')

def add_election(request):
    if not request.session.get('wid'):
        return redirect('login')
    legislatures = legislature.objects.all()
    elections = election_tbl.objects.all()
    if request.method == "POST":
        legislature_id = request.POST.get('legislature')
        year = request.POST.get('year')
        jurisdiction = request.POST.get('jurisdiction')
        leg = legislature.objects.get(id=legislature_id)
        ins = election_tbl(legislature=leg, year=year, jurisdiction=jurisdiction)
        ins.save()
        return render(request, 'add_election.html', {'msg': 'Election Added Successfully', 'legislatures': legislatures, 'elections': elections})
    return render(request, 'add_election.html', {'legislatures': legislatures, 'elections': elections})

def add_legislature(request):
    if not request.session.get('admin'):
        return redirect('login')
    legislatures = legislature.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ins = legislature(name=name, description=description)
        ins.save()
        return render(request, 'add_legislature.html', {'msg': 'Legislature Added Successfully', 'legislatures': legislatures})
    return render(request, 'add_legislature.html', {'legislatures': legislatures})

def add_constituency(request):
    if not request.session.get('admin'):
        return redirect('login')
    legislatures = legislature.objects.all()
    constituencies = constituency.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        legislature_id = request.POST.get('legislature')
        description = request.POST.get('description')
        leg = legislature.objects.get(id=legislature_id)
        ins = constituency(name=name, legislature=leg, description=description)
        ins.save()
        return render(request, 'add_constituency.html', {'msg': 'Constituency Added Successfully', 'legislatures': legislatures, 'constituencies': constituencies})
    return render(request, 'add_constituency.html', {'legislatures': legislatures, 'constituencies': constituencies})

def add_candidate(request):
    if not request.session.get('wid'):
        return redirect('login')
    constituencies = constituency.objects.all()
    elections = election_tbl.objects.all()
    if request.method == "POST":
        constituency_id = request.POST.get('constituency')
        candidate_name = request.POST.get('candidate_name')
        party_name = request.POST.get('party_name')
        photo = request.POST.get('photo')
        election_id = request.POST.get('election')
        const = constituency.objects.get(id=constituency_id)
        elect = election_tbl.objects.get(id=election_id)
        ins = candidate_tbl(constituency=const, candidate_name=candidate_name, party_name=party_name, photo=photo, legislature=elect.legislature, election=elect)
        ins.save()
        return render(request, 'add_candidate.html', {'msg': 'Candidate Added Successfully', 'constituencies': constituencies, 'elections': elections})
    return render(request, 'add_candidate.html', {'constituencies': constituencies, 'elections': elections})

def add_voterlist(request):
    if not request.session.get('uid'):
        return redirect('login')
    legislatures = legislature.objects.all()
    constituencies = constituency.objects.all()
    elections = election_tbl.objects.all()
    user = register.objects.get(id=request.session['uid'])
    if request.method == "POST":
        constituency_id = request.POST.get('constituency')
        election_id = request.POST.get('election')
        elect = election_tbl.objects.get(id=election_id)
        const = constituency.objects.get(id=constituency_id)
        ins = voterlist(legislature=elect.legislature, constituency=const, election=elect, user=user)
        ins.save()
        return render(request, 'add_voterlist.html', {'msg': 'Applied to Voter List Successfully', 'legislatures': legislatures, 'constituencies': constituencies, 'elections': elections})
    return render(request, 'add_voterlist.html', {'legislatures': legislatures, 'constituencies': constituencies, 'elections': elections})

def view_voterlist(request):
    if not request.session.get('wid'):
        return redirect('login')
    voterlists = voterlist.objects.all()
    return render(request, 'view_voterlist.html', {'voterlists': voterlists})

def view_candidate(request):
    if not request.session.get('uid'):
        return redirect('login')
    user = register.objects.get(id=request.session['uid'])
    # Get approved voterlists for this user
    voterlists = voterlist.objects.filter(user=user, status='active')
    # Get unique elections from voterlists
    elections = list(set(vl.election for vl in voterlists))
    if request.method == 'POST':
        if 'election' in request.POST:
            election_id = request.POST.get('election')
            if election_id:
                election = election_tbl.objects.get(id=election_id)
                # Get voter's constituency for this election
                vl = voterlist.objects.get(user=user, election=election, status='active')
                constituency = vl.constituency
                # Get candidates for this election and constituency
                candidates = candidate_tbl.objects.filter(election=election, constituency=constituency)
                # Check if already voted
                already_voted = vote_tbl.objects.filter(voter=user, election=election).exists()
                return render(request, 'view_candidate.html', {'elections': elections, 'candidates': candidates, 'selected_election': election, 'already_voted': already_voted})
        elif 'candidate_id' in request.POST:
            candidate_id = request.POST.get('candidate_id')
            election_id = request.POST.get('election_id')
            election = election_tbl.objects.get(id=election_id)
            candidate = candidate_tbl.objects.get(id=candidate_id)
            vl = voterlist.objects.get(user=user, election=election, status='active')
            constituency = vl.constituency
            # Check if already voted
            if vote_tbl.objects.filter(voter=user, election=election).exists():
                messages.error(request, 'You have already voted in this election.')
            else:
                vote_tbl.objects.create(election=election, constituency=constituency, candidate=candidate, voter=user)
                messages.success(request, 'Your vote has been cast successfully.')
            # Redirect to view candidates again
            candidates = candidate_tbl.objects.filter(election=election, constituency=constituency)
            already_voted = True
            return render(request, 'view_candidate.html', {'elections': elections, 'candidates': candidates, 'selected_election': election, 'already_voted': already_voted})
    print("Elections:", elections)
    return render(request, 'view_candidate.html', {'elections': elections})

def publish_result(request):
    if not request.session.get('wid'):
        return redirect('login')
    elections = election_tbl.objects.all()
    if request.method == 'POST':
        election_id = request.POST.get('election')
        if election_id:
            election = election_tbl.objects.get(id=election_id)
            # Get all constituencies that have votes for this election
            constituencies = constituency.objects.filter(
                id__in=vote_tbl.objects.filter(election=election).values('constituency').distinct()
            )
            for const in constituencies:
                # Count votes per candidate in this constituency and election
                votes_count = {}
                votes = vote_tbl.objects.filter(election=election, constituency=const)
                for vote in votes:
                    candidate_id = str(vote.candidate.id)
                    votes_count[candidate_id] = votes_count.get(candidate_id, 0) + 1
                # Save to result_tbl
                import json
                result_tbl.objects.update_or_create(
                    election=election,
                    constituency=const,
                    defaults={'votes': json.dumps(votes_count)}
                )
            messages.success(request, 'Results published successfully for the selected election.')
            return render(request, 'publish_result.html', {'elections': elections, 'messages': list(messages.get_messages(request))})
    return render(request, 'publish_result.html', {'elections': elections, 'messages': list(messages.get_messages(request))})

def results(request):
    if not request.session.get('uid'):
        return redirect('login')
    elections = election_tbl.objects.all()
    constituencies = constituency.objects.all()
    selected_results = None
    if request.method == 'POST':
        election_id = request.POST.get('election')
        constituency_id = request.POST.get('constituency')
        if election_id and constituency_id:
            election = election_tbl.objects.get(id=election_id)
            constituency_obj = constituency.objects.get(id=constituency_id)
            try:
                result = result_tbl.objects.get(election=election, constituency=constituency_obj)
                import json
                votes_dict = json.loads(result.votes)
                candidates_votes = []
                for candidate_id, vote_count in votes_dict.items():
                    candidate = candidate_tbl.objects.get(id=int(candidate_id))
                    candidates_votes.append({
                        'candidate': candidate,
                        'votes': vote_count
                    })
                # Sort by votes descending
                candidates_votes.sort(key=lambda x: x['votes'], reverse=True)
                selected_results = {
                    'election': election,
                    'constituency': constituency_obj,
                    'candidates_votes': candidates_votes
                }
            except result_tbl.DoesNotExist:
                messages.error(request, 'No results found for the selected election and constituency.')
    return render(request, 'results.html', {'elections': elections, 'constituencies': constituencies, 'selected_results': selected_results})