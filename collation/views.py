from django.shortcuts import render
from django.http import JsonResponse
from collation.models import Vote
from constituency.models import Constituency, Region

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def collation(request):
    return render(request, 'collation.html')

def create_collation(request):

    if is_ajax:
        region = Region.objects.get(regional_code=request.POST.get('region'))
        constituency = Constituency.objects.get(constituency_code = request.POST.get('constituency'))
        npp = int(request.POST.get('npp'))
        ndc = int(request.POST.get('ndc'))
        other = int(request.POST.get('other'))


        collation = Vote.objects.create(npp_vote=npp, ndc_vote=ndc, 
                    other_vote=other, region=region, constituency=constituency)
        print(region)
        print(constituency)

        constituency.counted = True
        constituency.save()
        return JsonResponse({"created":'collation'})

    created = f"nothing here"
    return JsonResponse({"created":created})
        
def get_collation(request):
    votes = Vote.objects.raw(f"select id,sum(other_vote) as other ,sum(ndc_vote) as ndc, sum(npp_vote) as npp, sum(ndc_vote+npp_vote+other_vote) as total_votes from collation_vote;")[0]
    other_percent = (votes.other/votes.total_votes)*100
    npp_percent = (votes.npp/votes.total_votes)*100
    ndc_percent = (votes.ndc/votes.total_votes)*100
    total_votes = votes.total_votes

    percentages = {
        "ndc" : ndc_percent,
        "npp" : npp_percent,
        "other" : other_percent,
        "total_votes":total_votes
    }

    return JsonResponse({"data":percentages})