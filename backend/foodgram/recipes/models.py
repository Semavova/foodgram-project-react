from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ingredients.models import Ingredient
from tags.models import Tag

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта',
        help_text='Название рецепта',
    )
    image = models.ImageField(
        verbose_name='Изображение для рецепта',
        help_text='Изображение для рецепта',
        upload_to='recipes/',
    )
    text = models.TextField(
        verbose_name='Описание рецепта',
        help_text='Описание рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredients',
        related_name='recipes',
        verbose_name='Игредиенты для рецепта',
        help_text='Игредиенты для рецепта',
    )
    tags = models.ManyToManyField(
        Tag,
        through='RecipeTags',
        related_name='recipes',
        verbose_name='Теги рецепта',
        help_text='Теги рецепта',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(360),),
        verbose_name='Время приготовления в минутах',
        help_text='Время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации рецепта',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return (
            f'Рецепт: {self.name} '
            f'Автор: {self.author.username} '
            f'Дата: {self.pub_date} '
            f'Описание: {self.text[:15]} '
        )


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        verbose_name='Ингредиент'
    )
    amount = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(50),),
        verbose_name='Количество ингредиентов'
    )

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return (
            f'В рецепте {self.recipe} '
            f'используется ингредиент {self.ingredient} '
            f'В количестве {self.amount} штук'
        )


class RecipeTags(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        ordering = ('tag',)
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return (
            f'Рецепт: {self.recipe} '
            f'Теги: {self.tag}'
        )


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_favorite',
        verbose_name='Рецепт'
    )

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favorite_recipe'
            ),
        )

    def __str__(self):
        return f'Рецепт {self.recipe} в избранном у {self.user}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_shopping_cart',
        verbose_name='Рецепт'
    )

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_shopping_list_recipe'
            ),
        )

    def __str__(self):
        return f'Рецепт {self.recipe} в списке покупок у {self.user}'
