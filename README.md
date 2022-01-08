# Ex4
python

in this assignment we were required to create an algorithm that demonstrates a computer game - 
the game's puropse is to move different agents in the best way for them to capture valuable “Pokemons”.
The pokemons are simply points located on the directed graph’s edges that we implemented in the last assignment-each pokemon has a different value given in advance.
 therefore, the agent needs to take (aka walk) the proper edge to “grab” the pokemon,with the goal of maximizing the overall sum of weights of the “grabbed” pokemons.
Note:
The game is being played on a “server” that was given to us. we designed and implemented the client-side (only).



##  algorithm definition:
 in our algorithm, what we do is go over all the pokemons that are currently on the screen (=pokemons that are in the game) , and for each pokemon, we find an agent that will get there the fastest.
 this algorithm relies on the "shortest path" function we created last assignment - this function finds the shortest path from a node on the graph to another node. 
 in our case we used it to find the shortest path from an agent to a pokemon.for each agent we checked the time it will take him to reach the pokemon , and the fastest agent of them all was assigned the task
 


## GUI




## UML




## results


## Running The Program

Open the floder of the project and write this line in the terminal command:

python codes./Ex4.py **
(** enter one of the cases)


<br>
