# Spotify Lyrics Desktop Widget

## Front-End

The desktop widget is implemented using a cross-platform framework called [ElectronJS](https://www.electronjs.org/)

## Back-End

The lyrics for a song played on Spotify is received using the Spotify API and Genius API. Both APIs are implemented on Python.

Documentation can be found here : [Link to the Python code](https://towardsdatascience.com/become-a-lyrical-genius-4362e7710e43)

## How to set up

1. Clone the repository to local machine.
2. Set up Python virtual environment in the `/backend` directory

In the `/backend` directory,

On macOS: `python3 -m venv venv` to create a virtual environment.

On Windows: `py -m venv venv`

3. Run the Python virtual environment

Once in the `/backend` directory,

On macOS: `source venv/bin/activate` to activate virtual environment.

On Windows: `.\env\Scripts\activate`

4. `pip3 install -r requirements.txt` to install all dependencies

5. In the main directory, run `npm install` to install add node dependencies.

## How to run
1. Run `npm start` and then `npm run make` in your command line terminal
