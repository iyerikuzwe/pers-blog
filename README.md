# Personal-blog

A web application where one can start blogs and users can comment on the topic or start a blog of their own.
Live link: https://blog24.herokuapp.com/

### Prerequisites

Python 3.7 required


### Set-Up

To access this app on your local machine:
1) Clone the repo
2) Create a virtual environment then pip install requirements.txt
3) Create a start.sh file and in it export your secret key, mail username and password and add "python manage.py server" 
4) On your terminal run: chmod a+x start.sh
5) Then to run type :./start.sh 


### Features

1. Uses a number of Flask and Python modules.
2. Users log in have an account page get to upload profile pics.
3. Users once logged in can post a blog and comment on blogs posted.
4. Users can subscribe to get emails whenever a new blog has been posted.
## BDD
| Behaviour  | Input | Output |
| ------------- | ------------- |------------- |
| Click on Register button| Fill out form on your details| Register on blog|
| Click on View blogs button| Redirects you to page with blogs| View index page|
| Click on + Start a blog post in navigation bar| Fill out form on details on blogpost you'd like to post| Posts blog|
| Click on blue title in a blog| Opens the blog and comments made on it| See more details on the blogpost|
| Click on comment| Fill out form on what you want to comment on| Comments on the blog|
| Click on trash can in the blogpost| Refreshes the blogs' page minus that blog if you have the access rights | Deletes blog |
| Click on subscribe in navigation bar| Fill out your email address | Subscribes you to the blog to get emails when a new blog is posted |

## Known Bugs

There are no bugs. Incase of any, contact me at iyerikuzweregine19@gmail.com

### Technologies used

This application was made with Python version 3.7 using the flask framework. The templates were made using html and was styles using css and bootstrap 4.

### Support and Contact details

Incase of additions or if you run into any issues, my email address is: iyerikuzweregine19@gmail.com

## License

Copyright (c)  2019 Iyerikuzwe Regine

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




