Python classes
==

### Requirements:
* Python **2.7** is the required version of Python for these classes.
* Python libraries required: **IPython notebook**, **Numpy**, **Matplotlib**, **Pandas**, **Django**, **MySQL Connector**, **Boto3**.

**==> If you have an existing Python 2.7 installation:**
* ***pip*** (*should be installed on recent Python distributions*) -  [Installation instructions](http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#install-pip-setuptools-and-wheel).
* ***IPython notebook*** - ```pip install jupyter``` - [Installation instructions](http://jupyter.readthedocs.org/en/latest/install.html)
* ***Numpy***:    ```pip install numpy``` - [Installation instructions](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
* ***Matplotlib***: ```easy_install matplotlib```(Windows) or ```pip install matplotlib```(MacOS) - [Installation instructions]()
* ***Pandas***:   ```pip install pandas``` - [Installation instructions](http://pandas.pydata.org/pandas-docs/stable/install.html)
* ***Django***:
  * ```pip install django``` - [Installation instructions](https://docs.djangoproject.com/en/1.8/topics/install)
  * ```pip install djangorestframework```
  * ```pip install requests```
* ***MySQL Connector***: ```pip install mysql-connector-python --allow-exteernal mysql-connector-python``` [Installation instructions](https://geert.vanderkelen.org/2014/install-mysqlcpy-using-pip/)
* ***Boto3***: ```pip install boto3``` - [Installation instructions](http://boto3.readthedocs.org/en/latest/guide/quickstart.html)

**==> If you don't have any Python 2.7 installation:**

Follow ***either*** one of the following bullets.
The first bullet provides  a minimal installation of Python, allowing you to control your Python installation. The second bullet installs Python Anaconda, a fully-featured Python installation for scientific computing.
* ***Python*** [Installation Instructions](https://www.python.org/downloads/)
  * Once installed, add C:\Python27 and C:\Python27\Scripts to your ```%PATH```.
  * Follow the steps in '==> If you have an existing Python 2.7 installation'.
* ***Python Anaconda*** (fully-featured Python installation for scientific computing): [Installation instructions](http://docs.continuum.io/anaconda/install) - Choose the **Python 2.7** installation.
  * ***Ipython notebook***: ```conda install jupyter```
  * ***Django***:
    * ```conda install -c https://conda.anaconda.org/trentonoliphant django```
  * ***Django rest framework***:
    * ***Windows:*** ```cd C:\anaconda\Scripts``` and ```pip install djangorestframework``` and ```pip install requests```
    * ***MacOS X:*** ```cd ~/anaconda/scripts && pip install djangorestframework && pip install requests```
  * ***MySQL Connector***: ```conda install -c https://conda.anaconda.org/anaconda mysql-connector-python``` [Installation instructions](https://anaconda.org/anaconda/mysql-connector-python)
  * ***Boto3***:
      * ***Windows:*** ```cd C:\Anaconda\Scripts``` and ```pip install boto3```
      * ***MacOS X:*** ```cd ~/anaconda/scripts && pip install boto3```

### Download class materials
* **From Git**:
  * ***git***: [Installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  * ```git clone https://github.com/ocervell/python_classes```

### Run IPython Notebook
**Anaconda distribution:**
* Copy the IPython Notebook launcher from the menu to the desktop.
* Right click on the new launcher and change the ```Start in``` field by pasting the full path of the folder which will contain all the notebooks: ```/path/to/python_classes```.
* Double-click on the IPython Notebook desktop launcher (icon shows [IPy]) to start the Jupyter Notebook App.

**Command line:**
* ```cd /path/to/python_classes```
* ```ipython notebook``` (```ipython/jupyter``` has to be in your ```PATH```)

### Class curriculum
* **1. Python Basics ( ~ 2 hrs)**
  * 1.1. Global concepts & operators
  * 1.2. Numbers
  * 1.3. Strings
  * 1.4. Lists
  * 1.5. Dictionaries
  * 1.6. Sets
  * 1.7. Tuples

* **2. Object-Oriented Programming in Python ( ~ 2 hrs)**
  * 2.1. Python Rules
    * 2.1.1. Concepts
    * 2.1.2. Semantics
  * 2.2. Functions
  * 2.3. Classes
  * 2.4. File input / output
  * 2.5. Exception Handling

* **3. Advanced topics in Python (~ 5 hrs)**

  * 3.1. Parsing
    * 3.1.1. CSV Parsing
    * 3.1.2. JSON Parsing
    * 3.1.3. XML Parsing
    * 3.1.4. Bonus: Pretty Print and Conversion
    * 3.1.5. Exercice: Analyze XML file

  * 3.3. SQL Data Access (MySQL)
    * 3.3.1. Connecting to MySQL DB
    * 3.3.2. Createing / Deleting a database
    * 3.3.3. Creating / Deleting a table
    * 3.3.4. Populating a table
    * 3.3.5. Querying data from a table
    * 3.3.6. OOP Approach

  * 3.4. NoSQL Data Access (DynamoDB)
    * 3.4.1. Connecting to DynamoDB
    * 3.4.2. Creating / Deleting a table
    * 3.4.3. Populating a table
    * 3.4.4. Querying data from a table

  * 3.2. Rest API (Django)
    * 3.2.1. Serialization
    * 3.2.2. Requests and Responses
    * 3.2.3. Class based view
    * 3.2.4. Authentication and Permission
    * 3.2.5. Relationships and HyperLink APIs

  * 3.5. Exercise: Twitter REST API

* **4. Statistics and Machine Learning using Python (~ 6 hrs)**

  * 4.1. Numpy
    * 4.1.1. Arrays
    * 4.1.2. Array indexing
    * 4.1.3. Datatypes
    * 4.1.4. Array math
    * 4.1.5. Broadcasting
    * 4.1.6. Functions

  * 4.2. Matplotlib
    * 4.2.1. Plotting
    * 4.2.2. Subplots

  * 4.3. Pandas
    * 4.3.1. Series
    * 4.3.2. DataFrame
    * 4.3.3. Statistical analysis with pandas

  * 4.4. Exercise: Parse a switch record with Pandas and output to MySQL / DynamoDB