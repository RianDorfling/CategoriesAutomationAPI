# CategoriesAutomationAPI
 
  ![API](https://user-images.githubusercontent.com/105658230/168879994-a209b525-9226-4759-bb12-57c9183ee1df.png)


- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [HOW TO RUN THE TEST](#how-to-run-the-test)


# INSTALLATION

## Install Python

Go to **[Python](https://www.python.org/)**

Go to downloads and select the version to install

The following libraries need to be installed
- pytest
- requests
- jsonpath
- jsonpath_rw_ext

## How to install the libraries
Go to the comand promp and use the following 

`pip install -U pytest`

`pip install -U requests`

`pip install -U jsonpath`

`pip install -U jsonpath_rw_ext`

## Install Pycharm
Go to **[Pycharm](https://www.jetbrains.com/pycharm/)**
	

# DESCRIPTION
The purspose of this test is create an automomated test with the following acceptance criteria:
- Name = "Carbon credits"
- CanRelist = true
- The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"


# HOW TO RUN THE TEST
- Download the source code
- Open Pycharm
- Open project CategoriesAutomationAPI
- Open Run menu
- Select Run under Run Menu or press `shift+F10`

![image](https://user-images.githubusercontent.com/105658230/168870988-84ca7412-ec03-44fd-8917-81fc424bb1d9.png)
- Test results will be displayed

**Alternative**
- Go to `Terminal`

-![image](https://user-images.githubusercontent.com/105658230/168872146-dd7f6ba5-74eb-4cb3-9448-824129e1a801.png)

- Type the following command: `pytest -v TestCases`
- Test results will be displayed 


