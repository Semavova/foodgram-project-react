from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название ингредиента',
        help_text='Название ингредиента',
    )
    measurement_unit = models.CharField(
        max_length=10,
        verbose_name='Единица измерения ингредиента',
        help_text='Единица измерения ингредиента',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name
