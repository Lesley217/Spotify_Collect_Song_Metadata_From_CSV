# Scraping Information from Spotify about Songs by Importing a csv file 

### This is a project that aims at collecting information about songs by importing a csv file from your local directory and is written in python.

## Instructions 

1. Make a new csv file
 First of all, make a new csv file that includes song name and artist name. By only including the song name and artist name in the csv file, other information of the song can be collected (i.e. release date, popularitiy, album name) by running the scrape_info_of_song_spotify.py file. An example of the csv file, 'English_songs.csv' can be found above.
 
2. Download required modules
 Before running the scrape_info_of_song_spotify.py file, please install the requried modules. The required modules are as follows:
    - requests (pip install requests)
    - urllib (pip install urllib3)
    - dotenv (pip install python-dotenv)
    - os (pip install os-sys)
    - pandas (pip install pandas)
    - csv (pip install python-csv)
    - json (no need to install, installed with Python package)

 Other modules (required if method 2 authentication was used):
    - base64 (pip install pybase64)
    - webbrowser (no need to install, installed with Python package)

3. Sign up for Spotify Developer and collect the required information for authentication
Sign up for a Spotfiy Developer account and then create a new project in the Dashboard. There, you can find <strong>Client ID</strong> and <strong>
Client Secret </strong>. Press the 'Edit Settings' button and add <strong>redirect uris</strong>. An example will be http://localhost:8888/callback. Then, go to your personal Spotify profile to find your username. Below is the checklist of information to be collected from Spotify:
    - Client ID
    - Client Secret
    - Username

4.  Create a '.env' file in the same local directory
Check the .env file attached. Change the information accordingly to the variables and save the file. You can ignore 'CODE' if you are not using method 2 authentication that was commented in the scrape_info_of_song_spotify.py file.

For those using method 2 authentication, after inputting all the above details, you can follow the instructions below and add 'CODE' later.

5. Run scrape_info_of_song_spotify.py file
Upon runnning the code, user has to type the name of the csv file. An example here will be 'English_songs.csv'. Then, a new csv file, named 'spotify_output.csv' should be generated. You can then check the information about the songs. 

<h5> Method 2 authentication (those using Method 1 can skip this part) </h5>
After typing the name of the csv file, a webbrowser should be opened. Check the screenshot in 'code sample received for auth_headers.png', copy the code after 'code=' and paste the 'CODE' in the env file. Run the code again and type name of csv file, it should work the same as Method 1.

6. Results in CSV file
Open the CSV file, information about the song (uri, release date, duration(ms) and popularity) should be scraped from Spotify. For songs that cannot be found in Spotify, the results should be shown with 'N/A'. For other results, sometimes songs that are similiar to the ones you are typed may be included in the csv file.

## Find a bug ?

If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with fix, reference the issue you created 

## Limitations

Both song name and artist name has to added to the csv file in order to scrape information about the songs.

## Known issues

This project is still ongoing. The automation of scraping information about the songs from spotify has not been completed. This is coming soon.
