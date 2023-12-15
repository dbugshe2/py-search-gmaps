
from src.gmaps import Gmaps
from botasaurus import bt

import os
import shutil

try:
    # Try to get the path using shutil
    chrome_path = shutil.which("chrome") or shutil.which("google-chrome")
    # Set the CHROME_PATH environment variable only if chrome_path is not None
    if chrome_path is not None:
        # Set the path to your Chrome executable
        os.environ['CHROME_PATH'] = chrome_path
    print("Chrome executable path:", chrome_path)
except AttributeError:
    print("Shutil does not support which() on this platform.")
except Exception as e:
    print(f"An error occurred: {e}")


default_max = 20


def jump_lines(count=2):
    print("\n" * count)


def get_user_inputs(prompt="Type some text then hit ENTER (type 'done' to finish): "):
    # get each config from user
    user_inputs = []
    while True:
        user_input = input(prompt + ":> ")
        jump_lines()
        if user_input.lower() == '':
            break  # Exit the loop if the user enters 'done'
        else:
            user_inputs.append(user_input)
    return user_inputs


def get_user_input(prompt):
    user_input = input(
        prompt + "\n Hit ENTER when you're done \n:>  ")
    jump_lines()
    return user_input


def get_user_number_input(prompt="Type some text then hit ENTER (type 'done' to finish):> "):
    # get each config from user
    try:
        user_input = input(prompt + "\n:> ")

        if (user_input != ""):
            user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    return user_input


def scrape_data(queries, **other_config_options):
    # run the scrape fucntion given api key and config
    if (other_config_options):
        Gmaps.places(queries, fields={
                     Gmaps.ALL_FIELDS}, **other_config_options)
    else:
        Gmaps.places(queries, fields={Gmaps.ALL_FIELDS})


def save_to_csv(data, output_file='output.csv'):
    # save scrape result to csv file
    # Data to write to the file

    # Write the data to the file "data.json"
    bt.write_json(data, "data.json")

    # Read the contents of the file "data.json"
    print(bt.read_json("data.json"))

    # Write the data to the file "data.csv"
    bt.write_csv(data, output_file)

    # Read the contents of the file "data.csv"
    print(bt.read_csv(output_file))


if __name__ == "__main__":

    other_config = {}

    jump_lines()
    print("==========HI 👋 ============")
    queries = get_user_inputs(
        "PLACES: Search for places (eg: Restaurants in Abuja) then Hit ENTER")
    jump_lines()

    print("✅ Sucsess:\tSearch Queries Collected Succesfully...")
    jump_lines()

    print("🎉\Aiit nigga answer a few questions below, \nhint: hit ENTER to accept the default (the value in brackets).")
    jump_lines()

    max = get_user_number_input("how many records (all)")
    jump_lines()

    # should_scrape_socials = get_user_input(
    #     "should we scrape for socials E-Mail etc.\n yes/no (no)")
    # jump_lines()

    # if (should_scrape_socials == "yes"):
    #     YOUR_API_KEY = get_user_input(
    #         "Aiit then, Enter yourr RapiApi key")
    #     other_config["key"] = YOUR_API_KEY
    #     jump_lines()

    if (max == ""):
        results = scrape_data(queries, **other_config)
    else:
        results = scrape_data(
            queries, max=max, default_max=100000, **other_config)

    if results:
        print("QUERIES:")
        jump_lines()
        print(queries)
        save_to_csv(results)
        jump_lines()
        print("🎉 Data successfully saved to 'output.csv' Cheers man 🥂")
