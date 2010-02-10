from django.views.generic.simple import direct_to_template

def root(request):
  if request.device and request.device.id.lower().find('iphone') > -1:
    template = 'iphone/hello.html'
  else:
    template = 'hello.html'
  
  return direct_to_template(request, template, extra_context=dict(device=request.device))

