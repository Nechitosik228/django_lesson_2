from django.test import TestCase
from .models import Post, User


class BlogTestCase(TestCase):

    @classmethod
    def setUp(self):
        self.user = User.objects.create(
            username="Vasya", 
            email="example@gmail.com", 
            password="qwerty"
        )

        self.post_1 = Post.objects.create(
            title="My first blog",
            content="This is my first blog",
            progress="PB",
            user=self.user,
        )

        self.post_2 = Post.objects.create(
            title="My Trip",
            content="My first trip of 2025",
            progress="DF",
            user=self.user,
        )

        self.post_3 = Post.objects.create(
            title="My home",
            content="Very big house",
            user=self.user,
        )

    def test_get_posts(self):
        posts = Post.objects.all()
        self.assertEqual(len(posts), 3)

    def test_post_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, self.post_1.title)

    def test_post_3_progress(self):
        self.assertEqual(f"{self.post_3.progress}", "DF")

    def test_post_user(self):
        self.assertEqual(self.post_1.user, self.user)

    def test_update_progress_post_2(self):
        post = Post.objects.get(id=2)
        post.progress = "PB"
        post.save()
        self.assertEqual(post.progress, "PB")

    def test_delete_post(self):
        self.post_1.delete()
        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)

    def test_post_delete_when_user_deletes(self):
        self.user.delete()
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)