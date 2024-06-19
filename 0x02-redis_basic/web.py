import requests
from functools import wraps
from datetime import datetime, timedelta

# Define a cache dictionary with expiration time
cache = {}
cache_expiry = 10  # seconds

def memoize(duration):
  """
  Decorator function for caching function results.

  Args:
      duration: The duration in seconds for which the cache entry is valid.

  Returns:
      A decorator function that caches the results of the wrapped function.
  """
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      key = args[0]  # Use the first argument (URL) as the cache key
      if key in cache and cache[key]['expiry'] > datetime.utcnow():
        return cache[key]['data']
      else:
        data = func(*args, **kwargs)
        cache[key] = {'data': data, 'expiry': datetime.utcnow() + timedelta(seconds=duration)}
        # Update access count
        cache[f"count:{key}"] = cache.get(f"count:{key}", 0) + 1
        return data
    return wrapper
  return decorator

@memoize(cache_expiry)
def get_page(url: str) -> str:
  """
  Fetches the HTML content of a URL with caching.

  Args:
      url: The URL of the webpage to fetch.

  Returns:
      The HTML content of the webpage.
  """
  response = requests.get(url)
  response.raise_for_status()
  return response.text


url = "http://slowwly.robertomurray.co.uk"
content = get_page(url)
print(f"Fetched content from {url}")
print(f"Content: {content[:100]}...")

access_count = cache.get(f"count:{url}", 0)
print(f"URL accessed {access_count} times (including this request)")
