import requests
import redis
import time
from typing import Callable

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    cache_key = f"count:{url}"
    

    redis_client.incr(cache_key)
    
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')
    
    response = requests.get(url)
    html_content = response.text
    
    redis_client.setex(url, 10, html_content)
    
    return html_content


if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    for _ in range(3):
        start_time = time.time()
        content = get_page(test_url)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print(f"Content length: {len(content)}")
        print(f"Access count: {redis_client.get(f'count:{test_url}').decode('utf-8')}")
        print("---")
