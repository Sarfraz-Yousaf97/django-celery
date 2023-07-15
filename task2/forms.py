from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='FirstName', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class':'from-control mb-3', 'placeholder':'FirstName','id':'form-firstname'}
        ) 
    )
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(
            attrs={'class':'from-control mb-3', 'placeholder':'Email','id':'form-email'}
        ) 
    )
    review = forms.CharField(
        label='Review',widget=forms.Textarea(attrs={'class':'from-control mb-3', 'rows': '5'}
        ) 
    )


    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])