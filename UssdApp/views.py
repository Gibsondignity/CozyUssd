from pydoc import locate
from tkinter.messagebox import NO
from urllib import response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import User, Booking, AppartmentLocation


# Create your views here.
def displayApartments(locations):
    response = ""
    locationLen = len(locations)
    for location in locations:
        if locationLen == 1:
            response+= f"{location[0]}"
        
    return response


def handleUserRespoonse(locations):
    for location in locations:
        return



def getUserResponse(userResponse):
    userResponse = userResponse+1


@csrf_exempt
def Ussd(request):

    if request.method == 'POST'and request.POST:

        sessionId = request.POST.get('sessionId')
        serviceCode=request.POST.get('serviceCode')
        phoneNumber=request.POST.get('phoneNumber')
        text=request.POST.get('text')
        now = datetime.datetime.now()
        print(now)
       

        textList= text.split('*')
        userResponse= textList[-1].strip()

        print(userResponse)
        # Handle back if 
        try:
            #4. Check the level of the user from the DB and retain default level if none is found for this session
            session = User.objects.get(phoneNumber = phoneNumber)
            level = session.level


        except User.DoesNotExist as e:
            level=0     





        try:

            result,created = User.objects.get_or_create(phoneNumber=phoneNumber)    
            
            if created:
                result.save()       

            print(level)
            print(userResponse)
           

            if result and result.firstName and result.secondName and result.email and result.city:
                print("I'm here")
                if level == 0 or level == 1:
                    
                    if userResponse == "":
                        #print("I'm here too")
                        locations = AppartmentLocation.objects.all()
                        locList = []
                        for location in locations:
                            locList.append(location)


                        print(displayApartments(locList))
                        # locationLen = len(locList)
                        # print(locationLen)


                        if level == 1:
                            response = f"CON Hello {result.firstName}, Please choose an appartment to book.\n"

                            
                            response+= f"1. {locations[0]}\n"
                            response+= f"2. {locations[1]}\n"
                            response+= f"3. {locations[2]}\n"
 
                            
 


                        return HttpResponse(response, content_type='text/plain')

                




            else: #registering the user

                if created: #chek if user is in the microfinance table
                
                    result.save()#save the user in the microfinance table
                    response= "CON Welcome to Cozypropertiesgh.\n" 
                    response+= "Please enter your first name"
                    

                    return HttpResponse(response, content_type='text/plain')

                if not created:
                    if not result.firstName:
                        #save the name
                        result.firstName = userResponse
                        result.save()

                    
                        response= "CON Please enter your Second Name"
                        
                        return HttpResponse(response, content_type='text/plain')

                    if not result.secondName:
                        #save the city
                        result.secondName = userResponse
                        result.save()

                    
                        response ="CON Please enter your Email"
                        return HttpResponse(response, content_type='text/plain')
                

                    if not result.email:
                        #save the city
                        result.email = userResponse
                        result.level=1
                        result.save()

                    
                        response ="CON Please enter your City."
                        return HttpResponse(response, content_type='text/plain')
            
                    if not result.city:
                        #save the city
                        result.city = userResponse
                        result.level=1
                        result.save()

                    
                        response = "END You have successfully been registered\n" 
                        response+= "Please Dial The code to book now."
                        return HttpResponse(response, content_type='text/plain')
            



        except Exception as e:

            print('exception', e)


            #11g. Request for city again
            response = "END Apologies, something is wrong... \n"

            # Print the response onto the page so that our gateway can read it
            return HttpResponse(response, content_type='text/plain')

        

        #return HttpResponse(response, content_type='text/plain')

    return HttpResponse(request, content_type='text/plain')