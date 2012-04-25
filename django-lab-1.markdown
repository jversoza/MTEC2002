---
layout: default
title: MTEC2002 - Django Lab 1 - Hello World
---
Django Lab 1 - Hello World
===

###Objectives
* Install Django
* Create a hello world web application by using Django's URL dispatcher, views and templates

###Installing Django
__In terminal:__

<ol>
<li>
Install django using pip

{% highlight bash %}
pip install django
{% endhighlight %}
</li>
<li>
Check your installation

{% highlight bash %}
which django-admin.py
{% endhighlight %}

You should see the following as a result:
<pre>
/usr/local/bin/django-admin.py
</pre>
If nothing is returned, the installation did not work.  Look through the output of your pip install command to track down the reason why.  You can even run <code>pip install django</code> again try to reproduce what happened.
</li>
</ol>

###Prepping your working directory
__In terminal:__

<ol>
<li>
Clone the mtec2002_assignments repo into a folder in <code>Desktop</code>
{% highlight bash %}
cd Desktop
git clone https://your_user_name@github.com/your_user_name/mtec2002_assignments.git
{% endhighlight %}
</li>
<li>
Change your directory so that you're in <code>mtec2002_assignments</code>
{% highlight bash %}
cd your_user_name
{% endhighlight %}
</li>

<li>
Check that you're in the right place - this should return something like <code>/Users/student/Desktop/your_user_rname/mtec2002_assignments</code>
{% highlight bash %}
pwd
{% endhighlight %}
</li>

<li>
Make a directory for <code>class12</code> and cd into it
{% highlight bash %}
mkdir class12
cd class12
pwd
{% endhighlight %}
This time, you should be in the class12 directory: <code>/Users/student/Desktop/your_user_rname/mtec2002_assignments/class12</code>.

If you're not in this directory, check your path against <code>/Users/student/Desktop/your_user_rname/mtec2002_assignments/class12</code>.  Find where there is a discrepency and go through these steps again to see how to fix it.
</li>
</ol>

###Starting a new Django project and adding an app
__In terminal:__

<ol>
<li>
Start your project
{% highlight bash %}
django-admin.py startproject helloworld
{% endhighlight %}
List the files that were created.
{% highlight bash %}
ls
{% endhighlight %}
This should return:
{% highlight bash %}
helloworld
{% endhighlight %}
</li>

<li> 
Add an app to your project by using manage.py.
{% highlight bash %}
cd helloworld
python manage.py startapp hello
{% endhighlight %}
List the files that were created.
{% highlight bash %}
ls
{% endhighlight %}
This should return:
<pre>
hello		helloworld	manage.py
</pre>
List the files in the hello app.
{% highlight bash %}
ls hello
{% endhighlight %}
This should return:
<pre>
__init__.py	models.py	tests.py	views.py
</pre>
</li>
</ol>

###Running the dev server
__In terminal:__

<ol>
<li>
Make sure you're in your <code>helloworld</code> project directory.  If you're not, <code>cd</code> into it.
</li>
<li>
Run the dev server
{% highlight bash %}
python manage.py runserver
{% endhighlight %}
This should return the following:
<pre>
Validating models...

0 errors found
Django version 1.4, using settings 'helloworld.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
</pre>
</li>
<li>
You can view your application at:  <code>http://localhost:8000/</code>
</li>
</ol>

###Mapping a URL to a view

__Create a url at /hello__

<ol>
<li>
With the dev server running, verify that the URL does not exist yet.  Open <code>http://localhost:8000/hello</code> in your browser.  You should see a page that has an error: <code>Page not found (404)</code>.
</li>
<li>Add the new URL to your application.  Open <code>helloworld/helloworld/urls.py</code> in your text editor (this should be in your class12 folder).</li>
<li>Before the last set of closing parentheses, add this line (including the comma):
{% highlight python %}
url(r'^hello/$', 'hello.views.hello'),
{% endhighlight %}
</li>
</ol>


###Checking your work so far
<ol>
<li>
Check your work by going copying and pasting <code>http://localhost:8000/hello</code> into your browser
</li>
<li>
You should get a page that says:
<code>ViewDoesNotExist at /hello</code>
</li>
This means that a view function has to be written.  A view was mapped to in urls.py, but it wasn't mapped to yet.
</ol>

###Creating a view
<ol>
<li>Open <code>helloworld/hello/views.py</code> in your text editor (this should be in your class12 folder).</li>
<li>Add the following to the file
{% highlight python %}
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world.")
{% endhighlight %}
</li>
<li>
Open <code>http://localhost:8000/hello/</code> in your browser.  You should see:
<pre>
Hello world.
</pre>
</li>
<li>
Try modifying what the index method returns so that it responds with an actual html document.  Try wraping the text in strong tags.
</li>
</ol>


###Using a template
<ol>
<li>Open <code>helloworld/hello/views.py</code> in your text editor (this should be in your class12 folder).</li>
<li>
Add this to the top of the file:
{% highlight python %}
from django.template import Context, loader
{% endhighlight %}
</li>
<li>
Replace the body of the index function (that is, the entire <code>return</code> statement) with this code:
{% highlight python %}
    t = loader.get_template('hello/index.html')
    d = {}
    c = Context(d)
    return HttpResponse(t.render(c))
{% endhighlight %}
</li>
<li>
Open <code>http://localhost:8000/hello/</code> in your browser.  You should see:
<pre>
TemplateDoesNotExist at /hello/
</pre>
</li>
<li>Use <code>pwd</code> to make sure that you're in <code>/Users/student/Desktop/yourusername/mtec2002_assignments/class12/helloworld</code>.  If you're not:
{% highlight bash %}
cd /Users/student/Desktop/yourusername/mtec2002_assignments/class12/helloworld
{% endhighlight %}
</li>
<li>
Make a <code>templates</code> directory in your <code>helloworld</code> project's directory
{% highlight bash %}
mkdir -p templates/hello
{% endhighlight %}
</li>
<li>
Create a file called <code>helloworld/templates/hello/index.html</code>in your text editor.
</li>
<li>
{% highlight html %}
<!doctype html>
<html>
<body>
<b>hello world</b>
</body>
<html>
{% endhighlight %}
</li>
<li>
Add the templates directory to your application's settings.  Open <code>helloworld/helloworld/settings.py</code>.  Find this block of code. 
{% highlight python %}
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
{% endhighlight %}
Add this line (your templates folder) before the closing parentheses:
{% highlight python %}
	"/Users/student/Desktop/yourusername/mtec2002_assignments/class12/helloworld/templates/",
{% endhighlight %}
</li>
<li>
	Restart your development server by pressing control-C and <code>python manage.py runserver</code>
</li>
<li>
	Try adding a variable to your view and displaying it in your template by using this in your view: <code>d = {'greeting': 'hello'}</code>
</li>
</ol>

###Other things to try
<ol>
<li>
Add another url, view, and template: 

<code>http://localhost:8000/howdy/</code>.

It should it display howdy universe in italics.
</li>
</ol>

