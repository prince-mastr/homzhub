# Welcome to Homzhub

Here I Have Tried to Create a Request Support System <br />
Where You can
See Status of  Request
Detail View of Request
Update Request(Admin Only)

Before Doing All above You need to Register as User
So Let's Start <br />
<br />
<br /> 
# Getting Started <br />

$ git clone <br />
$ source homzhub/bin/activate <br />
$ cd homzhub <br />
$ pip install -r requirements.txt<br />
$ python manage.py makemigrations <br />
$ python manage.py migrate <br />
$ python manage.py runserver <br />


## How to Use: <br />

**Just Hit Url** = "http://127.0.0.1:8000/" in any Browser <br />
Register Yourself

Click On Requests 
Create, View, Or Update Requests

# For Detail Request:
**Just Hit Url** = "http://127.0.0.1:8000/accounts/requestdetail/<int:id>/" in any Browser where id is Request id <br />

# For Update Request:
**Just Hit Url** = "http://127.0.0.1:8000/accounts/updaterequest/<int:id>/" in any Browser where id is Request id <br />

# For Request List:
**Just Hit Url** = "http://127.0.0.1:8000/accounts/requests/" in any Browser where id is Request id <br />


## Authors <br />
Prince Agarwal 
