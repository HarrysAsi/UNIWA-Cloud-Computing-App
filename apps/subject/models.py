import os, datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.cloud.validator import validate_file_extension


def create_image_path(self, filename):
    """
    Function which defines the path for the uploaded images for a team member    :param self:
    :param filename: the file name
    :return: the path where the image is going to be saved
    """
    timestamp = datetime.datetime.now().timestamp()

    return os.path.join('images/subjects/'
                        + str(self.title_en).replace(" ", "_") + "/"
                        + (str(int(timestamp)) + filename))


class Subject(models.Model):
    """
        Subject model which represents a subject
    """

    class Meta:
        db_table = 'subject'
        verbose_name = _('subject')
        verbose_name_plural = _("subject's")

    title_en = models.CharField(_("title en"), max_length=128, blank=False)
    title_el = models.CharField(_("title el"), max_length=128, blank=False)
    image = models.ImageField(verbose_name=_("subject image"),
                              upload_to=create_image_path,
                              default='images/no_img_available.jpg',
                              blank=True,
                              max_length=1024,
                              name="image",
                              )

    description = models.TextField(_("subject description"), blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.title_en}'


def create_file_upload_path(self, filename):
    """
    Function which defines the path for the uploaded images for a team member    :param self:
    :param filename: the file name
    :return: the path where the image is going to be saved
    """
    timestamp = datetime.datetime.now().timestamp()

    return os.path.join('files/exercises/'
                        + str(self.pk).replace(" ", "_") + "/"
                        + (str(int(timestamp)) + filename))


class SubjectExercise(models.Model):
    """
        Subject exercise which represents an exercise for a subject
    """

    class Meta:
        db_table = 'subject_exercise'
        verbose_name = _('subject_exercise')
        verbose_name_plural = _("subject_exercise's")

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(_("exercise Title"), max_length=128, blank=False)
    file = models.FileField(verbose_name=_("file"), upload_to=create_file_upload_path, blank=True,
                            null=False, max_length=1024, validators=[validate_file_extension])

    description = models.TextField(_("exercise description"), blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Exercise: {self.pk} subject"s {self.subject.title_en}'
