# Own Your Data

For this workshop, we'll be using Python. It'll be useful to know how to code, but the code itself will be fairly easy so if you usually code in a different language, you should still be able to follow along.

We'll be using various Python packages that make it easier to grab data from Google Analytics, Twitter and Facebook. There are almost always equivalent wrappers to make your life easier in other languages. For example, there's [Legato](https://github.com/tpitale/legato) for Ruby which makes the Google Analytics API easier to work with. [GitHub Code Search](https://github.com/search) is a good place to start.

## Setting up your environment

People with a fairly complete development environment may wish to simply add the few Python packages they're missing using: 

    # optionally, set up a virtual environment first
    # (if you don't know what this is, ignore this step)
    
    
    # install all the packages we're going to need
    pip install -r requirements.txt --find-links ./vendor

If you don't have a Python development environment on your computer (or if you'd simply prefer to use a virtual environment you can throw away after the workshop), instead follow these steps: 

1. Go to the vendor directory, install VirtualBox and Vagrant. There are installers for Linux, OS X and Windows, but only for 64-bit machines (most machines nowadays).
2. On the command line, type `vagrant init vendor/own-your-data.box`
3. Run your virtual environment using `vagrant up` and then ssh into it using `vagrant ssh`

Now you can run Python etc. inside of your virtual environment. The directory from which you ran `vagrant init` is synchronized with the virtual machine, meaning that you can put any code there you want and then run it inside of the virtual machine by prepending `/vagrant` to the path. To run `./example.py`, do `python /vagrant/example.py` and it'll just work.

## (Getting ready to) get your data

To get your site's Facebook data, we'll simply use what we can get using the big Export button in Facebook Insights. So grab a couple of months' worth of data from there.

Google has pretty good export functionality too, and you shouldn't be afraid to use it, but to avoid clicking around in the interface for ages, it actually often makes more sense to use the API.

To use the Google Analytics API, you'll need to tell Google that you're building a little application that needs Google Analytics data.

1. Visit the [Google Developers Console](https://console.developers.google.com/project) and create a new project.
2. Go to _APIs & Auth_, then _APIs_, locate the _Analytics API_ in the list and enable it.
3. Go to _Credentials_, click _Create new Client ID_, create an ID for an _installed application_ (this means it runs on your computer, not in a browser)
4. Save these credentials somewhere, e.g. by clicking _Download JSON_. Alternatively, save them in a `.profile` file using `export GOOGLE_ANALYTICS_CLIENT_ID=myclientid` and the same thing for `GOOGLE_ANALYTICS_CLIENT_SECRET`.

If you're using the JSON file with credentials, in your code they'll be available under `installed.client_secret` and `installed.client_id`, so e.g.

    credentials = json.load(open('credentials.json'))
    client_id = credentials['installed']['client_id']
    client_secret = credentials['installed']['client_secret']
