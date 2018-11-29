from django.db import models


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(slug__icontains=query)
        )


class Course(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(verbose_name='Descrição', blank=True)
    start_date = models.DateField(
        verbose_name='Data de Início', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem', null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Atualizado em', auto_now=True
    )

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
