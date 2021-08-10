#This is a python script for sending reminder email to bug review meeting members.
#Created date : 20210809
#Applied Platform : Windows 10 , Office 365 Outlook
#Author : Lance Yen

import smtplib,time
import re
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Preconfig the mail from and mail to ids
def mail_list_predefine(paramfile):
    lineidx = 0
    mmt = open(paramfile, 'r',encoding='UTF-8')
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

def body_date_modify():
    now = datetime.now()

    line_idx = 0
    cur_date = now.strftime("%m/%d")

    f = open('RM_MSG_BODY.txt', 'r', encoding='UTF-8')
    fw = open('NEW_RM_MSG_BODY.txt', 'w', encoding='UTF-8')

    for line in f:

        if line_idx == 2:
            newline = re.sub('\d{1,2}\/\d{1,2}', cur_date, line)
            fw.writelines(newline)
        else:
            fw.writelines(line)

        line_idx += 1

    f.close()
    fw.close()
    time.sleep(1)

    os.remove("RM_MSG_BODY.txt")
    os.rename("NEW_RM_MSG_BODY.txt", "RM_MSG_BODY.txt")
    time.sleep(1)


username = "lance.yen@technexion.com"
password = "vzynvdfrdmcnkgmb"
#mail_from = "lance.yen@technexion.com"
#mail_receipts = "hsinchi.yen@gmail.com,lance.yen@technexion.com"
#mail_subject = "Please Update Redmine Issues"

#load parameters from external file
mail_from, mail_receipts, mail_subject = mail_list_predefine('MAIL_TR_DEF.txt')

#START - import a mail body from external text file RM_MSB_BODY.TXT
msgbody = open('RM_MSG_BODY.txt','r',encoding='UTF-8')
mail_body = msgbody.read()
msgbody.close()
#END - import a mail body from external text file RM_MSB_BODY.TXT

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
