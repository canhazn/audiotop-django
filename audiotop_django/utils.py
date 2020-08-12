# change django summernote model
from django.conf import settings as django_settings
from audiotop_django import settings

def change_sumernote_attchment_model(ATTACHMENT_MODEL):
    setattr(django_settings, 'SUMMERNOTE_CONFIG', {
        "attachment_model": ATTACHMENT_MODEL
    })



def get_and_save_image_foreignkey(html_content, obj, imageModel, foreignkeyModel):
    """
    Return array of url of images attachment of main model
    """
    img_urls = []

    soup = BeautifulSoup(html_content, 'html.parser')
    imgs = soup.find_all('img')

    for image in imgs:
        if image['src'].find("audiotop") != -1:
            img_urls.append(image['src'])
            # Remove string /media/
            print(image['src'][7:])
            imageObject = models.Image.objects.get(file=image['src'][7:])
            imageObject.project = obj
            imageObject.save()
            print(imageObject)
    return img_urls