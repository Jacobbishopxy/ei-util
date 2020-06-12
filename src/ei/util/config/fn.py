"""
@author Jacob Xie
@time 5/12/2020
"""
from pkg_resources import resource_filename
import yaml


def find_resource_file_from_package(package_name: str, resource_path: str) -> dict:
    return yaml.safe_load(open(resource_filename(package_name, resource_path), "rb"))


def find_resource_file_from_local(resource_path: str) -> dict:
    return yaml.safe_load(open(resource_path, "rb"))

