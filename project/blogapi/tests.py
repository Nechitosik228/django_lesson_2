from django.test import TestCase
from .models import Post, User


class BlogTestCase(TestCase):

    def setUp(self):
        self.user = User(
            username = "Vasya", 
            email = "example@gmail.com", 
            password ="qwerty"
            )
        User.save(self.user)

    
    def create_posts(self):
        self.post_1 = Post(
            title = "My first blog", 
            content = "This is my first blog", 
            progress = "PB", 
            user = self.user
            )
        
        post_2 = Post(
            title = "My Trip", 
            content = "My first trip of 2025", 
            progress = "DF", 
            user = self.user
            )
        
        Post.save(self.post_1)
        Post.save(post_2)
        
    def get_posts(self):
        posts = Post.objects.all()
        print(posts)

    def delete_post(self):
        Post.objects.delete(self.post_1)

    def delete_user(self):
        User.objects.delete(self.user)
