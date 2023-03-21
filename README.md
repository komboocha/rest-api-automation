# rest-api-automation

The following API to manage footbal players is given. Base URL address is: 
https://g07547egsi.execute-api.eu-west-1.amazonaws.com/dev

The API resource GET /players contains the list of players. It should always return 200 response code.

1. You can create a new player with JSON:
```
{
    "club": "FC Porto",
    "name": "player1"
}
```
via POST `/players` request. After successfully creating a player 201 response and JSON with player's ID are returned.
```
{
    "club": "FC Porto",
    "goals": "0",
    "id": "da45fcbc-4be3-4bd7-a141-2747c2a209c8",
    "name": "player1"
}
```
If you are missing the required keys 400 response code is returned.

2. Downloading player's details (GET /players/ID), returns 200 and players details, if the player exisits. If the players doesn't exist - 404 code is returned.

3. Player's details can be updated with PUT /players/ID and JSON:
```
{
    "club": "New Club",
    "name": "player1"
}
```
After a successful update a 202 and updated player's details are returned. If the player doesn't exist - 404, if required keys are missing - 400.

4. To delete a player use: DELETE /players/ID. It returns 204 code and an empty response if the player was in the API, if the player doesn't exit - 404 error is returned.

5. You can increase player's goals by 1 using: POST /players/ID/score (without body).
Endpoint requires API-KEY header and V1stul4!@2021 value. It should return 200, no header - 401, incorrect header - 403.


The following test for the API have been written:
- Get the list of players.
- Create a new player and ask for their details. 
- Update an existing player and check their details after the update. 
- Delete an existing player and assert they don't exist in the API anymore. 
- Increase player's goals by 2 and check the new number in player's details. 
