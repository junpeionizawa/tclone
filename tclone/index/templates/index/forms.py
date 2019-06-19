
from django import forms
#テキストエリアのフォーム利用を可能に
class NewtweetForm(forms.Form):
	 tweet = Forms.CharField(widget=forms.Textarea)