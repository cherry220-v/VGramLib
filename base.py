from typing import List, Optional, Union
import json

class JsonAPI:
    def __init__(self):
        self.data = {}

    def setData(self, key, value):
        self.data[key] = value

    def json(self):
        return json.dumps({key: getattr(self, key, None) for key in self.valid})

    @classmethod
    def obj(cls, subclass, data):
        instance = subclass()
        for key, value in data.items():
            if key in instance.valid:
                setattr(instance, instance.valid.get(key), value)
        return instance

class User(JsonAPI):
    def __init__(self):
        self.id = id
        self.isBot = None
        self.firstName = None
        self.lastName = None
        self.username = None
        self.languageCode = None
        self.isPremium = None
        self.addedToAttachmentMenu = None
        self.canJoinGroups = None
        self.canReadAllGroupMessages = None
        self.supportsInlineQueries = None
        self.canConnectToBusiness = None
        self.hasMainWebApp = None

        self.valid = {
            "id": "id",
            "is_bot": "isBot",
            "first_name": "firstName",
            "last_name": "lastName",
            "username": "username",
            "language_code": "languageCode",
            "is_premium": "isPremium",
            "added_to_attachment_menu": "addedToAttachmentMenu",
            "can_join_groups": "canJoinGroups",
            "can_read_all_group_messages": "canReadAllGroupMessages",
            "supports_inline_quieries": "supportsInlineQueries",
            "can_connect_to_business": "canConnectToBusiness",
            "has_main_web_app": "hasMainWebApp"
        }

class Location(JsonAPI):
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.horizontalAccuracy = None
        self.livePeriod = None
        self.heading = None
        self.proximityAlertRadius = None

        self.valid = {
            "latitude": "latitude",
            "longitude": "longitude",
            "horizontal_accuracy": "hotizontalAccuracy",
            "live_period": "livePeriod",
            "heading": "heading",
            "proximity_alert_radius": "proximityAlertRadius"
        }

class Contact(JsonAPI):
    def __init__(self):
        self.phoneNumber = None
        self.firstName = None
        self.lastName = None
        self.userId = None
        self.vcard = None

        self.valid = {
            "phone_number": "phoneNumber",
            "first_name": "firstName",
            "last_name": "lastName",
            "user_id": "userId",
            "vcard": "vcard"
        }

class ReactionType(JsonAPI):
    def __init__(self):
        self.valid = {}

class ReactionTypeEmoji(ReactionType):
    def __init__(self):
        super().__init__()
        self.emoji = None
        self.valid = {"emoji": "emoji"}

class ReactionTypeCustomEmoji(ReactionType):
    def __init__(self):
        super().__init__()
        self.customEmojiId = None
        self.valid = {"custom_emoji_id": "customEmojiId"}

class ReactionCount(JsonAPI):
    def __init__(self):
        self.type = None  # Instance of ReactionType
        self.count = None

        self.valid = {
            "type": "type",
            "count": "count"
        }

class PhotoSize(JsonAPI):
    def __init__(self):
        self.type = None
        self.fileId = None
        self.fileUniqueId = None
        self.width = None
        self.height = None
        self.fileSize = None

        self.valid = {
            "type": "type",
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "width": "width",
            "height": "height",
            "file_size": "fileSize"
        }

class Animation(JsonAPI):
    def __init__(self):
        self.fileId = None
        self.fileUniqueId = None
        self.width = None
        self.height = None
        self.duration = None
        self.thumbnail = None  # Instance of PhotoSize
        self.fileName = None
        self.mimeType = None
        self.fileSize = None

        self.valid = {
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "width": "width",
            "height": "height",
            "duration": "duration",
            "thumbnail": "thumbnail",
            "file_name": "fileName",
            "mime_type": "mimeType",
            "file_size": "fileSize"
        }

class Audio(JsonAPI):
    def __init__(self):
        self.fileId = None
        self.fileUniqueId = None
        self.duration = None
        self.performer = None
        self.title = None
        self.fileName = None
        self.mimeType = None
        self.fileSize = None
        self.thumbnail = None  # Instance of PhotoSize

        self.valid = {
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "duration": "duration",
            "performer": "performer",
            "title": "title",
            "file_name": "fileName",
            "mime_type": "mimeType",
            "file_size": "fileSize",
            "thumbnail": "thumbnail"
        }

class Document(JsonAPI):
    def __init__(self):
        self.fileId = None
        self.fileUniqueId = None
        self.thumbnail = None  # Instance of PhotoSize
        self.fileName = None
        self.mimeType = None
        self.fileSize = None

        self.valid = {
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "thumbnail": "thumbnail",
            "file_name": "fileName",
            "mime_type": "mimeType",
            "file_size": "fileSize"
        }

