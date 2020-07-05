import zmail
from tools.project_path import test_report_path, test_image_path, mail_config_path
from tools.read_config import ReadConfig


class SendMail:

    @staticmethod
    def send():
        # html报告地址
        with open(test_report_path, 'r', encoding="utf-8") as f:
            content_html = f.read()

        mail_config = eval(ReadConfig.get_config(mail_config_path, 'Mail', 'mail'))

        mail = {
            'subject': mail_config['subject'],  # Anything you want.
            'content_text': mail_config['content_text'],  # Anything you want.
            # 'content_html': content_html, # Body html
            'attachments': mail_config['attachments'],  # Absolute path will be better.
        }

        server = zmail.server(mail_config['sender'],
                              mail_config['auth'],
                              smtp_host=mail_config['smtp_host'],
                              smtp_port=mail_config['smtp_port'])
        server.send_mail(mail_config['receiver'], mail, cc=mail_config['cc'])
