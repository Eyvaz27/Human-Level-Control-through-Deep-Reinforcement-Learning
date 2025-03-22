# Human Level Control through Deep Reinforcement Learning
Implementation of Human Level Control through Deep Reinforcement Learning with PyTorch

## How to set up Arcade environments:
- python -m pip install --no-cache-dir --upgrade pip 
- python -m pip install --no-cache-dir pipenv
- pipenv --rm 
- pipenv install numpy scikit-learn pandas seaborn matplotlib ale-py gymnasium[atari] -d --skip-lock 
- pipenv run python -m pip freeze > requirements.txt 
- pipenv --rm 
- pipenv install -r requirements.txt 
- pipenv lock 
- pipenv shell