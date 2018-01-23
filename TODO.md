WHAT STILL NEEDS TO HAPPEN:

1. Get adding/editing pokemon working
  - ~~javascript doesn't show up~~
  - ~~doesn't modify database~~
  - Prevent user from selecting a move multiple times
  - When edited a pokemon, the previous moves, ability, etc. should show.

2. Get editing a team working
  - trying to change the name/version/description of an already-existing team
    throws a database error
  - Limit amount of pokemon to 6. Flashes "You can have no more than 6 pokemon per team" if user attempts to add more.

3. Get strengths/weaknesses working !!!!!!!!
  - requires several helper functions and some api work
  - Make two functions in api.py that returns strength and weakness values in an array. 
       -One function for single-typed pokemon, the other for double-typed

4. Aesthetic changes
  - make sure all color schemes work
  - make sure everything is readable
  - make sure everything looks nice

5. Video!
  - we'll decide on something when we meet on Tuesday
  
6. Documents
  - Update DESIGN.pdf
  - Update README.md
  
Lastly, make a fresh new clone and confirm the app works.
