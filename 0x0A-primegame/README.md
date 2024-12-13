# Prime Number Removal Game

* **Game**
  * Two players take turns removing prime numbers and their multiples from a set of consecutive integers
  * Player who cannot make a move loses the round

* **Function Signature**
  * `def isWinner(x, nums)`
    * `x`: Number of game rounds
    * `nums`: Array of maximum integers per round

* **Rules**
  * Start with consecutive integers from 1 to n
  * Players choose prime numbers strategically
  * Removing a prime number eliminates that prime and all its multiples

* **Constraints**
  * Maximum `n` and `x` is 10000
  * No external package imports
  * Optimal play is assumed

* **Output**
  * Returns name of player with most round wins
  * Returns `None` if winner cannot be determined