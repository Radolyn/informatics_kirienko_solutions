from utils import run_python_tool

run_python_tool('pip install --upgrade pip')

run_python_tool('pip install requests BeautifulSoup4 lxml autopep8 yapf --user')

print('Done. Happy hacking :)')
