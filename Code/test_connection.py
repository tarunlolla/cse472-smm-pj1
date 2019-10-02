import tweepy

def tweepy_conn_test(conn_details):

    auth = tweepy.OAuthHandler(conn_details['consumer_key'], conn_details['consumer_secret'])
    auth.set_access_token(conn_details['access_token'], conn_details['access_token_secret'])
    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        print("Found screen name : "+api.me().screen_name)
    except:
        print("Error trying to authenticate. Please check your credentials")
        exit(1)

def main():
    keys_file=open("conn_details.txt",'r')
    lines=keys_file.readlines()
    conn_details=dict()
    for line in lines:
        a=line.rstrip().split('=')
        conn_details[a[0]] = a[1]
    keys_file.close()
    if conn_details['consumer_key'] == '':
        conn_details['consumer_key'] = input("No Consumer Key found in file. Please enter a consumer key: ")
    if conn_details['consumer_secret'] == '':
        conn_details['consumer_secret'] = input("No Consumer Secret Key found in file. Please enter a consumer secret key: ")
    if conn_details['access_token'] == '':
        conn_details['access_token'] = input("No Access Token found in file. Please enter an Access Token: ")
    if conn_details['access_token_secret'] == '':
        conn_details['access_token_secret'] = input("No Secret Access Token found in file. Please enter a Secret Access Token: ")
    tweepy_conn_test(conn_details)


if __name__ == '__main__':
    main()
