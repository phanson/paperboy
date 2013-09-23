import email_settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import onepaperperday
from onepaperperday import serialize
import app_authorization
import StringIO

COMMASPACE = ', '

msg = MIMEMultipart()
msg['Subject'] = email_settings.subject
msg['From'] = email_settings.from_addr
msg['To'] = COMMASPACE.join(email_settings.to_addr_list)

papers = onepaperperday.get_papers(app_authorization.keys)
html = StringIO.StringIO('<html><head></head><body>')
serialize.to_html(papers, html)
html.write('</body></html>')

htmltext = html.getvalue()
htmlpart = MIMEText(htmltext, 'html', 'utf-8')
msg.attach(htmlpart)
html.close()

s = smtplib.SMTP()
s.connect(email_settings.server)
s.login(email_settings.username, email_settings.password)
s.sendmail(email_settings.from_addr, email_settings.to_addr_list, msg.as_string())
