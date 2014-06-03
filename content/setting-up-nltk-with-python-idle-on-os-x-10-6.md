Title: Setting up nltk with Python IDLE on OS X (10.6)  
Date: 2011-03-06 01:36  
Author: chris  
Category: Uncategorized  
Slug: setting-up-nltk-with-python-idle-on-os-x-10-6  

UPDATE (2/6/14): The right way to do this is to ignore this post and go get [virtualenv] [1].

Having spent a frustrating couple of hours on trying to set up the
Python IDLE and nltk module so I can teach myself some text mining
basics, I thought it would be worth noting the problems I had and how I
solved them.  [This thread] [2] charts similar problems to mine, but I
resolved mine in a different way to the suggestions given. Basically,
the issue stems from installing a new version of Python alongside the
one that came with your Mac.

Instructions for setting up [nltk](http://www.nltk.org/download) can be found at. Macs ship with Python installed, but the
IDLE app either does not come with OSX or is not enabled.  nltk.org
recommends upgrading to the latest Python before installing the nltk
module, so naturally I downloaded 2.7.1 (not going to 3.x), which also
comes with the IDLE app. I then installed PyYAML and nltk as the
instructions say.  In the folder with the IDLE app is a handy script to
update your .bash\_profile, which I ran.

Python 2.7 would run in Terminal, but `import nltk` would not work
either in Terminal or IDLE.  Despite editing $PATH and my .bash\_profile
as suggested on various websites, I couldn't get nltk to install its
files on this new version of Python.  The nltk website suggests: `cd
/tmp/nltk-installer` and then `sudo python setup.py install` but
this didn't fix it for me (seems like this would just run the installer
again?).

After lots of head-scratching over how environment variables work and
running the nltk installer many times, I realised all I needed to do
was, in the Finder, copy the files nltk installer had placed at
/Library/Python/site-packages/2.6/ to the location of the 2.7 install at
/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/

After this `import nltk` worked immediately and
rage levels subsided noticeably.  Highly recommended.
 
[1]: https://pypi.python.org/pypi/virtualenv 		"virtualenv"
[2]: http://groups.google.com/group/nltk-users/browse_thread/thread/e14b647243ca5b66	"this thread"
