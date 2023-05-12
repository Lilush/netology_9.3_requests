from pprint import pprint
import requests
import datetime as dt

class StackOverflow():
    def __init__(self):
        self.baseurl = "https://api.stackexchange.com/2.3/"

    def _get_time(self, days):
        now_date = dt.date.today()
        start_date = now_date - dt.timedelta(days=days)
        secs = dt.datetime(start_date.year, start_date.month, start_date.day).timestamp()
        return int(secs)

    def get_most_activity_python_questions(self, days):
        url = self.baseurl + "questions"
        params = {
            'fromdate': self._get_time(days),
            'order': 'desc',
            'sort': 'activity',
            'tagget': 'python',
            'site': 'stackoverflow',
        }
        response = requests.get(url, params)
        if response.status_code != 200:
            return response.status_code
        titles = []
        data = response.json()
        for item in data["items"]:
            titles.append(item['title'])
        return titles


if __name__ == "__main__":
    stof = StackOverflow()
    pprint(stof.get_most_activity_python_questions(2))