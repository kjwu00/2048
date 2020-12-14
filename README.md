# What's in a Game: Solving 2048 with Reinforcement Learning

Please view paper.pdf for a more detailed write up of this project.

##

Game AI agents are a common sub-field of artificial intelligence research. One of the most well known agents is Alpha Go Zero which achieved superhuman performance in the game Go without the aid of human supervision. In this project, we implemented an agent which uses the Monte Carlo Tree Search algorithm to play the game 2048. We compared three different value functions: the merge score of the game (the sum of all merged tiles throughout the game), the largest tile on the final board of the game (with ties broken by the sum of the tiles on the final board), and the sum of all of the tiles on the final board of the game. We evaluated agents using the percentage of games it achieves the 2048 tile in, the average sum of the final board for the games it plays, and the average merge score for the games it plays. We found that using the sum of the tile on the final board of the game as the evaluation policy allows us to obtain the largest percentage of games where the tile 2048 is achieved, largest average sum of the final board, and largest average merge score.
