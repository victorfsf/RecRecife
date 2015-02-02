# -*- encoding: utf-8 -*-
from django import forms
from recmap.constants import escolhas_feedbackForm
from recmap.models import Feedback


class FeedbackForm(forms.ModelForm):

    escolhas_erros =  [(escolha, escolha) for escolha in escolhas_feedbackForm]

    nome_attrs = {
        'class': 'form-control',
        'placeholder': 'Nome (Opcional)'
    }

    email_attrs = {
        'class': 'form-control',
        'placeholder': 'E-mail (Opcional)'
    }

    erros_attrs = {
        'class': 'form-control',
    }

    desc_attrs = {
        'class': 'form-control',
        'maxlength': '512',
        'rows': '4',
        'placeholder': 'Comentário... (Opcional)'
    }

    nome = forms.CharField(max_length=200, widget=forms.TextInput(attrs=nome_attrs), required=False)
    email = forms.EmailField(max_length=256, widget=forms.TextInput(attrs=email_attrs), required=False)
    erros = forms.ChoiceField(choices=escolhas_erros,
                              widget=forms.Select(attrs=erros_attrs), required=True)
    descricao = forms.CharField(max_length=512, widget=forms.Textarea(attrs=desc_attrs),
                                required=False)

    def clean(self):
        erro_selecionado = self.cleaned_data.get('erros')
        descricao = self.cleaned_data.get('descricao')

        if erro_selecionado == u'Situação do local...':
            raise forms.ValidationError('Seleciona uma situação!', code=0)

        if not ''.join(descricao.split()) and erro_selecionado == u'Outro...':
            raise forms.ValidationError('Descreva a situação!', code=1)

    class Meta:
        model = Feedback
        fields = ('nome', 'email', 'erros', 'descricao',)