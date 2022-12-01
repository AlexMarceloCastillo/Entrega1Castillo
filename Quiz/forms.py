from django import forms

class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()


class EquipoFormulario(forms.Form):
    nombre = forms.CharField()
    fundacion = forms.DateField()


class PaisFormulario(forms.Form):
    nombre = forms.CharField()
