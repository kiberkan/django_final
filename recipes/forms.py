from django import forms
from .models import Recipe, RecipeCategory

class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=RecipeCategory.objects.all(), required=True)

    class Meta:
        model = Recipe
        fields = [
            'image', 'title', 'description', 'instructions', 'preparation_time',  'category']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Изображение',
            'title': 'Название',
            'description': 'Описание',
            'instructions': 'Инструкция приготовления',
            'preparation_time': 'Время приготовления(мин)',
            'category': 'Категория',
        }
