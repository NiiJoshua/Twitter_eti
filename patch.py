# all api setting apply
# update to api excludes wait_on_rate_limit_notify=True
api = tw.API(auth, wait_on_rate_limit=True)
# The function is okay but the argument has updated
tweets = tw.Cursor(api.search_tweets, q=query, lang="en",since_id=date_since).item(count)