class Video(JsonAPI):
    def __init__(self):
        self.fileId = None
        self.fileUniqueId = None
        self.width = None
        self.height = None
        self.duration = None
        self.thumbnail = None  # Instance of PhotoSize
        self.fileName = None
        self.mimeType = None
        self.fileSize = None

        self.valid = {
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "width": "width",
            "height": "height",
            "duration": "duration",
            "thumbnail": "thumbnail",
            "file_name": "fileName",
            "mime_type": "mimeType",
            "file_size": "fileSize"
        }

class Voice(JsonAPI):
    def __init__(self):
        self.fileId = None
        self.fileUniqueId = None
        self.duration = None
        self.mimeType = None
        self.fileSize = None

        self.valid = {
            "file_id": "fileId",
            "file_unique_id": "fileUniqueId",
            "duration": "duration",
            "mime_type": "mimeType",
            "file_size": "fileSize"
        }

class PaidMediaInfo(JsonAPI):
    def __init__(self):
        self.starCount = None
        self.paidMedia = []  # List of PaidMedia instances

        self.valid = {
            "star_count": "starCount",
            "paid_media": "paidMedia"
        }

class PaidMedia(JsonAPI):
    def __init__(self):
        self.type = None

        self.valid = {
            "type": "type"
        }

class PaidMediaPreview(PaidMedia):
    def __init__(self):
        super().__init__()
        self.width = None
        self.height = None
        self.duration = None

        self.valid.update({
            "width": "width",
            "height": "height",
            "duration": "duration"
        })

class PaidMediaPhoto(PaidMedia):
    def __init__(self):
        super().__init__()
        self.photo = []  # List of PhotoSize instances

        self.valid.update({
            "photo": "photo"
        })

class PaidMediaVideo(PaidMedia):
    def __init__(self):
        super().__init__()
        self.video = None  # Instance of Video

        self.valid.update({
            "video": "video"
        })

class Dice(JsonAPI):
    def __init__(self):
        self.emoji = None
        self.value = None

        self.valid = {
            "emoji": "emoji",
            "value": "value"
        }

class PollOption(JsonAPI):
    def __init__(self):
        self.text = None
        self.textEntities = []  # List of MessageEntity instances
        self.voterCount = None

        self.valid = {
            "text": "text",
            "text_entities": "textEntities",
            "voter_count": "voterCount"
        }

class InputPollOption(JsonAPI):
    def __init__(self):
        self.text = None
        self.textParseMode = None
        self.textEntities = []  # List of MessageEntity instances

        self.valid = {
            "text": "text",
            "text_parse_mode": "textParseMode",
            "text_entities": "textEntities"
        }

class PollAnswer(JsonAPI):
    def __init__(self):
        self.pollId = None
        self.voterChat = None  # Instance of Chat
        self.user = None  # Instance of User
        self.optionIds = []

        self.valid = {
            "poll_id": "pollId",
            "voter_chat": "voterChat",
            "user": "user",
            "option_ids": "optionIds"
        }

class Poll(JsonAPI):
    def __init__(self):
        self.id = None
        self.question = None
        self.questionEntities = []  # List of MessageEntity instances
        self.options = []  # List of PollOption instances
        self.totalVoterCount = None
        self.isClosed = None
        self.isAnonymous = None
        self.type = None
        self.allowsMultipleAnswers = None
        self.correctOptionId = None
        self.explanation = None
        self.explanationEntities = []  # List of MessageEntity instances
        self.openPeriod = None
        self.close_date = None

        self.valid = {
            "id": "id",
            "question": "question",
            "question_entities": "questionEntities",
            "options": "options",
            "total_voter_count": "totalVoterCount",
            "is_closed": "isClosed",
            "is_anonymous": "isAnonymous",
            "type": "type",
            "allows_multiple_answers": "allowsMultipleAnswers",
            "correct_option_id": "correctOptionId",
            "explanation": "explanation",
            "explanation_entities": "explanationEntities",
            "open_period": "openPeriod",
            "close_date": "close_date"
        }

class Chat(JsonAPI):
    def __init__(self):
        self.id = None
        self.type = None
        self.title = None
        self.username = None
        self.firstName = None
        self.lastName = None
        self.isForum = None

        self.valid = {
            "id": "id",
            "type": "type",
            "title": "title",
            "username": "username",
            "first_name": "firstName",
            "last_name": "lastName",
            "is_forum": "isForum"
        }

