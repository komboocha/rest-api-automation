BASE_URL = 'https://g07547egsi.execute-api.eu-west-1.amazonaws.com/dev'

animals_url = f'{BASE_URL}/animals'
authorized_url = f'{BASE_URL}/authorized'
players_url = f'{BASE_URL}/players'


def animal_details_url(animal_id):
    return f'{animals_url}/{animal_id}'


def player_details_url(player_id):
    return f'{players_url}/{player_id}'


def goals_details_url(player_id):
    return f'{players_url}/{player_id}/score'



