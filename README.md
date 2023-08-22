# It's Rock Paper Scissors lol
## Semi-Important Notes
The only thing worth noting is the use of math.ceil() instead of round(). Since Python 3 uses [Banker's Rounding](https://wiki.c2.com/?BankersRounding), using round() to calculate the amount of wins needed gave unwanted results. For example: if the user wanted to play 5 rounds, round(5/2) would give 2 instead of 3. This made a selection of Bo5 function the same as Bo3.
### Less Important Notes 
I am fully aware Lines 98 and beyond are sloppy. There is undoubtedly a better way to handle the inifinite gameplay loop, and I may refactor it at a later date. Consider it in the changelog for v1.5 if I ever come back to this.
