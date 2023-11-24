# imported the datetime module
from datetime import datetime

# creating our database

available_airlines = ['Air Peace', 'Ibom Air', 'United Nigeria', 'Arik Air', 'Green Africa Airline']

flight_desc = {
    'Air Peace':{
        'destination':{
            'Lagos to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            },
            'Asaba to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 35000,
                    'Business class': 45000,
                    'First class': 60000
                }
            },
            'Asaba to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 65000
                }
            },
            'Abuja to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30500,
                    'Business class': 40000,
                    'First class': 70000
                }
            }
        }
    },
    'Ibom Air':{
        'destination':{
            'Lagos to Akwa-ibom': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 35000,
                    'Business class': 45000,
                    'First class': 60000
                }
            },
            'Akwa-ibom to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 45000,
                    'First class': 60500
                }
            },
            'Lagos to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            },
            'Crossriver to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 35000,
                    'Business class': 40000,
                    'First class': 60000
                }
            }
        }
    },
    'United Nigeria':{
        'destination':{
            'Lagos to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 50000
                }
            },
            'Asaba to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 35500,
                    'Business class': 40000,
                    'First class': 55000
                }
            },
            'Enugu to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 60000
                }
            },
            'Abuja to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            }
        }
    },
    'Arik Air':{
        'destination':{
            'Lagos to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            },
            'Enugu to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 45000,
                    'First class': 65000
                }
            },
            'Asaba to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 60000
                }
            },
            'Anambra to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 55000
                }
            }
        }
    },
    'Green Africa Airline':{
        'destination':{
            'Lagos to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 60000
                }
            },
            'Asaba to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            },
            'Imo to Abuja': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 40000,
                    'First class': 70000
                }
            },
            'Abuja to Lagos': {
                'times': ['06:00', '12:00', '18:00'],
                'ticket fee': {
                    'Economy': 30000,
                    'Business class': 45000,
                    'First class': 70000
                }
            }
        }
    }
}

passengers = {

}

# getting basic user information
user_name = input('Please enter your first and last name: ').strip().title()
first_name = user_name.split()[0]
last_name = user_name.split()[1]

print(f'\n***Hey there {user_name}!, nice to have you here***\n        Welcome to Group D flight services!')

# displaying different airlines travel route
print('\nHere are the available flights')
for airline in available_airlines:
    print(f'\n{airline}')
    for index, value in enumerate(list(flight_desc[airline]["destination"]), start = 1):
        print(f'{index}. {value}')

