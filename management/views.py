from django.shortcuts import render,redirect

from django.views.generic import View


from . models import Participant

from django.db.models import Q


# Create your views here.


class GetParticipant:

    def get_participant(self,request,uuid):

        try:
                        
            participant = Participant.objects.get(uuid=uuid)

            return participant
        
        except:

            return render(request,'errorpages/error-404.html')
        
class DashboardView(View):
    
    def get(self, request, *args, **kwargs):
    
        from .models import Event

        total_events = Event.objects.count()
    
        total_participants = Participant.objects.count()
    
        active_events = Event.objects.filter(active_status=True).count()
    
        recent_events = Event.objects.order_by('-created_at')[:5]


        return render(request, 'dashboard/dashboard.html', {
          
            'total_events': total_events,
          
            'total_participants': total_participants,
                   
            'active_events': active_events,
          
            'recent_events': recent_events,
        })

    
class ParticipantListView(View):
    
    def get(self, request, *args, **kwargs):
    
        query = request.GET.get('query')
        
        participants = Participant.objects.filter(active_status=True)

        if query:
            
            participants = participants.filter(
            
                Q(name__icontains=query) |
            
                Q(email__icontains=query) |
            
                Q(event__name__icontains=query)
            )

        return render(request, 'participants/display_events_participants.html', {'participants': participants})
    

class ParticipantDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        participant = GetParticipant().get_participant(request,uuid)

        participant.active_status = False

        participant.save()

        return redirect('participants-list')
    



    git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sonuamal333/Event-mangement-System.git
git push -u origin main