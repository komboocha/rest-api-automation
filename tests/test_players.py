import pytest
import requests
import endpoints
import random


def generate_player_payload():
    return {
        "club": random.choice(["FC Barcelona", "Real Madrid", "Manchester United", "Bayern Munchen"]),
        "name": f'{"player"}{random.randint(1, 80)}'
    }


@pytest.fixture
def player_id():
    payload = generate_player_payload()
    new_player_response = requests.post(endpoints.players_url, json=payload)
    assert new_player_response.status_code == 201
    player_id = new_player_response.json()['id']
    return player_id


class TestPlayers:

    def test_get_list_of_players(self):
        response_players = requests.get(endpoints.players_url)
        assert response_players.status_code == 200

    def test_create_new_player(self, player_id):
        player_details_response = requests.get(endpoints.player_details_url(player_id))
        assert player_details_response.status_code == 200

    def test_update_player(self, player_id):
        updated_payload = generate_player_payload()
        updated_player_response = requests.put(endpoints.player_details_url(player_id), json=updated_payload)
        updated_player_dict = updated_player_response.json()
        assert updated_player_response.status_code == 202
        assert updated_player_dict['name'] == updated_payload['name']

        get_updated_player = requests.get(endpoints.player_details_url(player_id))
        updated_player_dict = get_updated_player.json()
        assert updated_player_dict['name'] == updated_payload['name']

    def test_delete_player(self, player_id):
        delete_player_response = requests.delete(endpoints.player_details_url(player_id))
        assert delete_player_response.status_code == 204

        get_deleted_player_response = requests.get(endpoints.player_details_url(player_id))
        assert get_deleted_player_response.status_code == 404

    def test_player_goals(self, player_id):
        goals_header = {'API-KEY': 'V1stul4!@2021'}
        goals_response = requests.post(endpoints.goals_details_url(player_id), headers=goals_header)
        assert goals_response.status_code == 200

        goals_response = requests.post(endpoints.goals_details_url(player_id), headers=goals_header)

        goals_dict = goals_response.json()
        player_goals = goals_dict['goals']
        assert player_goals == 2
