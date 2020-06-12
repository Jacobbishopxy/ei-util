"""
@author Jacob Xie
@time 5/12/2020
"""
from importlib.resources import read_binary
import yaml


def find_resource_file_from_package(package_name: str, resource_path: str) -> dict:
    return yaml.safe_load(read_binary(package_name, resource_path))


def find_resource_file_from_local(resource_path: str) -> dict:
    return yaml.safe_load(open(resource_path, "rb"))

