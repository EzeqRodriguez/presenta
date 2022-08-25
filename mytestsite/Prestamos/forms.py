from django import forms


tiposPre =(
    ("hipotecario", "Prestamo Hipoteario"),
    ("prendario", "Prestamo Prendario"),
    ("personal", "Prestamo Personal"),
)


class ContactForm(forms.Form):
    monto = forms.IntegerField(label="Monto", required=True)
    opcion = forms.ChoiceField(choices = tiposPre,  label='Tipo de prestamo', required=True) 
    fecha = forms.DateField(label='Fecha de Inicio', input_formats=['%Y-%m-%d'], required=True, widget=forms.DateInput(attrs={'class':'form-control mb-1', 'type':'date'}))
    
    
