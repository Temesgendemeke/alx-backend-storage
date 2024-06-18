#!/usr/bin/env python3
#!/usr/bin/env python3
""" 102-log_stats """
from pymongo import MongoClient


def print_stats(data, title, sort_key=None, descending=True):
  """Prints formatted statistics for a given data collection.
  """
  print(f"\n{title}:")
  if sort_key:
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=descending)
    for key, value in sorted_data:
      print(f"  {key}: {value}")
  else:
    for key, value in data.items():
      print(f"  {key}: {value}")


if __name__ == "__main__":
  client = MongoClient('mongodb://127.0.0.1:27017')
  logs = client.logs.nginx
  total_logs = logs.count_documents({})

  methods = logs.aggregate([
      {"$group": {"_id": "$method", "count": {"$sum": 1}}}
  ])
  method_counts = {doc["_id"]: doc["count"] for doc in methods}
  status_checks = logs.aggregate([
      {"$group": {"_id": "$status", "count": {"$sum": 1}}}
  ])
  status_counts = {doc["_id"]: doc["count"] for doc in status_checks}

  ip_counts = logs.aggregate([
      {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
      {"$sort": {"count": -1}},
      {"$limit": 10}
  ])
  top_ips = {doc["_id"]: doc["count"] for doc in ip_counts}

  print_stats(data={"total logs": total_logs}, title="Logs")
  print_stats(data=method_counts, title="Methods")
  print_stats(data=status_counts, title="Status checks")
  print_stats(data=top_ips, title="IPs", sort_key=None)

