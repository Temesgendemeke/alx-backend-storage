#!/usr/bin/env python3
""" Redis """
import redis
import uuid
import typing


class Cache:
    """_summary_"""
    def __init__(self) -> None:
        """_summary_"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """_summary_"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
