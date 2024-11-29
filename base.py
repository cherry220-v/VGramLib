from typing import List, Optional, Union



class User:
    def __init__(self, id: int, is_bot: bool, first_name: str, last_name: Optional[str] = None, 
                 username: Optional[str] = None, language_code: Optional[str] = None, 
                 is_premium: Optional[bool] = False, added_to_attachment_menu: Optional[bool] = False,
                 can_join_groups: Optional[bool] = False, can_read_all_group_messages: Optional[bool] = False,
                 supports_inline_queries: Optional[bool] = False, can_connect_to_business: Optional[bool] = False,
                 has_main_web_app: Optional[bool] = False):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business
        self.has_main_web_app = has_main_web_app

class Location:
    def __init__(self, latitude: float, longitude: float, 
                 horizontalAccuracy: Optional[float] = None, 
                 livePeriod: Optional[int] = None, 
                 heading: Optional[int] = None, 
                 proximityAlertRadius: Optional[int] = None):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontalAccuracy = horizontalAccuracy
        self.livePeriod = livePeriod
        self.heading = heading
        self.proximityAlertRadius = proximityAlertRadius

class Contact:
    def __init__(self, phoneNumber: str, firstName: str, 
                 lastName: Optional[str] = None, userId: Optional[int] = None):
        self.phoneNumber = phoneNumber
        self.firstName = firstName
        self.lastName = lastName
        self.userId = userId

class ReactionType:
    def __init__(self, type: str):
        self.type = type

class ReactionTypeEmoji(ReactionType):
    def __init__(self, emoji: str):
        super().__init__(type="emoji")
        self.emoji = emoji

class ReactionTypeCustomEmoji(ReactionType):
    def __init__(self, custom_emoji_id: str):
        super().__init__(type="custom_emoji")
        self.custom_emoji_id = custom_emoji_id

class ReactionTypePaid(ReactionType):
    def __init__(self):
        super().__init__(type="paid")

class ReactionCount:
    def __init__(self, reaction: ReactionType, total_count: int):
        self.reaction = reaction
        self.total_count = total_count

class PhotoSize:
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

class Animation:
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int,
                 thumbnail: Optional[PhotoSize] = None, file_name: Optional[str] = None,
                 mime_type: Optional[str] = None, file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

