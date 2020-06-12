call activate py36

rmdir /s/q dist
rmdir /s/q build

python setup.py bdist_wheel

twine upload --repository-url http://192.168.50.130:8091/repository/qi-pipy-hosted/ dist\*.whl -u admin -p admin123

pip uninstall ei.util -y
pip install ei.util
