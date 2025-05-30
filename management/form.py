from django import forms

from .models import Participant

class SubscriberRegisterForm(forms.ModelForm):

    class Meta:

        model = Participant

        exclude = ['uuid', 'active_status','created_at','updated_at']  

        widgets =   {'id': forms.TextInput(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-select',
                                                  'placeholder': 'Enter full name',
                                                  'required': 'required'}),

                    'name': forms.TextInput(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-select',
                                                      'placeholder': 'Enter phone number',
                                                      'required': 'required'}),

                    'email': forms.EmailInput(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-select',
                                                     'placeholder': 'Enter email address',
                                                     'required': 'required'}),

                    'event': forms.TextInput(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-select',
                                                    'placeholder': 'Enter place'}),
                                                    
                                                    
                    'registration_date': forms.DateInput(attrs={'class': 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-select',
                                                    'placeholder': 'Enter place'}),}                          
                                                    
                                                    
                                                    
                                                    
        
                    


    