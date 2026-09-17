# python-fastapi
1. install uv package 
pip install uv

2. Run project setup command using uv
uv init --no-package

3. Add packages
uv add fastapi[standard]
uv add wikipedia
uv add --dev pytest
uv add --dev pytest-cov
uv add --dev black
uv add --dev fire
