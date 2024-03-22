# need install requests and urllib
# pip install requests urllib
import requests

def get_user_choose():
    '''
    Get the 2 or 1 entered by the user.
    If the input is not 0 or 1, the user needs to re-enter
    :return: 2 or 1
    '''
    while True:
        try:
            user_input = int(input('input your choice: '))
            if user_input == 1 or user_input == 2:
                return user_input
            else:
                print('Your output is wrong, please re-enter')
        except:
            print('Your output is wrong, please re-enter')


if __name__ == "__main__":

    # Prompt user for input
    print('The functions we provide are as follows')
    print('[1] Get the number of astronauts')
    print('[2] Get the current International Space Station location\n')

    # Get the 2 or 1 entered by the user
    user_input = get_user_choose()

    # log
    with open('log.txt', 'a') as file:
        file.write(f'user input {user_input}\n')

    # If it is 1, then enter the astronaut of the current space station
    if user_input == 1:
        url = 'http://api.open-notify.org/astros.json'
        response = requests.get(url).json()
        peoples = response['people']
        for index, people in enumerate(peoples):
            print(f'astronaut {index + 1}:')
            name = people['name']
            craft = people['craft']
            print(f'name: {name}')
            print(f'craft: {craft}')

            # log
            with open('log.txt', 'a') as file:
                file.write(f'astronaut {index + 1}:\n')
                file.write(f'name: {name}\n')
                file.write(f'craft: {craft}\n')
    # If it is 2, then output the current position of the International Space Station
    else :
        url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(url).json()
        position = response['iss_position']
        lat = position['latitude']
        lon = position['longitude']
        print('The current location of the International Space Station is as follows:')
        print(f'latitude: {lat}')
        print(f'longitude: {lon}')

        # log
        with open('log.txt', 'a') as file:
            file.write('The current location of the International Space Station is as follows:\n')
            file.write(f'latitude: {lat}\n')
            file.write(f'longitude: {lon}\n')


