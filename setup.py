"""
@author Jacob Xie
@time 12/10/2019
"""

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    str_list = [line.strip(' \n') for line in f]
    install_reqs = [s for s in str_list if not s.startswith('#') and s != '']

setup(name="ei.util",
      version="0.0.2",
      description="EI Util",
      author="Jacob Xie",
      author_email="jacobbishopxy@gmail.com",
      namespace_packages=["ei", "ei.util"],
      packages=find_packages("src"),
      package_dir={"": "src"},
      python_requires=">=3.7",
      install_requires=install_reqs,
      zip_safe=False)

if __name__ == '__main__':
    # print(install_reqs)

    pass
