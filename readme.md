Set up virtual environment
- check pip version: 
PS D:\Repos\pyalgo101> pip --version
pip 20.0.2 from c:\programdata\miniconda3\lib\site-packages\pip (python 3.6)

- install virtualenv
PS D:\Repos\pyalgo101> pip install virtualenv

- create new virtual environment for you project
PS D:\Repos\pyalgo101> python -m venv algoenv

Notice that you can use any name for your environment, we used algoenv here.
The above command will create new folder named algoenv for your virtual environment.

- activate your virtual environment
PS D:\Repos\pyalgo101> algoenv/scripts/activate
(algoenv) PS D:\Repos\pyalgo101>

Notice the (algoenv) prefix indicated that it is activated

- deactivate
(algoenv) PS D:\Repos\pyalgo101> deactivate
PS D:\Repos\pyalgo101>

TDD with PyTest
- install pytest
(algoenv) PS D:\Repos\pyalgo101> pip install pytest

- install pytest-cov
(algoenv) PS D:\Repos\pyalgo101> pip install pytest-cov

- create the tests folder then put all of your tests under it.
    - all test files must follow the following convention: test_<test_name>.py
    - all test function must follow the following convention: test_<test_name>
        
        def test_add2num:
            pass
        def test_multiply2num:
            pass

- to run tests
    PS> python -m pytest -v