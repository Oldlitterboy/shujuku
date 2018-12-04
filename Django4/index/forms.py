from django import forms
from . models import *
#声明 ChoiceField要用到的数据
# TOPIC_CHOICE =(
#               ('1','好评'),
#               ('2','中评'),
#               ('3','差评'),
#               )
# #表示评论内容的表单控件的class
# #控件1 评论标题-文本框
# class RemarkForm(forms.Form):
#     subject=forms.CharField(label='标题') 
# #控件2 - 电子邮箱 - 邮箱框
#     email=forms.EmailField(label='邮箱')
# #控件3 评论的内容- Textarea
#     message=forms.CharField(label='内容',widget=forms.Textarea)
# #控件4 评论级别- 下拉选择框
#     topic=forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
# #控件5 是否保存-复选框
#     isSaveed=forms.BooleanField(label='是否保存')

# class AuthorForm(forms.Form):
#     name=forms.CharField(label='姓名')
#     age=forms.IntegerField(label='年龄')
#     email=forms.EmailField(label='邮箱')

class AuthorForm(forms.ModelForm):
    class Meta:
        #1关联的model
        #2指定生成控件的字段们
        #3 指定每个控件的label
        model=author
        fields=['name','age','email']
        labels={
            'name':'用户名称',
            'age':'用户年龄',
            'email':'用户邮箱',
        }

class widForm(forms.Form):
    uname=forms.CharField(label='用户名称',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'请输入用户名称'
    }))
    upwd=forms.CharField(label='用户密码',widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'请输入密码'
    }))

class widForm1(forms.ModelForm):
    class Meta:
        model=author
        fields=['name','age','email']
        labels={
            'name':'用户姓名',
            'age':'用户年龄',
            'email':'用户邮箱',
        }
        widgets={
            'age':forms.NumberInput(attrs={
                'placeholder':'请输入年龄','class':'placeholder'}),
            'email':forms.EmailInput(attrs={'placeholder':'请输入电子邮件','class':'placeholder'})
        }