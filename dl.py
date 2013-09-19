import onepaperperday
import app_authorization

papers = onepaperperday.get_papers(app_authorization.keys)
for p in papers:
    # the plan is to keep track of which files we've downloaded
    # and download any new files any time the script is run,
    # then send an email to the user notifying them that new
    # papers are waiting to be read
    print(p.id)