class ChatFullInfo(JsonAPI):
    def __init__(self):
        super().__init__()

        self.id = None
        self.type = None
        self.title = None
        self.username = None
        self.firstName = None
        self.lastName = None
        self.isForum = None
        self.accentColorId = None
        self.maxReactionCount = None
        self.photo = None
        self.activeUsernames = []
        self.birthdate = None
        self.businessIntro = None
        self.businessLocation = None
        self.businessOpeningHours = None
        self.personalChat = None
        self.availableReactions = []
        self.backgroundCustomEmojiId = None
        self.profileAccentColorId = None
        self.profileBackgroundCustomEmojiId = None
        self.emojiStatusCustomEmojiId = None
        self.emojiStatusExpiration_date = None
        self.bio = None
        self.hasPrivateForwards = None
        self.hasRestrictedVoiceAndVideoMessages = None
        self.joinToSendMessages = None
        self.joinByRequest = None
        self.description = None
        self.inviteLink = None
        self.pinnedMessage = None
        self.permissions = None
        self.canSendPaidMedia = None
        self.slowMode_delay = None
        self.unrestrictBoostCount = None
        self.messageAuto_deleteTime = None
        self.hasAggressiveAntiSpamEnabled = None
        self.hasHiddenMembers = None
        self.hasProtectedContent = None
        self.hasVisibleHistory = None
        self.stickerSetName = None
        self.canSetStickerSet = None
        self.customEmojiStickerSetName = None
        self.linkedChatId = None
        self.location = None

        # Define the valid attribute mapping
        self.valid = {
            "id": "id",
            "type": "type",
            "title": "title",
            "username": "username",
            "first_name": "firstName",
            "last_name": "lastName",
            "is_forum": "isForum",
            "accent_color_id": "accentColorId",
            "max_reaction_count": "maxReactionCount",
            "photo": "photo",
            "active_usernames": "activeUsernames",
            "birthdate": "birthdate",
            "business_intro": "businessIntro",
            "business_location": "businessLocation",
            "business_opening_hours": "businessOpeningHours",
            "personal_chat": "personalChat",
            "available_reactions": "availableReactions",
            "background_custom_emoji_id": "backgroundCustomEmojiId",
            "profile_accent_color_id": "profileAccentColorId",
            "profile_background_custom_emoji_id": "profileBackgroundCustomEmojiId",
            "emoji_status_custom_emoji_id": "emojiStatusCustomEmojiId",
            "emoji_status_expiration_date": "emojiStatusExpiration_date",
            "bio": "bio",
            "has_private_forwards": "hasPrivateForwards",
            "has_restricted_voice_and_video_messages": "hasRestrictedVoiceAndVideoMessages",
            "join_to_send_messages": "joinToSendMessages",
            "join_by_request": "joinByRequest",
            "description": "description",
            "invite_link": "inviteLink",
            "pinned_message": "pinnedMessage",
            "permissions": "permissions",
            "can_send_paid_media": "canSendPaidMedia",
            "slow_mode_delay": "slowMode_delay",
            "unrestrict_boost_count": "unrestrictBoostCount",
            "message_auto_delete_time": "messageAuto_deleteTime",
            "has_aggressive_anti_spam_enabled": "hasAggressiveAntiSpamEnabled",
            "has_hidden_members": "hasHiddenMembers",
            "has_protected_content": "hasProtectedContent",
            "has_visible_history": "hasVisibleHistory",
            "sticker_set_name": "stickerSetName",
            "can_set_sticker_set": "canSetStickerSet",
            "custom_emoji_sticker_set_name": "customEmojiStickerSetName",
            "linked_chat_id": "linkedChatId",
            "location": "location"
        }

class ChatPhoto(JsonAPI):
    def __init__(self):
        self.smallFileId = None
        self.smallFileUniqueId = None
        self.bigFileId = None
        self.bigFileUniqueId = None

        self.valid = {
            "small_file_id": "smallFileId",
            "small_file_unique_id": "smallFileUniqueId",
            "big_file_id": "bigFileId",
            "big_file_unique_id": "bigFileUniqueId"
        }

class ChatInviteLink(JsonAPI):
    def __init__(self):
        self.inviteLink = None
        self.creator = None  # User instance
        self.createsJoinRequest = None
        self.isPrimary = None
        self.isRevoked = None
        self.name = None
        self.expire_date = None
        self.memberLimit = None
        self.pendingJoinRequestCount = None
        self.subscriptionPeriod = None
        self.subscriptionPrice = None

        self.valid = {
            "invite_link": "inviteLink",
            "creator": "creator",
            "creates_join_request": "createsJoinRequest",
            "is_primary": "isPrimary",
            "is_revoked": "isRevoked",
            "name": "name",
            "expire_date": "expire_date",
            "member_limit": "memberLimit",
            "pending_join_request_count": "pendingJoinRequestCount",
            "subscription_period": "subscriptionPeriod",
            "subscription_price": "subscriptionPrice"
        }

