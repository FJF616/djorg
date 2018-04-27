from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
# from django.core.context_processors import csrf
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

@login_required
def user_profile(request):
      if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user.profile)
            if form.is_valid():
                  form.save()
                  return HttpResponseRedirect('/accounts/loggedin')
      else:
            user = request.user
            profile = user.profile
            form = ProfileForm(instance=profile)

      args = {}
      args.update(csrf(request))

      args['form'] = form

      return render_to_response('profile.html', args)

def file_upload(request):
      if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                  'uploaded_file_url': uploaded_file_url
            })
      return render(request, 'core/index.html')
#             
#      context = {'bookmarks': Bookmark.objects.all(), 'form': BookmarkForm()}
#     return render(request, 'bookmarks/index.html', context) 