from django import forms

from deals.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):

        # data from the form is fetched using super function
        super(UserForm, self).clean()

        # extract the username and text field from the data
        password = self.cleaned_data.get('password')
        if len(password) < 5:
            self._errors['password'] = self.error_class([
                'Minimum 5 characters required'])
        # return any errors if found
        return self.cleaned_data
