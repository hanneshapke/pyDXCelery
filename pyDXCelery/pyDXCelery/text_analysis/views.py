import time
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from textstat.textstat import textstat

from .models import Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment', ]


class CommentCreate(CreateView):
    model = Comment
    form_class = ContactForm
    success_url = reverse_lazy('add_comment')

    def analyse_text(self, comment):

        time.sleep(10)
        return """
        Reading ease: {} \n
        Smog index: {} \n
        Flesch kincaid grade: {} \n
        Coleman liau index: {} \n
        Automated readability index: {} \n
        Dale_chall readability score: {} \n
        Difficult words: {} \n
        Linsear write formula: {} \n
        Gunning fog: {} \n
        Text standard: {} \n
        """.format(
            textstat.flesch_reading_ease(comment),
            textstat.smog_index(comment),
            textstat.flesch_kincaid_grade(comment),
            textstat.coleman_liau_index(comment),
            textstat.automated_readability_index(comment),
            textstat.dale_chall_readability_score(comment),
            textstat.difficult_words(comment),
            textstat.linsear_write_formula(comment),
            textstat.gunning_fog(comment),
            textstat.text_standard(comment)
        )

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        form.instance.stats = self.analyse_text(form.instance.comment)
        form.instance.save()
        return super(CommentCreate, self).form_valid(form)

    def comments(self):
        return Comment.objects.all()
