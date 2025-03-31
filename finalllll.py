import webbrowser
import pyttsx3  # For text-to-speech

def open_map_route(start_address, end_coordinates):
    """Opens a Google Maps route in the browser."""
    end_lat, end_lon = end_coordinates
    url = f"https://www.google.com/maps/dir/{start_address}/{end_lat},{end_lon}"
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    greeting_message = "Hi, this is the campus navigation bot for Vignan's Institute of Technology and Science (VGNT). Here is the location of the college canteen."
    print(greeting_message)  # Print to the console as well
    engine.say(greeting_message)
    engine.runAndWait()  # Wait for the speech to finish

    start_address = "VITS canteen, 8PVC+HJ7, Vignan Institute of Technology And Sciences Rd, Deshmuki Village, Telangana 501512"
    end_coordinates = (17.3443066, 78.7222610)
    open_map_route(start_address, end_coordinates)
