from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Question

class BlogPostModelTest(TestCase):
    def setUp(self):
        """Create a BlogPost object for testing."""
        self.post = BlogPost.objects.create(
            title="Test Post",
            content="This is a test blog post.",
        )

    def test_blogpost_str(self):
        """Test the string representation of the BlogPost."""
        self.assertEqual(str(self.post), "Test Post")

    def test_blogpost_creation(self):
        """Test if BlogPost is created successfully."""
        post = BlogPost.objects.get(title="Test Post")
        self.assertEqual(post.content, "This is a test blog post.")

class BlogPostViewTest(TestCase):
    def setUp(self):
        """Create a BlogPost object for testing."""
        self.post = BlogPost.objects.create(
            title="Test Post",
            content="This is a test blog post.",
        )
        self.url = reverse('blog')  # Assuming your URL name for the blog page is 'blog'

    def test_blog_view_status_code(self):
        """Test if the blog page returns a 200 status code."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_blog_view_template(self):
        """Test if the correct template is used for the blog page."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'website/blog.html')

    def test_blog_view_content(self):
        """Test if the blog view contains the correct content."""
        response = self.client.get(self.url)
        self.assertContains(response, "Test Post")  # Check if title appears in response

class ContactViewTest(TestCase):
    def setUp(self):
        """Set up initial data."""
        self.url = reverse('contact')  # Assuming your URL name for the contact page is 'contact'

    def test_contact_form_submission(self):
        """Test if contact form submissions are saved to the database."""
        response = self.client.post(self.url, {'name': 'John Doe', 'question': 'What is Django?'})
        self.assertEqual(response.status_code, 200)  # Check if the form renders again
        self.assertTrue(Question.objects.filter(name='John Doe').exists())  # Check if the question is saved
