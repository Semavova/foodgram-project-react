from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=['user', 'author'],
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(user=models.F('author')),
            ),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return (
            f'Подписчик: {self.user.username},'
            f'автор: {self.author.username}'
        )
