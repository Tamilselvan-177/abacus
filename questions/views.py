from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import Test, Question
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import random

@login_required(login_url='/login/')
def home(request):
    # In your Django view
    levels = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'home.html', {'levels': levels})

@login_required(login_url='/login/')
def start_test(request, level):
    """
    This view generates the test based on the specified level and stores it in the session.
    The question generation logic will change depending on the level selected.
    """
    questions = []

    # Handle different levels dynamically
    if level == 1:
        for i in range(100):
            row1 = random.randint(1, 9)  # Single-digit for Level 1
            row2 = random.randint(1, 9)
            row3 = random.randint(1,row1+row2)
            
            # Define operation for each row
          
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
          
       
            if operation_row3 == 'sub':
                row3=-(row3)
                operation_row3='sub'
            else:
                operation_row3='add'

            # Calculate answers based on operations
            

            # Append question with multiple operations
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })

    elif level == 2:
        for i in range(100):
            row1 = random.randint(10, 99)  # Double-digit for Level 2
            row2 = random.randint(10, 99)
            row3 = random.randint(1, row1 + row2)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
    elif level == 3:
            for i in range(100):
                row1 = random.randint(1, 9)  # Single-digit for Level 1
                row2 = random.randint(1, 9)
                row3 = random.randint(1,row1+row2)
                
                # Define operation for each row
            
                operation_row3 = random.choice(['add', 'sub'])

                # Ensure no negative answers for subtraction
            
        
                if operation_row3 == 'sub':
                    row3=-(row3)
                    operation_row3='sub'
                else:
                    operation_row3='add'

                # Calculate answers based on operations
                

                # Append question with multiple operations
                questions.append({
                    'id': i + 1,
                    'row1': row1,
                    'row2': row2,
                    'row3': row3,
                    'ans': row1 + row2 + row3,
                })
    elif level == 4:
        for i in range(50):
            row1 = random.randint(1, 99)  # Double-digit for Level 2
            row2 = random.randint(1, 99)
            row3 = random.randint(1, row1 + row2)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
        for i in range(50,100):
            row1 = random.randint(1, 9)  # Double-digit for Level 2
            row2 = 'X'
            row3 = random.randint(1, 9)

            # Define operation for each row

            # Ensure no negative answers for subtraction
          

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 * row3,
            })
    elif level == 5:
        for i in range(50):
            row1 = random.randint(10, 99)  # Double-digit for Level 2
            row2 = random.randint(10, 99)
            row3 = random.randint(1, row1 + row2)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
        for i in range(50,100):
            row1 = random.randint(10, 99)  # Double-digit for Level 2
            row2 = 'X'
            row3 = random.randint(10, 99)

            # Define operation for each row

            # Ensure no negative answers for subtraction
          

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 * row3,
            })
    elif level == 6:
        for i in range(50):
            row1 = random.randint(100, 999)  # Double-digit for Level 2
            row2 = random.randint(100, 999)
            row3 = random.randint(100, 999)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
        for i in range(50,100):
            row1 = random.randint(10, 99)  # Double-digit for Level 2
            row2 = 'X'
            row3 = random.randint(10, 99)

            # Define operation for each row

            # Ensure no negative answers for subtraction
          

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 * row3,
            })
    elif level == 7:
        for i in range(50):
            row1 = random.randint(100, 99)  # Double-digit for Level 2
            row2 = random.randint(100, 99)
            row3 = random.randint(100, row1 + row2)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
        for i in range(50,100):
            row1 = random.randint(100, 999)  # Double-digit for Level 2
            row2 = 'X'
            row3 = random.randint(1,10)

            # Define operation for each row

            # Ensure no negative answers for subtraction
          

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 * row3,
            })
    else:
        for i in range(50):
            row1 = random.randint(1000, 9999)  # Double-digit for Level 2
            row2 = random.randint(100, 999)
            row3 = random.randint(100, 500)

            # Define operation for each row
            operation_row3 = random.choice(['add', 'sub'])

            # Ensure no negative answers for subtraction
            if operation_row3 == 'sub':
                row3 = -(row3)
                operation_row3 = 'sub'
            else:
                operation_row3 = 'add'

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 + row2 + row3,
            })
        for i in range(50,100):
            row1 = random.randint(100, 999)  # Double-digit for Level 2
            row2 = 'X'
            row3 = random.randint(10,99)

            # Define operation for each row

            # Ensure no negative answers for subtraction
          

            # Calculate answers based on operations
            # Here, answer is row1 + row2 + row3, depending on the chosen operation
            questions.append({
                'id': i + 1,
                'row1': row1,
                'row2': row2,
                'row3': row3,
                'ans': row1 * row3,
            })

    # Store generated questions and correct answers in session (temporary storage for the duration of the test)
    request.session['questions'] = questions

    # Create a new test entry for the user in the database
    test = Test.objects.create(user=request.user)
    request.session['test_id'] = test.id
    request.session['level'] = level
    qestion=Question.objects.create()
    qestion.test_id=test.id
    qestion.set_data(questions)
    qestion.save()
    # Store test ID in session for later use

    return render(request, 'test_page.html', {'test': test, 'questions': questions,'level':level})

