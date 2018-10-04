To run the scripts follow the steps:(Linux/Windows)

1. Open command line/terminal ---> pip install xlwt
2. In Windows locate xlwt folders in Python2.7>lib>site-packages> xlwt & xlwt-1.3.0.dist-info and copy these two and paste in plugins directory of Makehuman package. For windows the two xlwt folders are also present in this package so can be pasted directly into plugins.
   In Linux will have to locate the same above folders and paste in plugins of Makehuman.
3. Inside the Makehuman bundled package(in the main folder where plugins directory is located) either in Linux or in Windows paste all these files except xlwt folders.
4. Open Makehuman software GUI and under utilities--> Scripting tab, either paste the contents of works.py file or open works.py
5. Execute in Makehuman GUI.
4. Similarly trial3_Allmodifiers2.py script can also be run. This script can generate any kind of humanoid model if we set values accordingly in the script.

Note: lookup.xlsx file is also present in the folder that can just demonstrate how the script has written data till now.
      Script is still under development so a whole lot of changes have to be made while adding more nested for loops, currently only Muscle has been changed and a demo table is created
      
For Export to Matlab:-
Use trial3_Allmodifiers2.py script when we have to set the modifiers value in a script and then export the human body images to MATLAB for measurement computation.
Follow the steps to export the model as an image:-
1. Open MH--->set White background+Grid off+Show wire mesh+Show smoothened mesh. This has to be the state of model before script is run.
Note: White background scaling will give problems when height is increased, as the humanoid will become longer than the background and then while exporting into MATLAB a perfect binary image will not be created. To solve this issue before starting Makehuman, copy 0_modelling_backgrounds.py file from here and replace it with the same file in Makehuman directory. I have changed the background scaling in this file so that it does not affect the export to MATLAB.
2. After above conditions met run the script the screenshots will be saved. Locate them in Makehuman folder/Grab/  in My documents(Windows) andin Home/Makehuman/v13py/grab/ in Linux. 

For any kind of guidance/assistance Makehuman community forums is very helpful visit http://www.makehumancommunity.org/forum/
And create an account for posting queries
