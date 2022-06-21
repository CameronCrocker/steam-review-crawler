import requests
import sys


class Review:
    pass


def get_reviews(appID):
    """Function which gets the appropriate JSON file from the steamAPI

    :parameter
    appID - The appID of the steam game
    """

    game_url = 'http://store.steampowered.com/appreviews/'+appID+'?json=1'
    return requests.get(url=game_url).json()


if __name__ == '__main__':
    try:
        response_data = get_reviews("1382330")
    except:
        sys.exit(1)

    print(response_data['reviews'])  # Output of all of the reviews for appID 1382330
