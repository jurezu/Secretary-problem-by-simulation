# Secretary problem by simulation

Secretary problem which is also known as the marriage problem, the sultan's dowry problem, the fussy suitor problem, the googol game, and the best choice problem.

More about problem on [wikipedia](https://en.wikipedia.org/wiki/Secretary_problem).


The program is running arbitrary number of simulations provided by the user.
It will find optimal threshold R and average score of finding the best candidate among the list of candidates.
Also, number of candidates can be passed as a parameter. Default value is 100.

The following logic is used:

* Reject the first R candidates.
* Then hire the first one you see that is better than the best among the first R.




## Getting started

* install python 3 distribution
* install libraries from requirements.txt via pip
```
pip install -r requirements.txt
```
* or create anaconda environment from environment.yml file 
```
conda env create -f environment.yml
```



## Running the code

```
python simulation.py <number of candidates>
```
