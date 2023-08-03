import datetime
from utility.news_utility import get_news
from utility.weather_utility import get_temperature
now = datetime.datetime.now()

response_dict = {
    "Hello!":['hello','hey','hi'],
    "I\'m doing file and you?":['how','are','you','doing'],
    "Thank you!": ['love','your','work'],
    "Your\'r welcome!":['thanks','thank'],
    now.strftime("%A"):['day','today'],
    now.strftime("%H:%M:%S"):['time'],
    get_news():['news'],
    str(now): ['now'],
    get_temperature() : ['temperature'],
    now.strftime("%Y-%m-%d"): ['date','today']
}

# print(response_dict)

random_response_list = ["Could you please re-phrase that? ",
                "...",
                "I am not sure what you said.",
                "What does that mean?",
                "I could not understand what you just said."]

response_required_words_dict = {
    "Hello!":[],
    "I\'m doing file and you?":['how'],
    "Thank you!": ['love','your']
}