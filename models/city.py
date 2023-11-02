#!/usr/bin/python3
""" Module for City """
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ defines attributes for City """
    """ subclass of BaseModel """
    state_id = ""
    name = ""
