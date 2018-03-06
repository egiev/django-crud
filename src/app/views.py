from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.utils import timezone

from .models import Post, Comments

# Create your views here.
def index(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'index.html', context)

def add_comment(request, post_id):
	print (post_id)
	print (request.method)
	if(request.method == 'POST'):
		post = Post.objects.get(pk=post_id)
		text = request.POST['comment']

		if request.user.is_authenticated:
			comment = Comments(post=post, author=request.user, text=text, publish_date=timezone.now())
		else:
			comment = Comments(post=post, author=None, text=text, publish_date=timezone.now())
		comment.save()

		return redirect(reverse('index'))
	else:
		return redirect(reverse('index'))

def update_comment(request, comment_id):
	print(comment_id)
	if(request.method == 'POST'):
		text = request.POST['comment']
		comment = Comments.objects.get(id=comment_id)
		comment.text = text
		comment.save()
		return redirect(reverse('index'))
	else:
		return redirect(reverse('index'))

def delete_comment(request, comment_id):
	print(comment_id)
	if(request.method == 'POST'):
		comment = Comments.objects.get(id=comment_id)
		comment.delete()
		return redirect(reverse('index'))
	else:
		return redirect(reverse('index'))