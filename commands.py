from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# Создание пользователей
user1 = User.objects.create_user(username='user1', password='password')
user2 = User.objects.create_user(username='user2', password='password')

# Создание авторов
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавление категорий
categories = ['Sports', 'Politics', 'Education', 'Technology']
category_objects = [Category.objects.create(name=category) for category in categories]

# Добавление постов (статей и новостей)
post1 = Post.objects.create(author=author1, post_type=Post.ARTICLE, title='Article 1', text='Text of article 1')
post2 = Post.objects.create(author=author2, post_type=Post.ARTICLE, title='Article 2', text='Text of article 2')
post3 = Post.objects.create(author=author1, post_type=Post.NEWS, title='News 1', text='Text of news 1')

# Присвоение категорий постам
post1.categories.add(category_objects[0], category_objects[1])
post2.categories.add(category_objects[2])
post3.categories.add(category_objects[3])

# Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user1, text='Comment 1 on article 1')
comment2 = Comment.objects.create(post=post1, user=user2, text='Comment 2 on article 1')
comment3 = Comment.objects.create(post=post2, user=user1, text='Comment 1 on article 2')
comment4 = Comment.objects.create(post=post3, user=user2, text='Comment 1 on news 1')

# Лайки и дислайки постов и комментариев
post1.like()
post1.like()
post2.like()
post2.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment4.dislike()

# Обновление рейтингов авторов
author1.update_rating()
author2.update_rating()

# Получение лучшего пользователя
best_author = Author.objects.order_by('-rating').first()
print(f'Best author: {best_author.user.username}, Rating: {best_author.rating}')

# Получение лучшей статьи
best_post = Post.objects.order_by('-rating').first()
print(f'Best post: {best_post.created_at}, {best_post.author.user.username}, {best_post.rating}, {best_post.title}, {best_post.preview()}')

# Получение всех комментариев к лучшей статье
comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(f'{comment.created_at}, {comment.user.username}, {comment.rating}, {comment.text}')
