from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from .models import FoodIntake, DailyReport
from django.contrib.auth.models import User
from .forms import FoodIntakeForm
from account.models import UserBody

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def tool_main_section(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = FoodIntakeForm(request.POST)
            if form.is_valid():
                food_name = form.cleaned_data['name']
                food_quantity = form.cleaned_data['quantity']
                food_unit = form.cleaned_data['unit']
                food_calories_per_unit = form.cleaned_data['calories_per_unit']

                FoodIntake.objects.create(
                    user=request.user ,
                    name=food_name ,
                    quantity=food_quantity ,
                    unit=food_unit ,
                    calories_per_unit=food_calories_per_unit
                )

                messages.success(request, ('Item added to your food intake. Click calculate or add more items.'))
                return redirect('tool_page')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)

                    return redirect('tool_page')
        else:
            messages.error(request, ('Please Sign In to your account to use our tool.'))
            return redirect('tool_page')
    else:
        form = FoodIntakeForm()
        if request.user.is_authenticated:
            user_food_intake = FoodIntake.objects.filter(user__id=request.user.id, report__isnull=True)
            info = {
                'form':form,
                'food_intake':user_food_intake
            }
            return render(request, 'tool.html', info)
        else:
             return render(request, 'tool.html', {'form':form})



def tool_reset_section(request):
    if request.user.is_authenticated:
        user_food_intake = FoodIntake.objects.filter(user__id=request.user.id, report__isnull=True)
        if user_food_intake:    
            user_food_intake.delete()
            messages.success(request, ('Your food intake has been cleared.'))
            return redirect('tool_page')
        else:
            messages.error(request, ('Your food intake is already empty.'))
            return redirect('tool_page')
    else:
        messages.error(request, ('Please Sign In to your account to use our tool.'))
        return redirect('tool_page')



def tool_calculate_section(request):
    if request.user.is_authenticated:
        user_food_intake = FoodIntake.objects.filter(user__id=request.user.id, report__isnull=True)

        if not user_food_intake.exists():
            messages.error(request, ('There is no food intake to calculate.'))
            return redirect('tool_page')

        total_calories = 0
        for food in user_food_intake:
            if food.unit == 'gram':
                food_calories = (food.quantity / 100) * food.calories_per_unit
            elif food.unit == 'piece':
                food_calories = food.quantity * food.calories_per_unit
            elif food.unit ==  'ml':
                food_calories = (food.quantity / 100) * food.calories_per_unit

            total_calories += food_calories

        user_body_info = get_object_or_404(UserBody, user__id=request.user.id)

        if user_body_info.gender == 'M':
            bmr = (Decimal('10') * user_body_info.weight) + (Decimal('6.25') * user_body_info.height) - (Decimal('5') * user_body_info.age) + Decimal('5')
        elif user_body_info.gender == 'F':
            bmr = (Decimal('10') * user_body_info.weight) + (Decimal('6.25') * user_body_info.height) - (Decimal('5') * user_body_info.age) - Decimal('161')

        if user_body_info.physical_activity == 'little':
            activity_factor = Decimal('1.2')
        elif user_body_info.physical_activity == 'moderate':
            activity_factor = Decimal('1.55')
        elif user_body_info.physical_activity == 'too_much':
            activity_factor = Decimal('1.725')

        tdee = bmr * activity_factor

        calorie_difference = total_calories - tdee

        if total_calories < tdee * Decimal('0.90'):
            body_condition = 'low'
        elif total_calories <= tdee * Decimal('1.10'):
            body_condition = 'normal'
        else:
            body_condition = 'high'

        report = DailyReport.objects.create(
            user=request.user,
            bmr=bmr,
            tdee=tdee,
            total_calories=total_calories,
            calorie_difference=calorie_difference,
            body_condition=body_condition,
            age=user_body_info.age,
            height=user_body_info.height,
            weight=user_body_info.weight,
            gender=user_body_info.gender,
            physical_activity=user_body_info.physical_activity,        
        )

        user_food_intake.update(report=report)
        user_food_intake = FoodIntake.objects.filter(user__id=request.user.id, report=report)

        info = {
            'food_intake':user_food_intake,
            'report':report
        }
        return render(request, 'report.html', info)
    else:
        messages.error(request, ('Please Sign In to your account to use our tool.'))
        return redirect('tool_page')
