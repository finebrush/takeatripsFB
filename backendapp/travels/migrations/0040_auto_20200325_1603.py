# Generated by Django 2.2.7 on 2020-03-25 07:03

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0039_auto_20200325_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buypart',
            name='pin',
        ),
        migrations.AddField(
            model_name='buypart',
            name='pin',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '패션'), (2, '화장품'), (3, '과자'), (4, '전통시장'), (5, '특산물'), (6, '김'), (7, '아몬드'), (8, '기념품'), (9, '대형마트')], default='', max_length=17, verbose_name='Select Pin'),
        ),
        migrations.RemoveField(
            model_name='drinkpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='drinkpart',
            name='pin',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '커피'), (2, '차'), (3, '쥬스'), (4, '분위기있는'), (5, '조용한'), (6, '풍경이좋은'), (7, '케이크'), (8, '도너츠'), (9, '베이커리')], default='', max_length=17, verbose_name='Select Pin'),
        ),
        migrations.RemoveField(
            model_name='eatpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='eatpart',
            name='pin',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '담백한'), (2, '화끈한'), (3, '새콤달콤한'), (4, '전통적인'), (5, '국물이있는'), (6, '볶음요리'), (7, '해산물'), (8, 'BBQ'), (9, '채식')], default='', max_length=17, verbose_name='Select Pin'),
        ),
        migrations.RemoveField(
            model_name='funpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='funpart',
            name='pin',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '체험여행'), (2, '문화여행'), (3, '역사여행'), (4, '아웃도어'), (5, '전망이좋은'), (6, '야경이좋은'), (7, '놀이공원'), (8, '랜드마크'), (9, '산책')], default='', max_length=17, verbose_name='Select Pin'),
        ),
    ]
