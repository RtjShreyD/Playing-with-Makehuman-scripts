# LOOKUP TABLES-with-Makehuman-scripts 

WE are creating lookup tables for makehuman so that we can relate makehuman inputs with real metric measurements.
Using Makehuman-Master version for Python3 and PyQT5.
Download Makehuman for Python3 from the repository  https://github.com/RtjShreyD/makehuman
and once all dependencies are met and program is running on Linux environment only.......

1. Put fns.py in folder where Makehuman.py file is present, this is the same directory whicch consists of plugins directory.
3. When MH opens save the model that comes by default always by the name default.mhm, in the directory MH saves it by default.
2. Run the scripts from whithin Makehuman GUI scripting TAB and they will work. 

Files Description:
All_modifiers.py : This is the script for setting the parameters for all the available modifiers in a normal humanoid model in Makehuman.

fns.py : This has two functions - measures() & change(). measures() function returns the metric measurements for the current humanoid model selected. change() function compares the new model measurements after change with the old model measurements to generate a comparative measurement array.

Works.py(ALL) : These are the scripts we have been developing to use them to create lookup tables. Earlier we were storing the values in excel, later we shifted to database as handling the indexing of so many values was a tedious task in excel.
    Works4.py- This file runs nested loops for all the parameters and calculates full body measurements for every small change of      0.1(unit) of Makehuman scale in each of the Macro and Measure parameters of Makehuman. There are a total of 24 nested for loops in this, but this script gives an exception: "Too many statically nested blocks", whenever it is run. This is because there is a limit to nesting blocks in Python and is limited to 20 only, so 19 nested blocks can run but as soon as the Interpreter judges more that 19 blocks it gives this exception,and it occurs even before the code starts to run. To solve this problem we have used Works5.py and Works6.py while Works4.py is just a demo file for us now which gives a cear idea as to what we are planning to do. Works3.py is just a demo and incomplete file. Works2.py and Works.py demonstrate the same process but are storing measurements in excel.
    Works5.py & Works6.py- The problem for too many statically nested blocks was solved by creating functions for loop iterations. Both these scripts are having functions doing the loop iterations, however the only difference between the two is Works5.py has a single function named iter() which iterates from 2nd to 18th loop, while Works 6.py is such that the iter() function for loop from Works5.py has been breaken into four separate functions, which makes it a bit more efficient and the system would not hang much.
    






NOTE: We have not gone headless as it is not needed.
