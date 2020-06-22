from requests import get

# Considering each pages separately as there is only 2 pages
# if more pages then it is not a good idea.
page_1 = get('https://jsonmock.hackerrank.com/api/article_users?page=1').json()
page_2 = get('https://jsonmock.hackerrank.com/api/article_users?page=2').json()

def getUsernames(threshold_value):
    """
    This Method is used to get most active authors based on submission count.
    :param threshold_value: threshold value which is compared to submission count.
    :return: active authors
    """
    author_list = []
    for users in page_1['data']:
        if users['submission_count'] > threshold_value:
            author_list.append(users['username'])
    for users in page_2['data']:
        if users['submission_count'] > threshold_value:
            author_list.append(users['username'])

    return author_list

usernames = getUsernames(10)
print("Most Active Authors : ")
for user_name in usernames:
    print(user_name)
