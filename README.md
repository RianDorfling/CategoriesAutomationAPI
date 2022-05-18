# AUTOMATION API TESTING OF CATEGORIES
 <div id="top"></div>
<!--   ![API](https://user-images.githubusercontent.com/105658230/168879994-a209b525-9226-4759-bb12-57c9183ee1df.png) -->

<div align="center">
<a href="https://user-images.githubusercontent.com/105658230/">
    <img src="https://user-images.githubusercontent.com/105658230/168879994-a209b525-9226-4759-bb12-57c9183ee1df.png" alt="Logo" width="180" height="180">
</a>
</div>

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
Go to the comand promp and execute the following commands 

Install pytest library 
```sh
pip install -U pytest
```

Install requests library

```sh
pip install -U requests
```

Install jsonpath library
```sh
pip install -U jsonpath
```

Install jsonpath rw ext library
```sh
pip install -U jsonpath_rw_ext
```

## Install Pycharm
Go to **[Pycharm](https://www.jetbrains.com/pycharm/)**

Install Pycharm IDE (Community Edition is good enough)

<p align="right">(<a href="#top">back to top</a>)</p>

# DESCRIPTION
The purspose of this test is to create an automomated test with the following acceptance criteria:
- Name = "Carbon credits"
- CanRelist = true
- The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"


<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>
