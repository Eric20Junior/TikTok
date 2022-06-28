from http import client
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, JoinEvent, LikeEvent, ShareEvent, GiftEvent, FollowEvent, ViewerCountUpdateEvent

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="growparty724", **(
        {
            "enable_extended_gift_info": True
        }
    )
)

@client.on("connect")
async def on_connect(event: ConnectEvent):
    print("Connected To Room ID: ", client.room_id)

@client.on("join")
async def on_join(event: JoinEvent):
    print(f"{event.user.uniqueId} joined the stream!")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} followed the streamer!")

@client.on("share")
async def on_share(event: ShareEvent):
    print(f"{event.user.uniqueId} shared the streamer!")

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.uniqueId} liked the stream!")

@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.nickname} dropped a comment")

@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.repeat_end == 1:
        print(f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")

    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")

if __name__ == "__main__":

    client.run()