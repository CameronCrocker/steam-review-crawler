import requests


def get_reviews(appID):
    """Function which gets the appropriate JSON file from the steamAPI and appends the reviews into a list

    :parameter
    appID - The appID of the steam game
    """

    print("Fetching Reviews..")
    game_url = 'http://store.steampowered.com/appreviews/'+appID+'?json=1&cursor=*&filter=updated'
    response = requests.get(game_url).json()

    reviews_list = []
    for item in response['reviews']:
        reviews_list.append(item)

    while True:  # Loops through while there is a value for 'cursor'
        try:
            game_url = 'http://store.steampowered.com/appreviews/'+appID+'?json=1&cursor='+response['cursor']+'&filter=updated'
            response = requests.get(game_url).json()
            for item in response['reviews']:
                reviews_list.append(item)
        except:
            break
    print("Reviews Collected: " + str(len(reviews_list)))

    return reviews_list  # List contains all gathered reviews


if __name__ == '__main__':
    response_data = get_reviews("1382330")
    print(response_data)