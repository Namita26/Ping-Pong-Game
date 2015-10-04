# Ping-Pong-Game
Virtual Ping-Pong game

Problem Statement: 
Ping-Pong Championship
Description
Implement a virtual Ping-Pong championship, which features 8 players
and 1 referee (all 9 implemented as distinct applications). The 8 players
will be instances of the same app, with different attributes, defined in an
external file
The championship
The Referee program starts and waits all 8 players to join the
championship. When all players have joined, the referee draws the 4 initial
games and notifies the players about their game id, opponent and their
order of play (first, second).
All games are knock-out and supervised by the referee. After all 4 games
have ended, the referee informs the defeated players to shut down,
draws the second round (semi finals), informs the players about their new
game id and opponents. In a similar fashion, the process continues to the
final game and cup winner.
The game
The game starts with the first (offensive) player picking one random
number (from 1 to 10) and informing the referee about it. The defending
player creates a defense array of random numbers (from 1 to 10). The
length of the defense array is preset for each player (see players matrix at
the end of this document) and defined in their individual configuration
files.
If the number picked by the offensive player does not exist in the defense
array, then the player gets one point and plays again. If it exists, the
defender gets the point and they switch roles (defender attacks).
The first player to get 5 points wins the game.
Technical Specifications
All transactions between the referee and the players should be
implemented as a REST API or via function calls.
All 8 Players and the Referee have to run as autonomous applications;
able to communicate with each other via REST API calls.
Pay attention to the proper definition of the REST API routes,
implementation, status codes etc. 
Pay attention to each player identification/authentication (during both of
joining and game processes).
At the end of the championship the Referee should export a report, which
lists all the games, the final scores and the Champion.
You can use any framework and library you want.
Deliverables
Please provide full code required to implement the championship, along
with complete setup instructions.
Please provide the full list of REST API routes supported by both the Referee
and the Player sub-application.
Timeframe
While there is no defined timeframe, it is expected that the time to
complete the assignment would range between 4 and 8 hours.
The Players
Player # Player
Name
Defence
set length
1 Joey 8
2 Nick 8
3 Russel 7
4 Vivek 7
5 Pritam 6
6 Amit 6
7 Chandler 5
8 Colwin 5 

Steps to execute:
  1. cd Ping-Pong-Game/
  2. python apis/referee.py, this starts a flask app referee which contains api for registration/joining of players   for the match
  3. python apis/player.py, this will take player's data from players_info.json and calls post request for     registration. 
  4. After this, game will start between two randonmly generated players and winner's declared. 