class ChatAdministratorRights(JsonAPI):
    def __init__(self):
        self.isAnonymous = None
        self.canManageChat = None
        self.can_deleteMessages = None
        self.canManageVideoChats = None
        self.canRestrictMembers = None
        self.canPromoteMembers = None
        self.canChangeInfo = None
        self.canInviteUsers = None
        self.canPostStories = None
        self.canEditStories = None
        self.can_deleteStories = None
        self.canPostMessages = None
        self.canEditMessages = None
        self.canPinMessages = None
        self.canManageTopics = None

        self.valid = {
            "is_anonymous": "isAnonymous",
            "can_manage_chat": "canManageChat",
            "can_delete_messages": "can_deleteMessages",
            "can_manage_video_chats": "canManageVideoChats",
            "can_restrict_members": "canRestrictMembers",
            "can_promote_members": "canPromoteMembers",
            "can_change_info": "canChangeInfo",
            "can_invite_users": "canInviteUsers",
            "can_post_stories": "canPostStories",
            "can_edit_stories": "canEditStories",
            "can_delete_stories": "can_deleteStories",
            "can_post_messages": "canPostMessages",
            "can_edit_messages": "canEditMessages",
            "can_pin_messages": "canPinMessages",
            "can_manage_topics": "canManageTopics"
        }

class ChatMemberUpdated(JsonAPI):
    def __init__(self):
        self.chat = None  # Chat instance
        self.fromUser = None  # User instance
        self.date = None
        self.oldChatMember = None  # ChatMember instance
        self.newChatMember = None  # ChatMember instance
        self.inviteLink = None  # ChatInviteLink instance
        self.viaJoinRequest = None
        self.viaChatFolderInviteLink = None

        self.valid = {
            "chat": "chat",
            "from_user": "fromUser",
            "date": "date",
            "old_chat_member": "oldChatMember",
            "new_chat_member": "newChatMember",
            "invite_link": "inviteLink",
            "via_join_request": "viaJoinRequest",
            "via_chat_folder_invite_link": "viaChatFolderInviteLink"
        }

class ChatMember(JsonAPI):
    def __init__(self):
        self.user = None  # User instance
        self.status = None

        self.valid = {
            "user": "user",
            "status": "status"
        }

