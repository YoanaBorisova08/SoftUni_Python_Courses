from collections import deque

links = deque([int(x) for x in input().split()])
articles = [int(x) for x in input().split()]
target = int(input())
final_feed = []

while articles and links:
    if articles[-1] > links[0]:
        article = articles.pop()
        link = links.popleft()
        reminder =  article % link
        final_feed.append(reminder)
        if reminder!=0:
            articles.append(reminder*2)
    elif articles[-1] < links[0]:
        article = articles.pop()
        link = links.popleft()
        reminder = link % article
        final_feed.append(-reminder)
        if reminder != 0:
            links.append(reminder * 2)
    else:
        final_feed.append(0)
        articles.pop()
        links.popleft()

print(f"Final Feed: {', '.join([str(x) for x in final_feed])}")
engagement = sum(final_feed)
if engagement >= target:
    print(f"Goal achieved! Engagement Value: {engagement}")
else:
    shortfall = target - engagement
    print(f"Goal not achieved! Short by: {shortfall}")
