from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 입력해주세요.')])
    userid = StringField('아이디', validators=[DataRequired('아이디를 입력해주세요.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired('비밀번호를 입력해주세요.'), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호 확인을 입력해주세요.')])
    email = EmailField('이메일', validators=[DataRequired('이메일을 입력해주세요.'), Email()])
    #authority = IntegerField('권한', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    userid = StringField('사용자이름', validators=[DataRequired('아이디를 입력해주세요.'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요.')])

class ImageForm(FlaskForm):
    image = FileField('이미지', validators=[FileRequired(), FileAllowed(['jpg', 'png'], '이미지 파일 (jpg, png) 파일만 가능합니다!')])