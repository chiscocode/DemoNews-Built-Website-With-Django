# DemoNews-Built-Website-With-Django
The aim of this website is to enable general public get latest gist and information of what is happing in our environment.


### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/chiscocode/DemoNews-Built-Website-With-Django.git

```

--> Move into the directory where we have the project files : 
```bash
cd DemoNews-Built-Website-With-Django

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment on windows:
```bash
envname\scripts\activate

```
or 
```
source env/bin/activate
```
 on Mac and Linux.


--> Install the requirements :
```bash
pip install -r requirements.txt

```

Make migrations with: 
```
python manage.py makemigrations
``` 
and then
 ```
python manage.py migrate
```.

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<br/>
<div align="center">
  Customer Home<br/>
 <img src="screenshot.PNG" width="800px"</img> 

</div>

    


## License
MIT License

Copyright (c) 2022 Chukwudifu Patrick Chimezie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

