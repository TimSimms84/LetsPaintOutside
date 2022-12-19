## CUSTOM API 

This project is a small database with information about all 403 episodes of The Joy Of Painting with Bob Ross.

The front end of this project is a small application that authenicates users and stores their information in a MongoDB (Atlas)

To use this program you first need to go into the /API/ folder and execute the script launch_api.bash. This will create the database if it doesn't exist and use a uvicorn server and FastAPI to serve data from the database.


You must then open another terminal and navigate to the /frontend/ folder and execute the script ./launch_frontend.bash

You must create an account and login to use the search.

Here is a current list of available search terms.

'barn', 'beach', 'boat', 'bridge', 'building', 'bushes',
'cabin', 'cactus', 'cirrus', 'cliff', 'clouds', 'conifer',
'cumulus', 'deciduous', 'dock', 'farm', 'fence', 'fire',
'flowers', 'fog', 'grass', 'hills', 'lake', 'lakes',
'lighthouse', 'mill', 'moon', 'mountain', 'mountains',
'night', 'ocean', 'palm_trees', 'path', 'person', 'portrait',
'river', 'rocks', 'snow', 'snowy_mountain', 'structure', 'sun',
'tree', 'trees', 'waterfall', 'waves', 'windmill', 'winter'
