"""
@author Jacob Xie
@time 5/13/2020
"""

from ftplib import FTP


class FtpHelper(object):
    def __init__(self, host: str, username: str, password: str):
        self.session = FTP(host, username, password)

    def send_file_to_ftp(self, local_file_path: str, target_file_path: str):
        with open(local_file_path, "rb") as file:
            self.session.storbinary(f"STOR {target_file_path}", file)
