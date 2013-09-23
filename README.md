# Paperboy

Utility to get a uniform description of the latest recommendations from [OnePaperPerDay](https://twitter.com/onepaperperday) on Twitter.

Useful for automatically downloading the papers or setting up a notification system.

## Dependencies

 * [python-twitter](http://code.google.com/p/python-twitter/)
 * [Requests](http://docs.python-requests.org/en/latest/)

## Runtime Version

Tested under Python 2.7.3.

## Setup

Prior to using the built-in CSV or HTML exporters, create a file called `app_authorization.py` in the project directory. Put your Twitter API keys into a `keys` dictionary like so:

    keys = {
        'consumer_key':  '...',
        'consumer_secret': '...',
        'access_token_key': '...',
        'access_token_secret': '...'
    }

This will allow the built-in utilities to use your Twitter oAuth credentials to check the timeline. Note that `onepaperperday.get_papers()` requires a dictionary argument of this form when using it directly.

To use the email digest functionality (perhaps as a cron job), create a file called `email_settings.py` in the project directory. Place your email server information and credentials in the file as shown below:

   server = 'smtp.example.com'
   username = 'mailer'
   password = 'hunter2'
   from_addr = 'mailer@example.com'
   to_addr_list = ['Yourself <you@example.com>']
   subject = 'OnePaperPerDay Weekly Digest'

Then set up `digest.py` to run automatically on a fixed interval. In the future the digest script will remember which papers it has already sent and cull repeats from the list.
