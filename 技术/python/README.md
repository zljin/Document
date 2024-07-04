# Study Python

## prepare python visual venv 

We usually use visual python env to isolate another environment.
You can control the version you specify, it is safer and clean dependency resolution

pip is a packaage management tool,the same as maven

```

# 1. install virtualenv tool by pip
pip install virtualenv

# 2. create virtualenv and directory name is venv
virtualenv venv

# 3. switch virtual env
## windows
venv\Scripts\activate
## macbook
source venv/bin/activate 

# 4. view all Dependencies
pip list

# 5. like maven install some Dependencies
pip install -r requirements.txt

# 6. download current Dependencies and version in requirements.txt (optional)
pip freeze > requirements.txt

# 7. logout virtual env
deactive
```

## how to run your python code

```sh
virual_python_bin_path="d:/Codes/gitrepo/corePython/venv/Scripts/"
python_code_dir="d:/Codes/gitrepo/corePython/basics"

${virual_python_bin_path}/python.exe ${python_code_dir}/1.py
```

## IDES
recommend vscode or pycharm

## introduce directory

/basics : python basics code

/oop : Object-oriented code

/third: third lib to use

/commonlib: common lib to use

/assets: some static files

## reference

https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-zh.md#python

https://www.anaconda.com/download/

https://devguide.python.org/


