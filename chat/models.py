from django.db import models
from auth_user.models import MyUser

# Create your models here.
class Chat(models.Model):
	author = models.ForeignKey(MyUser, related_name='chat_author', on_delete=models.CASCADE)
	companion = models.ForeignKey(MyUser, related_name='chat_companion', on_delete=models.CASCADE)
	last_change = models.DateTimeField(auto_now=True)
	user_last_change = models.ForeignKey(MyUser, related_name='chat_user_last_change', on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		old_chat = Chat.objects.filter(author = self.companion, companion = self.author)
		if len(old_chat):
			raise ValidationError('Name must be unique in pair')
		super(Chat, self).save(*args, **kwargs)



class ChatMessage(models.Model):
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	text = models.TextField(max_length=250)
	date = models.DateTimeField(auto_now_add=True)

	def as_json(self):
		return dict(
			chat = self.chat.id,
			user = self.user.username,
			user_image = self.user.avatar.url,
			text = self.text,
			date = self.date.isoformat())