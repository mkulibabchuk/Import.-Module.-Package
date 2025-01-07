import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при запросе к URL: {url}. Код статуса: {response.status_code}")

if __name__ == "__main__":
    data = fetch_data('https://jsonplaceholder.typicode.com/posts')
    for post in data[:3]:
        print(post['title'])