class ChatMemberOwner(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()
        self.isAnonymous = None
        self.customTitle = None

        self.valid = {
            "user": "user",
            "status": "status",
            "is_anonymous": "isAnonymous",
            "custom_title": "customTitle"
        }

class ChatMemberAdministrator(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()
        self.canBeEdited = None
        self.isAnonymous = None
        self.canManageChat = None
        self.can_deleteMessages = None
        self.canManageVideoChats = None
        self.canRestrictMembers = None
        self.canPromoteMembers = None
        self.canChangeInfo = None
        self.canInviteUsers = None
        self.canPostStories = None
        self.canEditStories = None
        self.can_deleteStories = None
        self.canPostMessages = None
        self.canEditMessages = None
        self.canPinMessages = None
        self.canManageTopics = None
        self.customTitle = None

        self.valid = {
            "user": "user",
            "status": "status",
            "can_be_edited": "canBeEdited",
            "is_anonymous": "isAnonymous",
            "can_manage_chat": "canManageChat",
            "can_delete_messages": "can_deleteMessages",
            "can_manage_video_chats": "canManageVideoChats",
            "can_restrict_members": "canRestrictMembers",
            "can_promote_members": "canPromoteMembers",
            "can_change_info": "canChangeInfo",
            "can_invite_users": "canInviteUsers",
            "can_post_stories": "canPostStories",
            "can_edit_stories": "canEditStories",
            "can_delete_stories": "can_deleteStories",
            "can_post_messages": "canPostMessages",
            "can_edit_messages": "canEditMessages",
            "can_pin_messages": "canPinMessages",
            "can_manage_topics": "canManageTopics",
            "custom_title": "customTitle"
        }

class ChatMemberMember(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()
        self.until_date = None

        self.valid = {
            "user": "user",
            "status": "status",
            "until_date": "until_date"
        }

class ChatMemberRestricted(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()
        self.isMember = None
        self.canSendMessages = None
        self.canSendAudios = None
        self.canSend_documents = None
        self.canSendPhotos = None
        self.canSendVideos = None
        self.canSendVideoNotes = None
        self.canSendVoiceNotes = None
        self.canSendPolls = None
        self.canSendOtherMessages = None
        self.canAddWebPagePreviews = None
        self.canChangeInfo = None
        self.canInviteUsers = None
        self.canPinMessages = None
        self.canManageTopics = None
        self.until_date = None

        self.valid = {
            "user": "user",
            "status": "status",
            "is_member": "isMember",
            "can_send_messages": "canSendMessages",
            "can_send_audios": "canSendAudios",
            "can_send_documents": "canSend_documents",
            "can_send_photos": "canSendPhotos",
            "can_send_videos": "canSendVideos",
            "can_send_video_notes": "canSendVideoNotes",
            "can_send_voice_notes": "canSendVoiceNotes",
            "can_send_polls": "canSendPolls",
            "can_send_other_messages": "canSendOtherMessages",
            "can_add_web_page_previews": "canAddWebPagePreviews",
            "can_change_info": "canChangeInfo",
            "can_invite_users": "canInviteUsers",
            "can_pin_messages": "canPinMessages",
            "can_manage_topics": "canManageTopics",
            "until_date": "until_date"
        }

class ChatMemberLeft(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()

        self.valid = {
            "user": "user",
            "status": "status"
        }

class ChatMemberBanned(ChatMember, JsonAPI):
    def __init__(self):
        super().__init__()
        self.until_date = None

        self.valid = {
            "user": "user",
            "status": "status",
            "until_date": "until_date"
        }

class ChatJoinRequest(JsonAPI):
    def __init__(self):
        self.chat = None
        self.fromUser = None
        self.userChatId = None
        self.date = None
        self.bio = None
        self.inviteLink = None
        
        self.valid = {
            "chat": "chat",
            "from_user": "fromUser",
            "user_chat_id": "userChatId",
            "date": "date",
            "bio": "bio",
            "invite_link": "inviteLink"
        }

class ChatPermissions(JsonAPI):
    def __init__(self):
        self.canSendMessages = None
        self.canSendAudios = None
        self.canSend_documents = None
        self.canSendPhotos = None
        self.canSendVideos = None
        self.canSendVideoNotes = None
        self.canSendVoiceNotes = None
        self.canSendPolls = None
        self.canSendOtherMessages = None
        self.canAddWebPagePreviews = None
        self.canChangeInfo = None
        self.canInviteUsers = None
        self.canPinMessages = None
        self.canManageTopics = None
        
        self.valid = {
            "can_send_messages": "canSendMessages",
            "can_send_audios": "canSendAudios",
            "can_send_documents": "canSend_documents",
            "can_send_photos": "canSendPhotos",
            "can_send_videos": "canSendVideos",
            "can_send_video_notes": "canSendVideoNotes",
            "can_send_voice_notes": "canSendVoiceNotes",
            "can_send_polls": "canSendPolls",
            "can_send_other_messages": "canSendOtherMessages",
            "can_add_web_page_previews": "canAddWebPagePreviews",
            "can_change_info": "canChangeInfo",
            "can_invite_users": "canInviteUsers",
            "can_pin_messages": "canPinMessages",
            "can_manage_topics": "canManageTopics"
        }

class ChatBoostSource(JsonAPI):
    def __init__(self):
        self.source = None
        self.user = None
        
        self.valid = {
            "source": "source",
            "user": "user"
        }

class ChatBoostSourcePremium(ChatBoostSource):
    def __init__(self):
        super().__init__()
        self.source = "premium"
        
        self.valid = {
            "source": "source",
            "user": "user"
        }

class ChatBoostSourceGiftCode(ChatBoostSource):
    def __init__(self):
        super().__init__()
        self.source = "giftCode"
        
        self.valid = {
            "source": "source",
            "user": "user"
        }

class ChatBoostSourceGiveaway(ChatBoostSource):
    def __init__(self):
        super().__init__()
        self.source = "giveaway"
        self.giveawayMessageId = None
        self.prizeStarCount = None
        self.isUnclaimed = None
        
        self.valid = {
            "source": "source",
            "user": "user",
            "giveaway_message_id": "giveawayMessageId",
            "prize_star_count": "prizeStarCount",
            "is_unclaimed": "isUnclaimed"
        }

class ChatBoost(JsonAPI):
    def __init__(self):
        self.boostId = None
        self.add_date = None
        self.expiration_date = None
        self.source = None
        
        self.valid = {
            "boost_id": "boostId",
            "add_date": "add_date",
            "expiration_date": "expiration_date",
            "source": "source"
        }

class ChatBoostUpdated(JsonAPI):
    def __init__(self):
        self.chat = None
        self.boost = None
        
        self.valid = {
            "chat": "chat",
            "boost": "boost"
        }

class ChatBoostRemoved(JsonAPI):
    def __init__(self):
        self.chat = None
        self.boostId = None
        self.remove_date = None
        self.source = None
        
        self.valid = {
            "chat": "chat",
            "boost_id": "boostId",
            "remove_date": "remove_date",
            "source": "source"
        }

class UserChatBoosts(JsonAPI):
    def __init__(self):
        self.boosts = []
        
        self.valid = {
            "boosts": "boosts"
        }

class ChatShared(JsonAPI):
    def __init__(self):
        self.requestId = None
        self.chatId = None
        self.title = None
        self.username = None
        self.photo = []
        
        self.valid = {
            "request_id": "requestId",
            "chat_id": "chatId",
            "title": "title",
            "username": "username",
            "photo": "photo"
        }

class ChatBackground(JsonAPI):
    def __init__(self):
        self.type = None
        
        self.valid = {
            "type": "type"
        }

class ChatBoostAdded(JsonAPI):
    def __init__(self):
        self.boostCount = None
        
        self.valid = {
            "boost_count": "boostCount"
        }

class ChatLocation(JsonAPI):
    def __init__(self):
        self.location = None
        self.address = None
        
        self.valid = {
            "location": "location",
            "address": "address"
        }

class Message(JsonAPI):
    def __init__(self):
        self.id = None
        self.date = None
        self.chat = None
        self.sender = None
        self.senderChat = None
        self.senderBoostCount = None
        self.senderBusinessBot = None
        self.threadId = None
        self.businessConnectionId = None
        self.forwardOrigin = None
        self.isTopicMessage = None
        self.isAutomaticForward = None
        self.replyToMessage = None
        self.externalReply = None
        self.quote = None
        self.replyToStory = None
        self.viaBot = None
        self.editDate = None
        self.hasProtectedContent = None
        self.isFromOffline = None
        self.mediaGroupId = None
        self.authorSignature = None
        self.text = None
        self.entities = None
        self.linkPreviewOptions = None
        self.effectId = None
        self.animation = None
        self.audio = None
        self.document = None
        self.paidMedia = None
        self.photo = None
        self.sticker = None
        self.story = None
        self.video = None
        self.videoNote = None
        self.voice = None
        self.caption = None
        self.captionEntities = None
        self.showCaptionAboveMedia = None
        self.hasMediaSpoiler = None
        self.contact = None
        self.dice = None
        self.game = None
        self.poll = None
        self.venue = None
        self.location = None
        self.newChatMembers = None
        self.leftChatMember = None
        self.newChatTitle = None
        self.newChatPhoto = None
        self.deleteChatPhoto = None
        self.groupChatCreated = None
        self.supergroupChatCreated = None
        self.channelChatCreated = None
        self.messageAutoDeleteTimerChanged = None
        self.migrateToChatId = None
        self.migrateFromChatId = None
        self.pinnedMessage = None
        self.invoice = None
        self.successfulPayment = None
        self.refundedPayment = None
        self.usersShared = None
        self.chatShared = None
        self.connectedWebsite = None
        self.writeAccessAllowed = None
        self.passportData = None
        self.proximityAlertTriggered = None
        self.boostAdded = None
        self.chatBackgroundSet = None
        self.forumTopicCreated = None
        self.forumTopicEdited = None
        self.forumTopicClosed = None
        self.forumTopicReopened = None
        self.generalForumTopicHidden = None
        self.generalForumTopicUnhidden = None
        self.giveawayCreated = None
        self.giveaway = None
        self.giveawayWinners = None
        self.giveawayCompleted = None
        self.videoChatScheduled = None
        self.videoChatStarted = None
        self.videoChatEnded = None
        self.videoChatParticipantsInvited = None
        self.webAppData = None
        self.replyMarkup = None

        self.valid = {
            "id": "id",
            "date": "date",
            "chat": "chat",
            "sender": "sender",
            "sender_chat": "senderChat",
            "sender_boost_count": "senderBoostCount",
            "sender_business_bot": "senderBusinessBot",
            "thread_id": "threadId",
            "business_connection_id": "businessConnectionId",
            "forward_origin": "forwardOrigin",
            "is_topic_message": "isTopicMessage",
            "is_automatic_forward": "isAutomaticForward",
            "reply_to_message": "replyToMessage",
            "external_reply": "externalReply",
            "quote": "quote",
            "reply_to_story": "replyToStory",
            "via_bot": "viaBot",
            "edit_date": "editDate",
            "has_protected_content": "hasProtectedContent",
            "is_from_offline": "isFromOffline",
            "media_group_id": "mediaGroupId",
            "author_signature": "authorSignature",
            "text": "text",
            "entities": "entities",
            "link_preview_options": "linkPreviewOptions",
            "effect_id": "effectId",
            "animation": "animation",
            "audio": "audio",
            "document": "document",
            "paid_media": "paidMedia",
            "photo": "photo",
            "sticker": "sticker",
            "story": "story",
            "video": "video",
            "video_note": "videoNote",
            "voice": "voice",
            "caption": "caption",
            "caption_entities": "captionEntities",
            "show_caption_above_media": "showCaptionAboveMedia",
            "has_media_spoiler": "hasMediaSpoiler",
            "contact": "contact",
            "dice": "dice",
            "game": "game",
            "poll": "poll",
            "venue": "venue",
            "location": "location",
            "new_chat_members": "newChatMembers",
            "left_chat_member": "leftChatMember",
            "new_chat_title": "newChatTitle",
            "new_chat_photo": "newChatPhoto",
            "delete_chat_photo": "deleteChatPhoto",
            "group_chat_created": "groupChatCreated",
            "supergroup_chat_created": "supergroupChatCreated",
            "channel_chat_created": "channelChatCreated",
            "message_auto_delete_timer_changed": "messageAutoDeleteTimerChanged",
            "migrate_to_chat_id": "migrateToChatId",
            "migrate_from_chat_id": "migrateFromChatId",
            "pinned_message": "pinnedMessage",
            "invoice": "invoice",
            "successful_payment": "successfulPayment",
            "refunded_payment": "refundedPayment",
            "users_shared": "usersShared",
            "chat_shared": "chatShared",
            "connected_website": "connectedWebsite",
            "write_access_allowed": "writeAccessAllowed",
            "passport_data": "passportData",
            "proximity_alert_triggered": "proximityAlertTriggered",
            "boost_added": "boostAdded",
            "chat_background_set": "chatBackgroundSet",
            "forum_topic_created": "forumTopicCreated",
            "forum_topic_edited": "forumTopicEdited",
            "forum_topic_closed": "forumTopicClosed",
            "forum_topic_reopened": "forumTopicReopened",
            "general_forum_topic_hidden": "generalForumTopicHidden",
            "general_forum_topic_unhidden": "generalForumTopicUnhidden",
            "giveaway_created": "giveawayCreated",
            "giveaway": "giveaway",
            "giveaway_winners": "giveawayWinners",
            "giveaway_completed": "giveawayCompleted",
            "video_chat_scheduled": "videoChatScheduled",
            "video_chat_started": "videoChatStarted",
            "video_chat_ended": "videoChatEnded",
            "video_chat_participants_invited": "videoChatParticipantsInvited",
            "web_app_data": "webAppData",
            "reply_markup": "replyMarkup"
        }

class MessageEntity(JsonAPI):
    def __init__(self):
        self.valid = {
            "type": "type",
            "offset": "offset",
            "length": "length",
            "url": "url",
            "user": "user",
            "language": "language",
            "custom_emoji_id": "customEmojiId"
        }
        self.type = None
        self.offset = None
        self.length = None
        self.url = None
        self.user = None
        self.language = None
        self.customEmojiId = None

class TextQuote(JsonAPI):
    def __init__(self):
        self.valid = {
            "text": "text",
            "entities": "entities",
            "position": "position",
            "is_manual": "isManual"
        }
        self.text = None
        self.entities = None
        self.position = None
        self.isManual = None

class ExternalReplyInfo(JsonAPI):
    def __init__(self):
        self.valid = {
            "origin": "origin",
            "chat": "chat",
            "message_id": "messageId",
            "link_preview_options": "linkPreviewOptions",
            "animation": "animation",
            "audio": "audio",
            "document": "document",
            "photo": "photo",
            "sticker": "sticker",
            "story": "story",
            "video": "video",
            "video_note": "videoNote",
            "voice": "voice",
            "has_media_spoiler": "hasMediaSpoiler",
            "contact": "contact",
            "dice": "dice",
            "game": "game",
            "giveaway": "giveaway",
            "giveaway_winners": "giveawayWinners",
            "invoice": "invoice",
            "location": "location",
            "poll": "poll",
            "venue": "venue"
        }
        self.origin = None
        self.chat = None
        self.messageId = None
        self.linkPreviewOptions = None
        self.animation = None
        self.audio = None
        self.document = None
        self.photo = None
        self.sticker = None
        self.story = None
        self.video = None
        self.videoNote = None
        self.voice = None
        self.hasMediaSpoiler = None
        self.contact = None
        self.dice = None
        self.game = None
        self.giveaway = None
        self.giveawayWinners = None
        self.invoice = None
        self.location = None
        self.poll = None
        self.venue = None

class ReplyParameters(JsonAPI):
    def __init__(self):
        self.valid = {
            "message_id": "messageId",
            "chat_id": "chatId",
            "allow_sending_without_reply": "allowSendingWithoutReply",
            "quote": "quote",
            "quote_parse_mode": "quoteParseMode",
            "quote_entities": "quoteEntities",
            "quote_position": "quotePosition"
        }
        self.messageId = None
        self.chatId = None
        self.allowSendingWithoutReply = None
        self.quote = None
        self.quoteParseMode = None
        self.quoteEntities = None
        self.quotePosition = None

class MessageOrigin(JsonAPI):
    def __init__(self):
        self.valid = {
            "type": "type",
            "date": "date",
            "sender_user": "senderUser",
            "sender_user_name": "senderUserName",
            "sender_chat": "senderChat",
            "author_signature": "authorSignature"
        }
        self.type = None
        self.date = None
        self.senderUser = None
        self.senderUserName = None
        self.senderChat = None
        self.authorSignature = None

class MessageOriginUser(MessageOrigin):
    def __init__(self):
        super().__init__()
        self.type = 'user'

class MessageOriginHiddenUser(MessageOrigin, JsonAPI):
    def __init__(self):
        super().__init__()
        self.type = 'hiddenUser'

class MessageOriginChat(MessageOrigin, JsonAPI):
    def __init__(self):
        super().__init__()
        self.type = 'chat'

class MessageOriginChannel(MessageOrigin, JsonAPI):
    def __init__(self):
        super().__init__()
        self.type = 'channel'
        self.messageId = None

class MessageAutoDeleteTimerChanged(JsonAPI):
    def __init__(self):
        self.valid = {
            "message_auto_delete_time": "messageAutoDeleteTime"
        }
        self.messageAutoDeleteTime = None

class MessageReactionUpdated(JsonAPI):
    def __init__(self):
        self.valid = {
            "chat": "chat",
            "message_id": "messageId",
            "date": "date",
            "old_reaction": "oldReaction",
            "new_reaction": "newReaction",
            "user": "user",
            "actor_chat": "actorChat"
        }
        self.chat = None
        self.messageId = None
        self.date = None
        self.oldReaction = None
        self.newReaction = None
        self.user = None
        self.actorChat = None

class MessageReactionCountUpdated(JsonAPI):
    def __init__(self):
        self.valid = {
            "chat": "chat",
            "message_id": "messageId",
            "reaction_count": "reactionCount"
        }
        self.chat = None
        self.messageId = None
        self.reactionCount = None

class Update:
    def __init__(self):
        self.valid = {
            "update_id": "id",
            "message": "message",
            "edited_message": "editedMessage",
            "channel_post": "channelPost",
            "edited_channel_post": "editedChannelPost",
            "business_connection": "businessConnection",
            "business_message": "businessMessage",
            "edited_business_message": "editedBusinessMessage",
            "deleted_business_messages": "deletedBusinessMessages",
            "message_reaction": "messageReaction",
            "message_reaction_count": "messageReactionCount",
            "inline_query": "inlineQuery",
            "chosen_inline_result": "chosenInlineResult",
            "callback_query": "callbackQuery",
            "shipping_query": "shippingQuery",
            "pre_checkout_query": "preCheckoutQuery",
            "purchased_paid_media": "purchasedPaidMedia",
            "poll": "poll",
            "poll_answer": "pollAnswer",
            "my_chat_member": "myChatMember",
            "chat_member": "chatMember",
            "chat_join_request": "chatJoinRequest",
            "chat_boost": "chatBoost",
            "removed_chat_boost": "removedChatBoost"
        }
        self.id = None
        self.message = None
        self.editedMessage = None
        self.channelPost = None
        self.editedChannelPost = None
        self.businessConnection = None
        self.businessMessage = None
        self.editedBusinessMessage = None
        self.deletedBusinessMessages = None
        self.messageReaction = None
        self.messageReactionCount = None
        self.inlineQuery = None
        self.chosenInlineResult = None
        self.callbackQuery = None
        self.shippingQuery = None
        self.preCheckoutQuery = None
        self.purchasedPaidMedia = None
        self.poll = None
        self.pollAnswer = None
        self.myChatMember = None
        self.chatMember = None
        self.chatJoinRequest = None
        self.chatBoost = None
        self.removedChatBoost = None
