from ftplib import FTP_TLS


def do(ftp_server_address, ID, PW):
    ftp_tls = FTP_TLS(ftp_server_address)
    ftp_tls.login(user=ID, passwd=PW)
    file_list = ftp_tls.nlst()
    ftp_tls.quit()
    return file_list


# test_code
print(do("test.rebex.net", "demo", 'password'))