class Audio:
    def __init__(self, file_id: str, file_unique_id: str, duration: int, performer: Optional[str] = None,
                 title: Optional[str] = None, file_name: Optional[str] = None, mime_type: Optional[str] = None,
                 file_size: Optional[int] = None, thumbnail: Optional[PhotoSize] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail

class Document:
    def __init__(self, file_id: str, file_unique_id: str, thumbnail: Optional[PhotoSize] = None,
                 file_name: Optional[str] = None, mime_type: Optional[str] = None,
                 file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

class Story:
    def __init__(self, chat: 'Chat', id: int):
        self.chat = chat
        self.id = id

class Video:
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int,
                 thumbnail: Optional[PhotoSize] = None, file_name: Optional[str] = None,
                 mime_type: Optional[str] = None, file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

class VideoNote:
    def __init__(self, file_id: str, file_unique_id: str, length: int, duration: int, thumbnail: Optional[PhotoSize] = None,
                 file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size

class Voice:
    def __init__(self, file_id: str, file_unique_id: str, duration: int, mime_type: Optional[str] = None,
                 file_size: Optional[int] = None):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

class PaidMediaInfo:
    def __init__(self, star_count: int, paid_media: List['PaidMedia']):
        self.star_count = star_count
        self.paid_media = paid_media

class PaidMedia:
    def __init__(self, type: str):
        self.type = type

class PaidMediaPreview(PaidMedia):
    def __init__(self, type: str = "preview", width: Optional[int] = None, height: Optional[int] = None,
                 duration: Optional[int] = None):
        super().__init__(type)
        self.width = width
        self.height = height
        self.duration = duration

class PaidMediaPhoto(PaidMedia):
    def __init__(self, type: str = "photo", photo: List[PhotoSize] = None):
        super().__init__(type)
        self.photo = photo

class PaidMediaVideo(PaidMedia):
    def __init__(self, type: str = "video", video: Video = None):
        super().__init__(type)
        self.video = video

class Contact:
    def __init__(self, phone_number: str, first_name: str, last_name: Optional[str] = None,
                 user_id: Optional[int] = None, vcard: Optional[str] = None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

class Dice:
    def __init__(self, emoji: str, value: int):
        self.emoji = emoji
        self.value = value

class PollOption:
    def __init__(self, text: str, text_entities: Optional[List['MessageEntity']] = None, voter_count: int = 0):
        self.text = text
        self.text_entities = text_entities
        self.voter_count = voter_count

class InputPollOption:
    def __init__(self, text: str, text_parse_mode: Optional[str] = None,
                 text_entities: Optional[List['MessageEntity']] = None):
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities

class PollAnswer:
    def __init__(self, poll_id: str, voter_chat: Optional['Chat'] = None, user: Optional['User'] = None,
                 option_ids: List[int] = []):
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids

class Poll:
    def __init__(self, id: str, question: str, question_entities: Optional[List['MessageEntity']] = None,
                 options: List[PollOption] = None, total_voter_count: int = 0, is_closed: bool = False, 
                 is_anonymous: bool = False, type: str = "regular", allows_multiple_answers: bool = False,
                 correct_option_id: Optional[int] = None, explanation: Optional[str] = None,
                 explanation_entities: Optional[List['MessageEntity']] = None, open_period: Optional[int] = None,
                 close_date: Optional[int] = None):
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date

class PollOption:
    def __init__(self, text: str, voter_count: int = 0, text_entities: Optional[List['MessageEntity']] = None):
        self.text = text
        self.voter_count = voter_count
        self.text_entities = text_entities

class Chat:
    def __init__(self, id: int, type: str, title: Optional[str] = None, username: Optional[str] = None,
                 first_name: Optional[str] = None, last_name: Optional[str] = None, 
                 is_forum: Optional[bool] = False):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum

class ChatFullInfo:
    def __init__(self, id: int, type: str, title: Optional[str] = None, username: Optional[str] = None,
                 first_name: Optional[str] = None, last_name: Optional[str] = None, 
                 is_forum: Optional[bool] = False, accent_color_id: Optional[int] = None, 
                 max_reaction_count: Optional[int] = None, photo: Optional['ChatPhoto'] = None,
                 active_usernames: Optional[List[str]] = None, birthdate: Optional['Birthdate'] = None, 
                 business_intro: Optional['BusinessIntro'] = None, business_location: Optional['BusinessLocation'] = None, 
                 business_opening_hours: Optional['BusinessOpeningHours'] = None, personal_chat: Optional['Chat'] = None,
                 available_reactions: Optional[List['ReactionType']] = None, 
                 background_custom_emoji_id: Optional[str] = None, profile_accent_color_id: Optional[int] = None, 
                 profile_background_custom_emoji_id: Optional[str] = None, 
                 emoji_status_custom_emoji_id: Optional[str] = None, emoji_status_expiration_date: Optional[int] = None,
                 bio: Optional[str] = None, has_private_forwards: Optional[bool] = False,
                 has_restricted_voice_and_video_messages: Optional[bool] = False, 
                 join_to_send_messages: Optional[bool] = False, join_by_request: Optional[bool] = False,
                 description: Optional[str] = None, invite_link: Optional[str] = None, 
                 pinned_message: Optional['Message'] = None, permissions: Optional['ChatPermissions'] = None,
                 can_send_paid_media: Optional[bool] = False, slow_mode_delay: Optional[int] = None,
                 unrestrict_boost_count: Optional[int] = None, message_auto_delete_time: Optional[int] = None, 
                 has_aggressive_anti_spam_enabled: Optional[bool] = False, has_hidden_members: Optional[bool] = False,
                 has_protected_content: Optional[bool] = False, has_visible_history: Optional[bool] = False,
                 sticker_set_name: Optional[str] = None, can_set_sticker_set: Optional[bool] = False,
                 custom_emoji_sticker_set_name: Optional[str] = None, linked_chat_id: Optional[int] = None,
                 location: Optional['ChatLocation'] = None):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames or []
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions or []
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location

class ChatPhoto:
    def __init__(self, small_file_id: str, small_file_unique_id: str, big_file_id: str, big_file_unique_id: str):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

class ChatInviteLink:
    def __init__(self, invite_link: str, creator: User, creates_join_request: bool, is_primary: bool, is_revoked: bool,
                 name: Optional[str] = None, expire_date: Optional[int] = None, member_limit: Optional[int] = None,
                 pending_join_request_count: Optional[int] = None, subscription_period: Optional[int] = None, 
                 subscription_price: Optional[int] = None):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count
        self.subscription_period = subscription_period
        self.subscription_price = subscription_price

class ChatAdministratorRights:
    def __init__(self, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool,
                 can_restrict_members: bool, can_promote_members: bool, can_change_info: bool, can_invite_users: bool,
                 can_post_stories: bool, can_edit_stories: bool, can_delete_stories: bool, can_post_messages: Optional[bool] = None,
                 can_edit_messages: Optional[bool] = None, can_pin_messages: Optional[bool] = None,
                 can_manage_topics: Optional[bool] = None):
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics

class ChatMemberUpdated:
    def __init__(self, chat: Chat, from_user: User, date: int, old_chat_member: 'ChatMember', new_chat_member: 'ChatMember',
                 invite_link: Optional[ChatInviteLink] = None, via_join_request: Optional[bool] = None,
                 via_chat_folder_invite_link: Optional[bool] = None):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link

class ChatMember:
    def __init__(self, user: User, status: str):
        self.user = user
        self.status = status

class ChatMemberOwner(ChatMember):
    def __init__(self, user: User, is_anonymous: bool, custom_title: Optional[str] = None):
        super().__init__(user, status='creator')
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

class ChatMemberAdministrator(ChatMember):
    def __init__(self, user: User, can_be_edited: bool, is_anonymous: bool, can_manage_chat: bool,
                 can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool,
                 can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_stories: bool,
                 can_edit_stories: bool, can_delete_stories: bool, can_post_messages: Optional[bool] = None,
                 can_edit_messages: Optional[bool] = None, can_pin_messages: Optional[bool] = None,
                 can_manage_topics: Optional[bool] = None, custom_title: Optional[str] = None):
        super().__init__(user, status='administrator')
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.custom_title = custom_title

class ChatMemberMember(ChatMember):
    def __init__(self, user: User, until_date: Optional[int] = None):
        super().__init__(user, status='member')
        self.until_date = until_date

class ChatMemberRestricted(ChatMember):
    def __init__(self, user: User, is_member: bool, can_send_messages: bool, can_send_audios: bool,
                 can_send_documents: bool, can_send_photos: bool, can_send_videos: bool, can_send_video_notes: bool,
                 can_send_voice_notes: bool, can_send_polls: bool, can_send_other_messages: bool,
                 can_add_web_page_previews: bool, can_change_info: bool, can_invite_users: bool,
                 can_pin_messages: bool, can_manage_topics: bool, until_date: int):
        super().__init__(user, status='restricted')
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date

class ChatMemberLeft(ChatMember):
    def __init__(self, user: User):
        super().__init__(user, status='left')

class ChatMemberBanned(ChatMember):
    def __init__(self, user: User, until_date: int):
        super().__init__(user, status='kicked')
        self.until_date = until_date

class ChatJoinRequest:
    def __init__(self, chat: Chat, from_user: User, user_chat_id: int, date: int, bio: Optional[str] = None,
                 invite_link: Optional[ChatInviteLink] = None):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

class ChatPermissions:
    def __init__(self, can_send_messages: Optional[bool] = None, can_send_audios: Optional[bool] = None,
                 can_send_documents: Optional[bool] = None, can_send_photos: Optional[bool] = None,
                 can_send_videos: Optional[bool] = None, can_send_video_notes: Optional[bool] = None,
                 can_send_voice_notes: Optional[bool] = None, can_send_polls: Optional[bool] = None,
                 can_send_other_messages: Optional[bool] = None, can_add_web_page_previews: Optional[bool] = None,
                 can_change_info: Optional[bool] = None, can_invite_users: Optional[bool] = None,
                 can_pin_messages: Optional[bool] = None, can_manage_topics: Optional[bool] = None):
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics

class ChatBoostSource:
    def __init__(self, source: str, user: User):
        self.source = source
        self.user = user

class ChatBoostSourcePremium(ChatBoostSource):
    def __init__(self, user: User):
        super().__init__(source="premium", user=user)

class ChatBoostSourceGiftCode(ChatBoostSource):
    def __init__(self, user: User):
        super().__init__(source="gift_code", user=user)

class ChatBoostSourceGiveaway(ChatBoostSource):
    def __init__(self, user: Optional[User], giveaway_message_id: int, prize_star_count: Optional[int], is_unclaimed: Optional[bool] = None):
        super().__init__(source="giveaway", user=user)
        self.giveaway_message_id = giveaway_message_id
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed

class ChatBoost:
    def __init__(self, boost_id: str, add_date: int, expiration_date: int, source: ChatBoostSource):
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source

class ChatBoostUpdated:
    def __init__(self, chat: Chat, boost: ChatBoost):
        self.chat = chat
        self.boost = boost

class ChatBoostRemoved:
    def __init__(self, chat: Chat, boost_id: str, remove_date: int, source: ChatBoostSource):
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source

class UserChatBoosts:
    def __init__(self, boosts: List[ChatBoost]):
        self.boosts = boosts

class ChatShared:
    def __init__(self, request_id: int, chat_id: int, title: Optional[str] = None, 
                 username: Optional[str] = None, photo: Optional[List[PhotoSize]] = None):
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo if photo is not None else []

class ChatBackground:
    def __init__(self, type: str):
        self.type = type

class ChatBoostAdded:
    def __init__(self, boost_count: int):
        self.boost_count = boost_count

class ChatLocation:
    def __init__(self, location: Location, address: str):
        self.location = location
        self.address = address

class Message:
    def __init__(self, 
                 id: int, 
                 date: int, 
                 chat: 'Chat', 
                 sender: Optional['User'] = None, 
                 senderChat: Optional['Chat'] = None,
                 senderBoostCount: Optional[int] = None, 
                 senderBusinessBot: Optional['User'] = None, 
                 threadId: Optional[int] = None,
                 businessConnectionId: Optional[str] = None,
                 forwardOrigin: Optional['MessageOrigin'] = None,
                 isTopicMessage: Optional[bool] = None,
                 isAutomaticForward: Optional[bool] = None,
                 replyToMessage: Optional['Message'] = None,
                 externalReply: Optional['ExternalReplyInfo'] = None,
                 quote: Optional['TextQuote'] = None,
                 replyToStory: Optional['Story'] = None,
                 viaBot: Optional['User'] = None,
                 editDate: Optional[int] = None,
                 hasProtectedContent: Optional[bool] = None,
                 isFromOffline: Optional[bool] = None,
                 mediaGroupId: Optional[str] = None,
                 authorSignature: Optional[str] = None,
                 text: Optional[str] = None,
                 entities: Optional[List['MessageEntity']] = None,
                 linkPreviewOptions: Optional['LinkPreviewOptions'] = None,
                 effectId: Optional[str] = None,
                 animation: Optional['Animation'] = None,
                 audio: Optional['Audio'] = None,
                 document: Optional['Document'] = None,
                 paidMedia: Optional['PaidMediaInfo'] = None,
                 photo: Optional[List['PhotoSize']] = None,
                 sticker: Optional['Sticker'] = None,
                 story: Optional['Story'] = None,
                 video: Optional['Video'] = None,
                 videoNote: Optional['VideoNote'] = None,
                 voice: Optional['Voice'] = None,
                 caption: Optional[str] = None,
                 captionEntities: Optional[List['MessageEntity']] = None,
                 showCaptionAboveMedia: Optional[bool] = None,
                 hasMediaSpoiler: Optional[bool] = None,
                 contact: Optional['Contact'] = None,
                 dice: Optional['Dice'] = None,
                 game: Optional['Game'] = None,
                 poll: Optional['Poll'] = None,
                 venue: Optional['Venue'] = None,
                 location: Optional['Location'] = None,
                 newChatMembers: Optional[List['User']] = None,
                 leftChatMember: Optional['User'] = None,
                 newChatTitle: Optional[str] = None,
                 newChatPhoto: Optional[List['PhotoSize']] = None,
                 deleteChatPhoto: Optional[bool] = None,
                 groupChatCreated: Optional[bool] = None,
                 supergroupChatCreated: Optional[bool] = None,
                 channelChatCreated: Optional[bool] = None,
                 messageAutoDeleteTimerChanged: Optional['MessageAutoDeleteTimerChanged'] = None,
                 migrateToChatId: Optional[int] = None,
                 migrateFromChatId: Optional[int] = None,
                 pinnedMessage: Optional['MaybeInaccessibleMessage'] = None,
                 invoice: Optional['Invoice'] = None,
                 successfulPayment: Optional['SuccessfulPayment'] = None,
                 refundedPayment: Optional['RefundedPayment'] = None,
                 usersShared: Optional['UsersShared'] = None,
                 chatShared: Optional['ChatShared'] = None,
                 connectedWebsite: Optional[str] = None,
                 writeAccessAllowed: Optional['WriteAccessAllowed'] = None,
                 passportData: Optional['PassportData'] = None,
                 proximityAlertTriggered: Optional['ProximityAlertTriggered'] = None,
                 boostAdded: Optional['ChatBoostAdded'] = None,
                 chatBackgroundSet: Optional['ChatBackground'] = None,
                 forumTopicCreated: Optional['ForumTopicCreated'] = None,
                 forumTopicEdited: Optional['ForumTopicEdited'] = None,
                 forumTopicClosed: Optional['ForumTopicClosed'] = None,
                 forumTopicReopened: Optional['ForumTopicReopened'] = None,
                 generalForumTopicHidden: Optional['GeneralForumTopicHidden'] = None,
                 generalForumTopicUnhidden: Optional['GeneralForumTopicUnhidden'] = None,
                 giveawayCreated: Optional['GiveawayCreated'] = None,
                 giveaway: Optional['Giveaway'] = None,
                 giveawayWinners: Optional['GiveawayWinners'] = None,
                 giveawayCompleted: Optional['GiveawayCompleted'] = None,
                 videoChatScheduled: Optional['VideoChatScheduled'] = None,
                 videoChatStarted: Optional['VideoChatStarted'] = None,
                 videoChatEnded: Optional['VideoChatEnded'] = None,
                 videoChatParticipantsInvited: Optional['VideoChatParticipantsInvited'] = None,
                 webAppData: Optional['WebAppData'] = None,
                 replyMarkup: Optional['InlineKeyboardMarkup'] = None):
        self.id = id
        self.threadId = threadId
        self.sender = sender
        self.senderChat = senderChat
        self.senderBoostCount = senderBoostCount
        self.senderBusinessBot = senderBusinessBot
        self.date = date
        self.businessConnectionId = businessConnectionId
        self.chat = chat
        self.forwardOrigin = forwardOrigin
        self.isTopicMessage = isTopicMessage
        self.isAutomaticForward = isAutomaticForward
        self.replyToMessage = replyToMessage
        self.externalReply = externalReply
        self.quote = quote
        self.replyToStory = replyToStory
        self.viaBot = viaBot
        self.editDate = editDate
        self.hasProtectedContent = hasProtectedContent
        self.isFromOffline = isFromOffline
        self.mediaGroupId = mediaGroupId
        self.authorSignature = authorSignature
        self.text = text
        self.entities = entities
        self.linkPreviewOptions = linkPreviewOptions
        self.effectId = effectId
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paidMedia = paidMedia
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.videoNote = videoNote
        self.voice = voice
        self.caption = caption
        self.captionEntities = captionEntities
        self.showCaptionAboveMedia = showCaptionAboveMedia
        self.hasMediaSpoiler = hasMediaSpoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.newChatMembers = newChatMembers
        self.leftChatMember = leftChatMember
        self.newChatTitle = newChatTitle
        self.newChatPhoto = newChatPhoto
        self.deleteChatPhoto = deleteChatPhoto
        self.groupChatCreated = groupChatCreated
        self.supergroupChatCreated = supergroupChatCreated
        self.channelChatCreated = channelChatCreated
        self.messageAutoDeleteTimerChanged = messageAutoDeleteTimerChanged
        self.migrateToChatId = migrateToChatId
        self.migrateFromChatId = migrateFromChatId
        self.pinnedMessage = pinnedMessage
        self.invoice = invoice
        self.successfulPayment = successfulPayment
        self.refundedPayment = refundedPayment
        self.usersShared = usersShared
        self.chatShared = chatShared
        self.connectedWebsite = connectedWebsite
        self.writeAccessAllowed = writeAccessAllowed
        self.passportData = passportData
        self.proximityAlertTriggered = proximityAlertTriggered
        self.boostAdded = boostAdded
        self.chatBackgroundSet = chatBackgroundSet
        self.forumTopicCreated = forumTopicCreated
        self.forumTopicEdited = forumTopicEdited
        self.forumTopicClosed = forumTopicClosed
        self.forumTopicReopened = forumTopicReopened
        self.generalForumTopicHidden = generalForumTopicHidden
        self.generalForumTopicUnhidden = generalForumTopicUnhidden
        self.giveawayCreated = giveawayCreated
        self.giveaway = giveaway
        self.giveawayWinners = giveawayWinners
        self.giveawayCompleted = giveawayCompleted
        self.videoChatScheduled = videoChatScheduled
        self.videoChatStarted = videoChatStarted
        self.videoChatEnded = videoChatEnded
        self.videoChatParticipantsInvited = videoChatParticipantsInvited
        self.webAppData = webAppData
        self.replyMarkup = replyMarkup

class MessageEntity:
    def __init__(self, type: str, offset: int, length: int, 
                 url: Optional[str] = None, user: Optional[User] = None, 
                 language: Optional[str] = None, custom_emoji_id: Optional[str] = None):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id

class TextQuote:
    def __init__(self, text: str, entities: Optional[List[MessageEntity]] = None, 
                 position: int = 0, is_manual: Optional[bool] = False):
        self.text = text
        self.entities = entities or []
        self.position = position
        self.is_manual = is_manual

class ExternalReplyInfo:
    def __init__(self, origin: 'MessageOrigin', chat: Optional['Chat'] = None, 
                 message_id: Optional[int] = None, link_preview_options: Optional['LinkPreviewOptions'] = None, 
                 animation: Optional['Animation'] = None, audio: Optional['Audio'] = None, 
                 document: Optional['Document'] = None, photo: Optional[List['PhotoSize']] = None, 
                 sticker: Optional['Sticker'] = None, story: Optional['Story'] = None, 
                 video: Optional['Video'] = None, video_note: Optional['VideoNote'] = None, 
                 voice: Optional['Voice'] = None, has_media_spoiler: Optional[bool] = False, 
                 contact: Optional['Contact'] = None, dice: Optional['Dice'] = None, 
                 game: Optional['Game'] = None, giveaway: Optional['Giveaway'] = None, 
                 giveaway_winners: Optional['GiveawayWinners'] = None, invoice: Optional['Invoice'] = None, 
                 location: Optional['Location'] = None, poll: Optional['Poll'] = None, 
                 venue: Optional['Venue'] = None):
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue

class ReplyParameters:
    def __init__(self, message_id: int, chat_id: Optional[Union[int, str]] = None, 
                 allow_sending_without_reply: bool = False, quote: Optional[str] = None, 
                 quote_parse_mode: Optional[str] = None, quote_entities: Optional[List[MessageEntity]] = None, 
                 quote_position: Optional[int] = None):
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities or []
        self.quote_position = quote_position

class MessageOrigin:
    def __init__(self, type: str, date: int, sender_user: Optional['User'] = None, 
                 sender_user_name: Optional[str] = None, sender_chat: Optional['Chat'] = None, 
                 author_signature: Optional[str] = None):
        self.type = type
        self.date = date
        self.sender_user = sender_user
        self.sender_user_name = sender_user_name
        self.sender_chat = sender_chat
        self.author_signature = author_signature

class MessageOriginUser(MessageOrigin):
    def __init__(self, date: int, sender_user: 'User'):
        super().__init__(type='user', date=date, sender_user=sender_user)

class MessageOriginHiddenUser(MessageOrigin):
    def __init__(self, date: int, sender_user_name: str):
        super().__init__(type='hidden_user', date=date, sender_user_name=sender_user_name)

class MessageOriginChat(MessageOrigin):
    def __init__(self, date: int, sender_chat: 'Chat', author_signature: Optional[str] = None):
        super().__init__(type='chat', date=date, sender_chat=sender_chat, author_signature=author_signature)

class MessageOriginChannel(MessageOrigin):
    def __init__(self, date: int, chat: 'Chat', message_id: int, author_signature: Optional[str] = None):
        super().__init__(type='channel', date=date, sender_chat=chat, author_signature=author_signature)
        self.message_id = message_id

class MessageAutoDeleteTimerChanged:
    def __init__(self, message_auto_delete_time: int):
        self.message_auto_delete_time = message_auto_delete_time

class MessageReactionUpdated:
    def __init__(self, chat: Chat, message_id: int, date: int, 
                 old_reaction: List[ReactionType] = None, new_reaction: List[ReactionType] = None, 
                 user: Optional[User] = None, actor_chat: Optional[Chat] = None):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction
        self.user = user
        self.actor_chat = actor_chat

class MessageReactionCountUpdated:
    def __init__(self, chat: Chat, message_id: int, date: int, reactions: List[ReactionCount]):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions