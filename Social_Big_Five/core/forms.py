from django import forms
import csv


# https://ipip.ori.org/30facetneo-pi-ritems.htm
def create_test_form():
    
    class TestForm():
        pass
    form = TestForm

    file_data = []
    with open('static/questions.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        file_data = [row for row in reader]
    
    choices = [
        ('1', 'Strongly Disagree'),
        ('2', 'Disagree'),
        ('3', 'Neutral'),
        ('4', 'Agree'),
        ('5', 'Strongly Agree'),
    ]
    for i, data in enumerate(file_data):
        FIELD_NAME = f'question_{i}'
        TestForm.base_fields[FIELD_NAME] = forms.ChoiceField(
            label=f'{data['left']} ... {data['right']}',
            widget=forms.RadioSelect,
            choices=choices,
            required=True
        )

    return form

TestForm = create_test_form()