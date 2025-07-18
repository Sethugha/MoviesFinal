from abc import ABC, abstractmethod
from typing import List, Optional, Dict
#from data_models import User, Movie, UserMovie

class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        """Retrieve all users"""
        pass

    @abstractmethod
    def get_user(self, user_id):
        """Retrieve single user by id."""
        pass

    @abstractmethod
    def get_all_movies(self):
        """Retrieve all movies."""
        pass

    @abstractmethod
    def get_movie(self, movie_id):
        """Retrieve movie by id."""
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """Retrieve user_movies by user_id"""
        pass

    @abstractmethod
    def get_user_movie(self, user_id, movie_id):
        """Retrieve single movie of defined user."""
        pass

    @abstractmethod
    def add_movie(self, title):
        """Add movie.."""
        pass

    @abstractmethod
    def add_user_movie(self, user_id, movie_id):
        """Add movie to users´ list."""
        pass

    @abstractmethod
    def update_user_movie(self, user_id, movie_id, update_data):
        """Renew the rating of a user´s movie."""
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        """Delete movie from db."""
        pass

    @abstractmethod
    def remove_user_movie(self, user_id, movie_id):
        """Remove movie from user´s list."""
        pass

    @property
    @abstractmethod
    def users(self):
        """Property of all users."""
        pass

    @property
    @abstractmethod
    def movies(self):
        """Property of all movies."""
        pass
