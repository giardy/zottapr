# -*- coding: utf-8 -*-

#Context processor sirve para que las imágenes de 'slides' puedan aparecer en el plugin de sliders

#def all_pages(request):
#    from mezzanine.galleries.models import Gallery
#    galleries = Gallery.objects.all()
#    return {'pages': galleries}

def get_pictures(request):
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    slides_dir = os.path.join(path, 'static/media/uploads/slides/')
    os.chdir(slides_dir)
    files = os.listdir(".")
    pictures = []

    for f in files:
        pieces = f.split(".")
        ext = pieces[-1]
        if pieces[ext] in ("jpg", "jpeg", "png", "gif"):
            #print pieces[ext]
            pictures.append(f)

    return {'pictures': pictures}
