from datetime import datetime
import requests
import uuid


class Review:
    def __init__(self, id, author, date, hours, content, comments, source, helpful, funny, recommended
                 , franchise, game_name):
        self.id = id
        self.author = author
        self.date = date
        self.hours = hours
        self.content = content
        self.comments = comments
        self.source = source
        self.helpful = helpful
        self.funny = funny
        self.recommended = recommended
        self.franchise = franchise
        self.game_name = game_name

    def get_content(self):
        return self.id, self.author, self.date, self.hours, self.content, self.comments, self.source, self.helpful, \
               self.funny, self.recommended, self.franchise, self.game_name



def get_reviews(appID, source, franchise, game_name):
    """Function which gets the appropriate JSON file from the steamAPI and appends the reviews into a list

    :parameter
    appID - The appID of the steam game
    """

    print("Fetching Reviews..")
    reviews_list = []
    cursor = "*"

    while True:  # Loops through while there is a value for 'cursor'
        try:
            game_url = 'http://store.steampowered.com/appreviews/' + appID + '?json=1&cursor=' + cursor + '&filter=recent'
            response = requests.get(game_url).json()
            cursor = response['cursor']
            for item in response['reviews']:
                author = uuid.uuid5(uuid.NAMESPACE_DNS, item['author']['steamid'])
                date = datetime.fromtimestamp(item['timestamp_created']).strftime('%d-%m-%y')

                item['recommendationid'] = Review(item['recommendationid'],  # ID
                                                  author,  # Review Author
                                                  date,  # Date review was written
                                                  item['author']['playtime_forever'],  # Total play time of reviewer
                                                  item['review'],  # Review content
                                                  item['comment_count'],  # Comments on the review
                                                  source,  # Platform review was written on
                                                  item['votes_up'],  # Review helpful count
                                                  item['votes_funny'],  # Review funny count
                                                  item['voted_up'],
                                                  # If the reviewer recommended the game or not (True/False)
                                                  franchise,  # Franchise of the game
                                                  game_name  # Game Name
                                                  )

                reviews_list.append(item['recommendationid'])

        except:
            break
    print("Reviews Collected: " + str(len(reviews_list)))

    return reviews_list # List contains all gathered reviews


if __name__ == '__main__':
    review_ids = get_reviews("1382330", "steam", "Persona", "Persona 5 Strikers")
