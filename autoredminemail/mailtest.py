import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Preconfig the mail from and mail to ids
def mail_list_predefine():
    lineidx = 0
    mmt = open('MAIL_TR_DEF.txt', 'r',encoding='UTF-8')
    for line in mmt:
        if lineidx == 1:
            r_username = line

        if lineidx == 3:
            r_password = str(line)

        if lineidx == 5:
            r_mail_from = line

        if lineidx == 7:
            r_mail_receipts = line

        if lineidx == 9:
            r_mail_subject = line

        lineidx += 1
    mmt.close()
    time.sleep(1)

    return r_mail_from,r_mail_receipts,r_mail_subject


username = "lance.yen@technexion.com"
password = "vzynvdfrdmcnkgmb"
#mail_from = "lance.yen@technexion.com"
#mail_receipts = "hsinchi.yen@gmail.com,lance.yen@technexion.com"
#mail_subject = "Please Update Redmine Issues"

mail_from, mail_receipts, mail_subject = mail_list_predefine()

#import a mail body from external text file RM_MSB_BODY.TXT
msgbody = open('RM_MSG_BODY.txt','r',encoding='UTF-8')
mail_body = msgbody.read()
msgbody.close()

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_receipts
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()

print('Mails is sent to receipts : %s' %mail_receipts)
print('done !')