# user airline selection
while True:
    print('\nEnter your prefered airline')
    for index, value in enumerate(available_airlines, start = 1): # displaying the available airlines
        print(f'{index}. {value}')
    while True:    
        airline = input(f'\n{first_name}, please choose an airline from the list of available airlines: ').strip().title()
        if airline not in available_airlines:
            print(f'{airline} is not an available airline, please choose from the list above.')
        elif airline in available_airlines:
            break
    print(f'\nWelcome to {airline}, {user_name}\n')
    print('Select a number from the available flights to proceed with your booking')
    index_list = []
    for index, value in enumerate(flight_desc[airline]['destination'], start = 1):
        index_list.append(index)
        print(f'{index}. {value}')

    # passenger's flight destination selection
    while True:    
        destination = input('\nPlease choose the corresponding number to your destination: ')
        if destination.isdigit():
            destination = int(destination)
            if destination not in index_list:
                print('Please enter a valid destination number')
            else:
                break
        else:
            print('Please enter a digit from the listed destinations')

            # getting passenger's preferred flight time
    for index, value in enumerate(flight_desc[airline]['destination'], start = 1):
        if destination == index:
            print(f'\nHere are the times for {value} flights')
            time_list = []
            for index, times in enumerate(flight_desc[airline]['destination'][value]['times'], start = 1): 
                time_list.append(index)                       
                print(f'{index}. {times}')
            while True:
                flight_time = input('Please select the corresponding number to your desired flight time: ')
                if flight_time.isdigit():
                    flight_time = int(flight_time)
                    if flight_time not in time_list:
                        print('Please enter a valid flight time number')
                    else:
                        break
                else:
                    print('Please enter the corresponding digit to your preferred flight time')

            for index, time in enumerate(flight_desc[airline]['destination'][value]['times'], start = 1):
                if flight_time == index:
                    num_of_adults = input('\nEnter number of adults: ')  # getting number of adult passengers
                    if num_of_adults.isdigit():
                        num_of_adults = int(num_of_adults)
                        num_of_infants = input('Enter number of infants: ')  # getting number of infants 
                        if num_of_infants.isdigit():
                            num_of_infants = int(num_of_infants)
                        else:
                            print(f'Please {first_name} enter a number.')
                    else:
                        print(f'Please {first_name} enter a number')

                        # getting passenger's flight date
                    while True:
                        input_date = input('\nEnter the date for your flight in the format (YYYY-MM-DD): ')
                        try:
                            flight_date = datetime.strptime(input_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0) # converting the input to an actual date
                            current_time = datetime.now()
                            time_difference = flight_date - current_time  # getting how far away the flight date is
                            if time_difference.days >= 0:
                                break
                            else:
                                print("You can't enter a past date. Try that again")   
                        except ValueError:
                            print('Invalid date format')

                        # computing our discount
                    days_difference = time_difference.days
                    if days_difference <= 29:
                        discount = 1
                    elif days_difference <= 90:
                        discount = 1.5
                    elif days_difference > 90:
                        discount = 2
                    
                    # getting passenger's desired flight class
                    print('\nHere are the available flight classes')
                    type_list = []
                    for num, flight_type in enumerate(flight_desc[airline]['destination'][value]['ticket fee'], start =1):
                        type_list.append(num)
                        print(f'{num}. {flight_type}')
                    while True:
                        flight_class = input('\nPlease enter the corresponding number to your desired flight type: ')
                        if flight_class.isdigit():
                            flight_class = int(flight_class)
                            if flight_class in type_list:
                                break
                            else:
                                print(f'{flight_class} is an invalid input.')
                        else:
                            print(f'\n{first_name}, please enter the corresponding digit to your desired flight type')

                    for num, flight_type in enumerate(flight_desc[airline]['destination'][value]['ticket fee'], start =1):
                        if flight_class == num:
                            
                            # getting ticket type (one-way or round trip) and displaying passenger's flight information
                            ticket_type = input(f'\nPlease {first_name}, enter 1 for a one-way ticket or 2 for a return ticket: ').strip()
                            if ticket_type == '1':
                                for location in flight_desc[airline]['destination']:
                                    if location == value:
                                        total_fee = round(((flight_desc[airline]['destination'][location]['ticket fee'][flight_type] 
                                                        * num_of_adults) + (10000 * num_of_infants)) / discount, 2)
                                        ticket_id = f'{last_name[-1:-3]}{first_name[1:3]}-{value[:3]}-{ticket_type}'
                                        print(f'\nOne way flight booking for {user_name},\n{flight_type} From {location}\nOn {flight_date.date()} costs: N{total_fee} and is scheduled for {time}\nTicket ID: {ticket_id}')
                                        print(f'\nThank you {user_name} for flying with {airline}, we love you.\n')
                            elif ticket_type == '2':
                                for location in flight_desc[airline]['destination']:
                                    if location == value:
                                        total_fee = round((((flight_desc[airline]['destination'][location]['ticket fee'][flight_type] 
                                                        * num_of_adults) + (10000 * num_of_infants)) * 1.5) / discount, 2)
                                        ticket_id = f'{last_name[-1:-3]}{first_name[1:3]}-{value[:3]}-{ticket_type}'
                                        print(f'\nTwo-way flight booking for {user_name},\n{flight_type} From {location}\nOn {flight_date.date()} costs: N{total_fee} and is scheduled for {time}\nTicket ID: {ticket_id}')
                                        print(f'\nThank you {user_name} for flying with {airline}, we love you.\n')
                            else:
                                print(f'Please {first_name} you have to choose 1 or 2')

                            date = flight_date.date() 
                            passengers.update({               # adding passenger's flight information to our database
                                'passenger name': user_name,
                                'Ticket ID': ticket_id,
                                'airline' : airline,
                                'destination' : value,
                                'flight time' : time,
                                'flight class': flight_type,
                                'num of adult(s)' : num_of_adults,
                                'num of infant(s)' : num_of_infants,
                                'flight date' : date,
                                'ticket type' : ticket_type,
                                'travel cost' : total_fee
                            })

                            print("Passenger's Details")
                            for key, value in passengers.items():          
                                print(f'{key} : {value}')                                 
    break