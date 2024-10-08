import requests

apiKey = "6c4b03db5c334cb2be25edd6c0994c53"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-08&sortBy=publishedAt&apiKey=6c4b03db5c334cb2be25edd6c0994c53"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]: 
      print(article['title'])