@login_required(login_url='/login/')
def submit_test(request):
    answers = []
    if request.method == "POST":
        test_id = request.POST.get("test_id")  # Get the test ID from the form submission
        level = request.POST.get("level")  # Get the level from the form submission
        
        if not test_id:  # Check if test_id is provided
            return render(request, 'error_page.html', {"error": "Test ID is missing. Please try again."})

        try:
            test = Test.objects.get(id=test_id, user=request.user)  # Fetch the test based on the test ID
        except Test.DoesNotExist:
            return render(request, 'error_page.html', {"error": "Test not found. Please try again."})

        # Retrieve the generated questions from the session
        questions = request.session.get('questions', [])
        time_taken = request.POST.get("remaining_time")
        total_marks = 0
        wrong_answers = 0

        # Process each question and validate the user's answers
        for question in questions:
            user_answer = request.POST.get(f'answer_{question["id"]}', '').strip()  # Get user input for each question

            if user_answer == '':  # If no answer is provided, treat as None
                user_answer = None
            else:
                try:
                    user_answer = int(user_answer)  # Convert to integer if possible
                except (ValueError, TypeError):
                    user_answer = None  # If conversion fails, treat as None

            # Calculate the correct answers

            correct_answer_row1 = question['ans']
           

            # Evaluate the user's answer
            answers.append(user_answer)
            total_answer = correct_answer_row1
            if user_answer == total_answer:
                print("Correct: ",user_answer,total_answer)
                total_marks += 1  # Increment score if the answer is correct
            elif user_answer is  not None :  # Answer is wrong
                print(user_answer)
                wrong_answers += 1

        # Save the test results in the database
        test.marks_obtained = total_marks
        test.wrong_answers = wrong_answers
        test.time_taken = time_taken
        test.level = level
        test.fullname = request.user.get_full_name()
        test.test_id=test_id
        test.set_data(answers)
        test.save()

        print(test_id)
       
        

        # Redirect to the results page with the test ID to show the user's score
        return render(request, 'test_result.html', {'test': test, 'time_taken': time_taken})






    return render(request, 'error_page.html', {"error": "Invalid request method."})


@login_required(login_url='/login/')
def test_result(request, test_id):
    try:
        test = Test.objects.get(id=test_id, user=request.user) 
        answer = test.get_data()  # Assuming this returns a list of answers
        question = Question.objects.get(test_id=test_id)
        questions = question.get_data()  # Assuming this returns the questions
        combined_json = []
        
        for index, item in enumerate(questions):
            combined_item = item.copy()  # Copy the item to avoid modifying the original
            
            if index < len(answer):  # Ensure the second JSON has data at the same index
                # Wrap answer in a dictionary if it's an integer
                combined_item.update({'user_ans': answer[index]})  # Adjust this as needed
            
            combined_json.append(combined_item)
        print(combined_json)
        context = {'combined_json': combined_json}
    except :
        return redirect('home')  # Redirect to home if test not found

    return render(request, 'details.html', context)




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django import forms
# View to handle user registration
class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username


# View to handle user registration
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            # Form data is valid
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.create(
                    first_name=full_name.split(' ')[0],
                    last_name=' '.join(full_name.split(' ')[1:]),
                    username=username,
                    password=make_password(password)
                )
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return render(request, 'signup.html', {'form': form})
        else:
            # Form is not valid, return with errors
            return render(request, 'signup.html', {'form': form})
    
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})


def login_user(request):
    """
    View to handle user login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')  # Replace 'home' with the name of your homepage URL
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'login.html')

@login_required
def view_previous_tests(request):
    
    # Fetch all tests taken by the current user
    return render(request, 'previous_tests.html', {'tests': Test.objects.filter(user=request.user)})

#
def logout_user(request):
    """
    View to handle user logout.
    """
    logout(request)  # Logs the user out
    messages.success(request, 'You have successfully logged out.')
    return redirect('signup')  # Make sure to return the redirect