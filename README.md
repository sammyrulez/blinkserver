Blink Server
============

The Blink Server is a configurable "hook service" to connect [obscure] cloud service with a nice, local [blink(1)](http://blink1.thingm.com) USB RGB LED.

Installation
============
 - install [libusb](http://www.libusb.org/) ( on OSX use ''brew install libusb'')
 - clone this repo
 - (Optional but strongly suggested) create a virtualenv
 - install requirements
 ```bash

 pip install -r requirements.txt

 ```
 - run the server
 ```bash

python manage.py runserver

 ```

 For setting up a proper enviroment for a Djnago application see [here](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/uwsgi/)


Requirements
============

 - pyusb >= 1.0.0
 - Django==1.5c2
 - South==0.7.6
 - django-admin-bootstrapped==0.3.2
 - a pyusb backend like libusb
 - probably has to run with root privileges on Linux in order to send raw USB messages

License
=======
[MIT](http://en.wikipedia.org/wiki/MIT_License)



>Copyright (c) 2013 sammyrulez
>
>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



The blink1 module has been written by Sam Merritt (I'm another Sam) you can find his orginal work [here](https://github.com/smerritt/pyblink1)
