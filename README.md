Interested in climate change, I wanted to do something to develop a program that allows us user to see the recent changes in our environment.

This project uses GIBS API, a form of REST API, from NASA to fetch two images, and compare between the two. The comparison was done using Pixel Subtraction, which is pretty straight forward, it first calculate the numeric value of each pixel from one image to another and then subtracts them.

I implemented a .JSON file for our database to keep track of each individual landmark. In order to add an landmark to the database, you havee to look for an landscape that you want to include, and add the following in order: Min Lat, Min Long, Max Lat, Max Long.


### **Goals in the future:**
- Change the comparison from pixel subtraction
  - Pixel Subtraction is poorly done because of how sensitive the picture can be from misalignment, clouds, time of day, and more.
  - Currently thinking of neural network, SVM and some other machine learning, but those are often slow in runtime.
- Look for a bigger database
  - In hopes of storing data locally to a more live database like SQL.
- Make it more user friendly so users don't have to look up the BBOX of the landmark
  - Might implement some sort of chatbox or redesign the entire format

